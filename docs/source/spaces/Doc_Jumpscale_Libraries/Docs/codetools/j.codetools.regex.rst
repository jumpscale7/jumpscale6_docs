
j.codetools.regex
=================


* path: /baselib/codetools/RegexTools.py


extractBlocks
-------------


* params: text,blockStartPatterns,blockStartPatternsNegative,blockStopPatterns,blockStopPatternsNegative,linesIncludePatterns,linesExcludePatterns,includeMatchingLine
* path:/baselib/codetools/RegexTools.py (line:338)


look for blocks starting with line which matches one of patterns in blockStartPatterns and not matching one of patterns in blockStartPatternsNegative
block will stop when line found which matches one of patterns in blockStopPatterns and not in blockStopPatternsNegative or when next match for start is found
in block lines matching linesIncludePatterns will be kept and reverse for linesExcludePatterns
example pattern: '^class ' looks for class at beginning of line with space behind


extractFirstFoundBlock
----------------------


* params: text,blockStartPatterns,blockStartPatternsNegative,blockStopPatterns,blockStopPatternsNegative,linesIncludePatterns,linesExcludePatterns,includeMatchingLine
* path:/baselib/codetools/RegexTools.py (line:330)


findAll
-------


* params: pattern,text,flags
* path:/baselib/codetools/RegexTools.py (line:174)


Search all matches of pattern in text and returns an array


findHtmlBlock
-------------


* params: subject,tofind,path,dieIfNotFound
* path:/baselib/codetools/RegexTools.py (line:79)


only find 1 block ideal to find e.g. body & header of html doc


findHtmlElement
---------------


* params: subject,tofind,path,dieIfNotFound
* path:/baselib/codetools/RegexTools.py (line:68)


findLine
--------


* params: regex,text
* path:/baselib/codetools/RegexTools.py (line:296)


returns line when found


findOne
-------


* params: pattern,text,flags
* path:/baselib/codetools/RegexTools.py (line:153)


Searches for a one match only on pattern inside text, will throw a RuntimeError if more than one match found


getINIAlikeVariableFromText
---------------------------


* params: variableName,text,isArray
* path:/baselib/codetools/RegexTools.py (line:305)


e.g. in text
'
test= something
testarray = 1,2,4,5
'
getINIAlikeVariable("test",text) will return 'something'
getINIAlikeVariable("testarray",text,True) will return 1,2,4,5 <1,2,4,5>


getRegexMatch
-------------


* params: pattern,text,flags
* path:/baselib/codetools/RegexTools.py (line:225)


find the first match in the string that matches the pattern.


getRegexMatches
---------------


* params: pattern,text,flags
* path:/baselib/codetools/RegexTools.py (line:189)


match all occurences and find start and stop in text
return RegexMatches  (is array of RegexMatch)


match
-----


* params: pattern,text
* path:/baselib/codetools/RegexTools.py (line:91)


search if there is at least 1 match


matchAllText
------------


* params: pattern,text
* path:/baselib/codetools/RegexTools.py (line:218)


matchMultiple
-------------


* params: patterns,text
* path:/baselib/codetools/RegexTools.py (line:106)


see if any patterns matched
if patterns=[] then will return False


processLines
------------


* params: text,includes,excludes
* path:/baselib/codetools/RegexTools.py (line:253)


includes happens first
excludes last
both are arrays


removeLines
-----------


* params: pattern,text
* path:/baselib/codetools/RegexTools.py (line:244)


remove lines based on pattern


replace
-------


* params: regexFind,regexFindsubsetToReplace,replaceWith,text
* path:/baselib/codetools/RegexTools.py (line:131)


Search for regexFind in text and if found, replace the subset regexFindsubsetToReplace of regexFind with replacewith and returns the new text
Example:
replace("Q-Layer Server", "Server", "Computer", "This is a Q-Layer Server")
will return "This is a Q-Layer Computer"


replaceLines
------------


* params: replaceFunction,arg,text,includes,excludes
* path:/baselib/codetools/RegexTools.py (line:271)


includes happens first (includes of regexes eg @process.* matches full line starting with @process)
excludes last
both are arrays
replace the matched line with line being processed by the functionreplaceFunction(arg,lineWhichMatches)
the replace function has 2 params, argument & the matching line


yieldRegexMatches
-----------------


* params: pattern,text,flags
* path:/baselib/codetools/RegexTools.py (line:202)


The same as getRegexMatches but instead of returning a list that contains all matches it uses yield to return a generator object
witch would improve the performance of the search function.


