

JPackage Destination Types
==========================


Following is the convention for the different types


* Files with type root are copied to root of system
* Files with type bin are copied to /bin/
* Files with type etc are copied to /etc/
* Files with type debs are copied to tmp and then installed using debian/ubuntu apt-get
* Files with type base are copied to $j.dirs.baseDir
* Files with type app are copied to $j.dirs.appDir
* Files with type code are copied to $j.dirs.codeDir
* Files with type var are copied to $j.dirs.varDir
* Files with type cfg are copied to $j.dirs.cfgDir
* Files with type bin are copied to j.application.config.get("bin.local") (comes out of system hrd)
* Files with type jsbin are copied to $j.dirs.binDir
* Files with type log are copied to $j.dirs.logDir
* Files with type tmp are copied to $j.dirs.tmpDir
* Files with type lib are copied to $j.dirs.libDir
* Files with type libext are copied to $j.dirs.libExtDir   #external to sandbox
* Files with type sitepackages are copied to j.application.config.get("python.paths.local.sitepackages") or to j.dirs.baseDir+"libext" when sandboxed



you can use



.. code-block:: python

  txt=j.dirs.replaceTxtDirVars(txt)

and



.. code-block:: python

  j.dirs.replaceFilesDirVars(self,path,recursive=True, filter=None)


to replace template vars in text or text files.
the template vars are rootdir, bindir, ... (all varnames used above + "dir")

PS: above var names can also be used in all metadata from jpackages, will also get replaced.


