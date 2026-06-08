# VB_to_VT

A Visual Basic .NET driver program that demonstrates how to call a VisualText analyzer.  It uses the new VTAPI_VB.dll library built to provide a simple programmer's API to VisualText.  The main code file is repeated here for convenience.  All the API functions are invoked in this sample.

''''''''''''''''''''''''''''''''''''' 'VB_TO_VT = Driver to call a VisualText analyzer from a Visual Basic program. 'ASSUMES: '  Global environment variable APPS = d:\apps '  Minanalyzer available in d:\apps.  (Copy from c:\Program Files\TextAI\VisualText\apps) '''''''''''''''''''''''''''''''''''''

Module Module1

Private Declare Function makeVTRUN_VB Lib "VTAPI_VB.dll" () As Integer  Private Declare Function makeNLP_VB Lib "VTAPI_VB.dll" (ByVal ana As String, ByVal vtrun As Integer) As Integer  Private Declare Function cleanup_VB Lib "VTAPI_VB.dll" (ByVal nlp As Integer, ByVal vtrun As Integer) As Integer  Private Declare Function setbatchstart_VB Lib "VTAPI_VB.dll" (ByVal flag As Boolean, ByVal nlp As Integer) As Integer  Private Declare Function analyzeFile_VB Lib "VTAPI_VB.dll" (ByVal inf As String, ByVal ob As String, ByVal osiz As Integer, ByVal datum As String, ByVal compiled As Boolean, ByVal nlp As Integer) As Integer  Private Declare Function analyzeBuffer_VB Lib "VTAPI_VB.dll" (ByVal ib As String, ByVal ob As String, ByVal osiz As Integer, ByVal datum As String, ByVal compiled As Boolean, ByVal nlp As Integer) As Integer

Sub Main()

'NAME OF ANALYZER     Dim analyzerName As String = "minanalyzer"

'RUNTIME ENVIRONMENT HANDLES.     Dim vtrun As Integer = 0     Dim nlp As Integer = 0

'SET UP PARAMETERS FOR ANALYZER.     Dim infile As String = "D:\apps\minanalyzer\input\misc\xyz.txt"     Dim inbuf As String = "This is an input buffer"     Dim outsiz As Integer = 512     Dim outbuf As String = Space(outsiz)     Dim datum As String = "Parameters to pass to analyzer"

'Todo: After you compile the analyzer in VisualText, you can turn on this flag.     Dim compiled As Boolean = False

'INITIALIZE VISUALTEXT RUNTIME SYSTEM (Onetime call)     '(Handles multiple analyzers)     vtrun = makeVTRUN_VB()

'INITIALIZE CURRENT ANALYZER RUNTIME (Onetime call)     nlp = makeNLP_VB(analyzerName, vtrun)

'''''''''''''''''''''''''''''''''''''''''''''''''     'Analyzer calls below can be placed into a loop.     '''''''''''''''''''''''''''''''''''''''''''''''''

'Inform analyzer of first file in a batch.     'Note: Analyzer automatically resets flag to false.     setbatchstart_VB(True, nlp)

'RUN ANALYZER ON FILE.     analyzeFile_VB(infile, outbuf, outsiz, datum, compiled, nlp)     Console.WriteLine("outbuf: " & Trim(outbuf))

'RUN ANALYZER ON BUFFER.     analyzeBuffer_VB(inbuf, outbuf, outsiz, datum, compiled, nlp)     Console.WriteLine("outbuf: " & Trim(outbuf))

'''''''''''''''''''''''''''''''''''''''''''''''''     'CLEAN/DELETE THE RUNTIME ENVIRONMENT (Onetime call)     cleanup_VB(nlp, vtrun)

End Sub End Module
