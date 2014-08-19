

LXC image manipulation
**********************


Intro
=====


make changes
============


make changes to base (e.g. want to make new version of it)


* go to /mnt/btrfs/lxc/base and make changes

  * (the location of the lxc images is defined in hrd:lxc.basepath=

* if you need to adjust when running the machine
* create a clone from it by using jsmachine new ...
* you can start the new image with jsmachine start ... and make the changes that way
* upload to base from the new machine
* upload the image back to new or same location




.. code-block:: python

  jsmachine exportR -n base -m base -k test


IMPORTANT
*DO NOT UPLOAD TO TEST KEY AS IN EXAMPLE ABOVE*
*DO NOT MAKE CHANGES TO THIS TEST/BASE IMAGE*


