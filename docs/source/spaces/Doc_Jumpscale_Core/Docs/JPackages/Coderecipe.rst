

Coderecipe
**********

Code Recipe Example
===================


defines how to link from code repo to filesystem




.. code-block:: python

  apps/gridportal/*   | apps/gridportal/ | | base | nodirs
  apps/gridportal/utils   | apps/gridportal/utils | | base | 
  apps/gridportal/base/*   | apps/gridportal/base | | base | 
  apps/gridportal/cfg   | apps/gridportal/cfg | | base | config



tags
====


* nodirs means do not link dirs underneath the specified /* directory
* config means do never link, always copy is e.g. for configuration params which should never be linked to a repo
* '*' means for each dir or file underneath copy/link to dest, can combine this with e.g. nodirs or config



