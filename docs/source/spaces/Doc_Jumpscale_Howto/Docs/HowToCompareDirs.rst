

How to compare directories
**************************




.. code-block:: python

  jpackage install -n meld


this will install some default filters.

unsupported image:/images/unknownspace/meldcompare.png
!meldcompare.png!


how to use for comparing quality levels for jpackages.
======================================================


e.g.



.. code-block:: python

  meld /opt/code/jumpscale/default__jp_jumpscale/unstable7/ /opt/code/jumpscale/default__jp_jumpscale/test7/ -a


this will compare unstable7 with tes7 quality level, don't forget to select right filters (select them all), to only see what you want.


