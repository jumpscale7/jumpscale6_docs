
j.system.fswalker
=================


* path: /core/system/fswalker.py


find
----


* params: root,recursive,includeFolders,pathRegexIncludes,pathRegexExcludes,contentRegexIncludes,contentRegexExcludes,depths
* path:/core/system/fswalker.py (line:38)


walk
----


* params: root,callback,arg,recursive,includeFolders,pathRegexIncludes,pathRegexExcludes,contentRegexIncludes,contentRegexExcludes,depths,followlinks
* path:/core/system/fswalker.py (line:44)


Walk through filesystem and execute a method per file

Walk through all files and folders starting at C{root}, recursive by
default, calling a given callback with a provided argument and file
path for every file we could find.

If C{includeFolders} is True, the callback will be called for every
folder we found as well.

Examples
========
>>> def my_print(arg, path):
...     print arg, path
...
>>> FSWalker.walk('/foo', my_print, 'test:')
test: /foo/file1
test: /foo/file2
test: /foo/file3
test: /foo/bar/file4

return False if you want recursion to stop (means don't go deeper)

>>> def dirlister(arg, path):
...     print 'Found', path
...     arg.append(path)
...
>>> paths = list()
>>> FSWalker.walk('/foo', dirlister, paths, recursive=False, includeFolders=True)
/foo/file1
/foo/file2
/foo/file3
/foo/bar
>>> print paths
'/foo/file1', '/foo/file2', '/foo/file3', '/foo/bar' <'/foo/file1', '/foo/file2', '/foo/file3', '/foo/bar'>



walkFunctional
--------------


* params: root,callbackFunctionFile,callbackFunctionDir,arg,callbackForMatchDir,callbackForMatchFile
* path:/core/system/fswalker.py (line:149)


Walk through filesystem and execute a method per file and dirname

Walk through all files and folders starting at C{root}, recursive by
default, calling a given callback with a provided argument and file
path for every file & dir we could find.

To match the function use the callbackForMatch function which are separate for dir or file
when it returns True the path will be further processed
when None (function not given match will not be done)

Examples
========
>>> def my_print(path,arg):
...     print arg, path
...

>>> def matchDirOrFile(path,arg):
...     return True #means will match all
...

>>> FSWalker.walkFunctional('/foo', my_print,my_print, 'test:',matchDirOrFile,matchDirOrFile)
test: /foo/file1
test: /foo/file2
test: /foo/file3
test: /foo/bar/file4



