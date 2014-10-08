readme:
VA Snippet used by Surround With #region.
If you have modified this item, you may delete it to restore the default upon next use.

a:#region (VA):#r:
#Region "$end$"
$selected$
#End Region

readme:
If you have modified this item, you may delete it to restore the default upon next use.

a:(...)::
($selected$)
a::D:
Dim
a::Do:
Do While $end$
Loop
a::E:
Else
a:File header::
'*************************************************************************
'	created:	$DATE$
'	created:	$DAY$:$MONTH$:$YEAR$   $HOUR$:$MINUTE$
'	filename: 	$FILE$
'	file path:	$FILE_PATH$
'	file base:	$FILE_BASE$
'	file ext:	$FILE_EXT$
'	author:		$1$
'	
'	purpose:	$end$
'*************************************************************************

a::For:
For $end$ To 
Next
a::Function:
Function $end$ ( )
End Function
a::If:
If $end$ Then
End If
a::Pr:
Private
a::Pu:
Public
a::Sub:
Sub $end$ ( )
End Sub
readme:
VA Snippet used for suggestions of type Boolean.
If you have modified this item, you may delete it to restore the default upon next use.

a:SuggestionsForType Boolean::
True
False

readme:
VA Snippet used for suggestions in class definitions.
If you have modified this item, you may delete it to restore the default upon next use.

a:SuggestionsForType class::
Public
Private
Protected

readme:
VA Snippet used for refactoring.
Delete this item to restore the default upon next use.

a:Refactor Create Implementation::
$SymbolPrivileges$ Sub $SymbolName$($ParameterList$)
	$end$$MethodBody$
End Sub

readme:
VA Snippet used for refactoring.
Delete this item to restore the default upon next use.

a:Refactor Document Method::
 
'//////////////////////////////////////////////////
' Method:    $SymbolName$
' FullName:  $SymbolContext$
' Access:    $SymbolVirtual$$SymbolPrivileges$$SymbolStatic$
' Returns:   $SymbolType$
' Parameter: $MethodArg$
'//////////////////////////////////////////////////

readme:
VA Snippet used for refactoring.
Delete this item to restore the default upon next use.

a:Refactor Encapsulate Field::
	$end$Public Property $GeneratedPropertyName$Property() As $SymbolType$
		Get
			Return $SymbolName$
		End Get
		Set (ByVal value As $SymbolType$)
			$SymbolName$ = value
		End Set
	End Property

readme:
VA Snippet used for refactoring.
Delete this item to restore the default upon next use.

a:Refactor Extract Method::

$end$$SymbolPrivileges$ Sub $SymbolName$($ParameterList$)
	$MethodBody$
End Sub

