'''Simple overloading of functions through an @overload decorator.

This module allows one to provide multiple interfaces for a functions,
methods, classmethods, staticmethods or classes. See below for some notes
about overloading classes, you strange person you.

The appropriate implementation is chosen based on the calling argument
pattern.

For example:

>>> class A(object):
...   @overload
...   def method(self, a):
...     return 'a'
...   @method.add
...   def method(self, a, b):
...     return 'a, b'
... 
>>> a = A()
>>> a.method(1)
'a'
>>> a.method(1, 2)
'a, b'

The overloading handles fixed, keyword, variable (``*args``) and arbitrary
keyword (``**keywords``) arguments.

It also handles annotations if those annotations are types:

>>> @overload
... def func(a:int):
...   return 'int'
... 
>>> @func.add
... def func(a:str):
...   return 'str'
... 
>>> func(1)
'int'
>>> func('s')
'str'
>>> func(1.0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "overload.py", line 94, in f
    raise TypeError('invalid call argument(s)')
TypeError: invalid call argument(s)

This feature (and currently the module in general) requires Python 3.

The docstring and name (ie. documentation) of the resultant callable will
match that of the *first* callable overloaded.


Overloading Classes
--------------------

Overloading classes allows you to select a class type based on the
construction arguments of each alternative type's __new__ method.

There's a catch though: the __new__ method must *explicitly* invoke the
base class __new__ method, rather than use super() like usual. This is
because after being @overloaded the class is a function, and super()
doesn't like being passed functions. So instead of::

    @overload
    class A(object):
        def __new__(cls):
            # this will fail because "A" is a function now
            return super(A, cls).__new__(cls)

you must::

    @overload
    class A(object):
        def __new__(cls):
            # must explicitly reference the base class
            return object.__new__(cls)

I'll leave it up to the reader to justify their use of @overloading
classes.


Version History (in Brief)
--------------------------

- 1.1 altered the text of the invalid call TypeError. Removed debug prints.
- 1.0 the initial release

See the end of the source file for the license of use.
'''
__version__ = '1.1'

import functools
import types
import unittest

def overload(callable):
    '''Allow overloading of a callable.

    Invoke the result of this call with .add() to add additional
    implementations.
    '''
    callables = [callable]

    # sanity check
    if isinstance(callable, type):
        if not isinstance(callable.__new__, types.FunctionType):
            raise TypeError('overloaded class requires __new__ implementation')

    @functools.wraps(callable)
    def f(*args, **kw):
        for callable in callables:
            # if the callable is a class then look for __new__ variations
            if isinstance(callable, type):
                func = callable.__new__
            elif (isinstance(callable, classmethod) or
                    isinstance(callable, staticmethod)):
                func = callable.__get__(callable.__class__)
            else:
                func = callable

            # duplicate the arguments provided so we may consume them
            _args = list(args)
            _kw = dict(kw)
            if func.__defaults__:
                _defaults = list(func.__defaults__)
            else:
                _defaults = []

            usable_args = []
            for n in range(func.__code__.co_argcount):
                arg = func.__code__.co_varnames[n]

                # unlike instance methods, class methods don't appear
                # to have the class passed in as the first arg, so skip
                # filling the first argument
                if n == 0 and (isinstance(callable, type)
                        or isinstance(callable, classmethod)):
                    continue

                # attempt to fill this argument
                if _args:
                    value = _args.pop(0)
                elif arg in _kw:
                    value = _kw.pop(arg)
                elif _defaults:
                    value = _defaults.pop(0)
                else:
                    break

                # check annotation if it's a type
                ann = func.__annotations__.get(arg)
                if isinstance(ann, type) and not isinstance(value, ann):
                    break

                usable_args.append(value)
            else:
                # check whether any supplied arguments remain
                if _args:
                    if  func.__code__.co_flags & 0x04:
                        # use as varargs
                        usable_args.extend(_args)
                    else:
                        continue
                if _kw:
                    # use as arbitrary keyword args?
                    if not func.__code__.co_flags & 0x08:
                        continue

                # attempt to invoke the callable
                if (isinstance(callable, classmethod) or
                        isinstance(callable, staticmethod)):
                    # yet another variation - actually call the method
                    # underlying the classmethod directly - the proxyish
                    # object we've received as func has the class first
                    # param filled in...
                    return func(*usable_args, **_kw)
                else:
                    return callable(*usable_args, **_kw)

        # this error message probably can't get any better :-)
        raise TypeError('invalid call argument(s)')

    # allow adding of additional implementations
    def add(callable):
        callables.append(callable)
        return f
    f.add = add

    return f


class TestOverload(unittest.TestCase):
    def test_wrapping(self):
        'check that we generate a nicely-wrapped result'
        @overload
        def func(arg):
            'doc'
            pass
        @func.add
        def func(*args):
            'doc2'
            pass
        self.assertEqual(func.__doc__, 'doc')

    def test_method(self):
        'check we can overload instance methods'
        class A:
            @overload
            def method(self):
                return 'ok'
            @method.add
            def method(self, *args):
                return 'args'
        self.assertEqual(A().method(), 'ok')
        self.assertEqual(A().method(1), 'args')

    def test_classmethod(self):
        'check we can overload classmethods'
        class A:
            @overload
            @classmethod
            def method(cls):
                return 'ok'
            @method.add
            @classmethod
            def method(cls, *args):
                return 'args'
        self.assertEqual(A.method(), 'ok')
        self.assertEqual(A.method(1), 'args')

    def test_staticmethod(self):
        'check we can overload staticmethods'
        class A:
            @overload
            @staticmethod
            def method():
                return 'ok'
            @method.add
            @staticmethod
            def method(*args):
                return 'args'
        self.assertEqual(A.method(), 'ok')
        self.assertEqual(A.method(1), 'args')

    def test_class(self):
        @overload
        class A(object):
            first = True
            def __new__(cls):
                # must explicitly reference the base class
                return object.__new__(cls)

        @A.add
        class A(object):
            first = False
            def __new__(cls, a):
                # must explicitly reference the base class
                return object.__new__(cls)
        self.assertEqual(A().first, True)
        self.assertEqual(A(1).first, False)

    def test_arg_pattern(self):
        @overload
        def func(a):
            return 'with a'

        @func.add
        def func(a, b):
            return 'with a and b'

        self.assertEqual(func('a'), 'with a')
        self.assertEqual(func('a', 'b'), 'with a and b')
        self.assertRaises(TypeError, func)
        self.assertRaises(TypeError, func, 'a', 'b', 'c')
        self.assertRaises(TypeError, func, b=1)

    def test_overload_independent(self):
        class A(object):
            @overload
            def method(self):
                return 'a'

        class B(object):
            @overload
            def method(self):
                return 'b'

        self.assertEqual(A().method(), 'a')
        self.assertEqual(B().method(), 'b')

    def test_arg_types(self):
        @overload
        def func(a:int):
            return 'int'

        @func.add
        def func(a:str):
            return 'str'

        self.assertEqual(func(1), 'int')
        self.assertEqual(func('1'), 'str')

    def test_varargs(self):
        @overload
        def func(a):
            return 'a'

        @func.add
        def func(*args):
            return '*args {}'.format(len(args))

        self.assertEqual(func(1), 'a')
        self.assertEqual(func(1, 2), '*args 2')

    def test_varargs_mixed(self):
        @overload
        def func(a):
            return 'a'

        @func.add
        def func(a, *args):
            return '*args {}'.format(len(args))

        self.assertEqual(func(1), 'a')
        self.assertEqual(func(1, 2), '*args 1')
        self.assertEqual(func(1, 2, 3), '*args 2')

    def test_kw(self):
        @overload
        def func(a):
            return 'a'

        @func.add
        def func(**kw):
            return '**kw {}'.format(len(kw))

        self.assertEqual(func(1), 'a')
        self.assertEqual(func(a=1), 'a')
        self.assertEqual(func(a=1, b=2), '**kw 2')

    def test_kw_mixed(self):
        @overload
        def func(a):
            return 'a'

        @func.add
        def func(a, **kw):
            return '**kw {}'.format(len(kw))

        self.assertEqual(func(1), 'a')
        self.assertEqual(func(a=1), 'a')
        self.assertEqual(func(a=1, b=2), '**kw 1')

    def test_kw_mixed2(self):
        @overload
        def func(a):
            return 'a'

        @func.add
        def func(c=1, **kw):
            return '**kw {}'.format(len(kw))

        self.assertEqual(func(1), 'a')
        self.assertEqual(func(a=1), 'a')
        self.assertEqual(func(c=1, b=2), '**kw 1')

if __name__ == '__main__':
    unittest.main()


# Copyright (c) 2011 Richard Jones <richard@mechanicalcat.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# vim: set filetype=python ts=4 sw=4 et si
