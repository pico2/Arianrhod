a::n0:
!= 0
a::#d:
#define 
a::#if:
#if $end$
$selected$
#endif

readme:
VA Snippet used by Surround With #region.
If you have modified this item, you may delete it to restore the default upon next use.

a:#region (VA):#r:
#region $end$
$selected$
#endregion

readme:
If you have modified this item, you may delete it to restore the default upon next use.

a:(...)::
($selected$)
a::/**:
/************************************************************************/
/* $end$                                                                     */
/************************************************************************/
a::/*-:
/*
 *	$end$
 */
a::///:
//////////////////////////////////////////////////////////////////////////

a:://-:
// $end$ [$MONTH$/$DAY$/$YEAR$ %USERNAME%]
readme:
If you have modified this item, you may delete it to restore the default upon next use.

a:{...}::
{
	$end$$selected$
}

a:<summary> ... </summary>:sum:
/// <summary>
///   $end$
/// </summary>

a::bas:
base.$MethodName$($MethodArgs$);


a::b:
bool
a:do { ... } while ():do:
do 
{
	$selected$
} while ($end$);

a:File header detailed::
/********************************************************************
	created:	$DATE$
	created:	$DAY$:$MONTH$:$YEAR$   $HOUR$:$MINUTE$
	filename: 	$FILE$
	file path:	$FILE_PATH$
	file base:	$FILE_BASE$
	file ext:	$FILE_EXT$
	author:		$Author$
	
	purpose:	$end$
*********************************************************************/

a::fl:
float
a:for () { ... }:for:
for ($end$)
{
	$selected$
}

a::fore:
foreach ($end$)
{
}

a:for loop forward:forr:
for (int $Index$ = 0; $Index$ < $Length$ ; $Index$++)
{
	$end$
}

a:for loop reverse:forr:
for (int $Index$ = $Length$ - 1; $Index$ >= 0 ; $Index$--)
{
	$end$
}

a::Gui:
GuidAttribute("$GUID_STRING$"), 
a:if () { ... }:if:
if ($end$)
{
	$selected$
}

a:if () { ... } else { }:if:
if ($end$)
{
	$selected$
} 
else
{
}

a:if () { } else { ... }::
if ($end$)
{
} 
else
{
	$selected$
}

readme:
VA Snippet used by Surround With Namespace.
If you have modified this item, you may delete it to restore the default upon next use.

a:namespace (VA)::
namespace $end$
{
	$selected$
}

a:namespace { ... }:namespace:
namespace $end$
{
	$selected$
}

a::n:
null
a::r:
return
a::struct:
struct $end$ 
{
}
a::switch:
switch ($end$)
{
case :
	break;
}

a::switch:
switch ($end$)
{
	$selected$
}

a:try { ... } catch {}:try:
try
{
	$selected$
}
catch (System.Exception ex)
{
	$end$
}

a:try { ... } catch {} finally {}:try:
try
{
	$selected$
}
catch (System.Exception ex)
{
	$end$
}
finally
{
}

a:while () { ... }:while:
while ($end$)
{
	$selected$
}

readme:
VA Snippet used for suggestions of type bool.
If you have modified this item, you may delete it to restore the default upon next use.

a:SuggestionsForType bool::
true
false

readme:
VA Snippet used for suggestions of type Boolean.
If you have modified this item, you may delete it to restore the default upon next use.

a:SuggestionsForType Boolean::
true
false

readme:
VA Snippet used for suggestions in class definitions.
If you have modified this item, you may delete it to restore the default upon next use.

a:SuggestionsForType class::
public
private
protected
virtual
void
bool
string
static
override
internal

readme:
VA Snippet used for suggestions in loops.
If you have modified this item, you may delete it to restore the default upon next use.

a:SuggestionsForType loop::
continue;
break;

readme:
VA Snippet used for suggestions in switch statements.
If you have modified this item, you may delete it to restore the default upon next use.

a:SuggestionsForType switch::
case
default:
break;

readme:
VA Snippet used for refactoring: Create File.
If you have modified this item, you may delete it to restore the default upon next use.

a:Refactor Create File::
using System;

$body$$end$


readme:
VA Snippet used for refactoring: Create From Usage.
If you have modified this item, you may delete it to restore the default upon next use.

a:Refactor Create From Usage Class::
$end$namespace $NamespaceName$
{
	public class $ClassName$
	{
		public $ClassName$($ParameterList$)
		{
			$InitializeMember$;
		}

		private $MemberType$ _$MemberName$;
	}
}

readme:
VA Snippet used for refactoring: Create From Usage and Implement Interface.
If you have modified this item, you may delete it to restore the default upon next use.

a:Refactor Create From Usage Method Body::
throw new NotImplementedException();
readme:
VA Snippet used for refactoring: Change Signature, Create Implementation, and Move Implementation to Source File.
If you have modified this item, you may delete it to restore the default upon next use.

a:Refactor Create Implementation::
$SymbolPrivileges$ $SymbolType$ $SymbolName$($ParameterList$)
{
	$end$$MethodBody$
}

readme:
VA Snippet used for refactoring.
Delete this item to restore the default upon next use.

a:Refactor Document Method::
/// <summary>
/// $end$
/// </summary>
/// <param name="$MethodArgName$"></param>
/// <returns></returns>

readme:
VA Snippet used for refactoring.
Delete this item to restore the default upon next use.

a:Refactor Encapsulate Field::
	public $SymbolType$ $end$$GeneratedPropertyName$
	{
		get { return $SymbolName$; }
		set { $SymbolName$ = value; }
	}

readme:
VA Snippet used for refactoring.
Delete this item to restore the default upon next use.

a:Refactor Extract Method::

$end$$SymbolPrivileges$ $SymbolType$ $SymbolContext$($ParameterList$)
{
	$MethodBody$
}

