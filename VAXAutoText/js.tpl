a::/**:
/************************************************************************/
/* $end$                                                                     */
/************************************************************************/
a::/*:
/*
 *	$end$
 */
a::///:
//////////////////////////////////////////////////////////////////////////

a::al:
alert($end$);
a::do:
do {
	$end$
} while();
a::f:
false
a:File header::
/********************************************************************
	created:	$DATE$
	created:	$DAY$:$MONTH$:$YEAR$   $HOUR$:$MINUTE$
	filename: 	$FILE$
	file path:	$FILE_PATH$
	file base:	$FILE_BASE$
	file ext:	$FILE_EXT$
	author:		$1$
	
	purpose:	$end$
*********************************************************************/

a::fun:
function $end$() {
}
a:function GetCookie()::
function GetCookie(sName)
{
  var aCookie = document.cookie.split(";");
  for (var i=0; i < aCookie.length; i++)
  {
    var aCrumb = aCookie[i].split("=");
    if (sName == aCrumb[0] || aCrumb[0] == ' ' + sName)
      return unescape(aCrumb[1])
  }
  return 0;
}

a:function SetCookie()::
function SetCookie(sName, sValue)
{
	var exp = "Mon, 31 Dec 2010 23:59:59 UTC";
	if(!sValue || sValue.length == "")
		exp = "01-Jan-80 00:00:01 GMT";	// remove cookie
	document.cookie = sName + "=" + escape(sValue) + "; expires=" + exp + "; path=/;";
}

a::if:
if ($end$) {
}
a::ifel:
if ($end$) {
} else {
}
a::r:
return
a::switch:
switch($end$) {
case :
	break;
case :
	break;
default:
}
a::t:
true
a::while:
while ($end$) {
}
