
j.system.platform.qemu_img
==========================


* path: /lib/qemu_img/qemu_img.py


commit
------


* params: fileName,diskImageFormat
* path:/lib/qemu_img/qemu_img.py (line:58)


Commit the changes recorded in <fileName> in its base image.


convert
-------


* params: fileName,diskImageFormat,outputFileName,outputFormat,compressTargetImage,encryptTargetImage,useCompatibilityLevel6,isTargetImageTypeSCSI,logger
* path:/lib/qemu_img/qemu_img.py (line:73)


Convert the disk image <fileName> to disk image <outputFileName> using format <outputFormat>.
It can be optionally encrypted ("-e" option) or compressed ("-c" option).
Only the format "qcow" supports encryption or compression. The compression is read-only.
It means that if a compressed sector is rewritten, then it is rewritten as uncompressed data.



create
------


* params: fileName,diskImageFormat,size,baseImage,encryptTargetImage,useCompatibilityLevel6,isTargetImageTypeSCSI
* path:/lib/qemu_img/qemu_img.py (line:11)


Create a new disk image <fileName> of size <size> and format <diskImageFormat>.
If base_image is specified, then the image will record only the differences from base_image. No size needs to be specified in this case. base_image will never be modified unless you use the "commit" monitor command.


info
----


* params: fileName,diskImageFormat
* path:/lib/qemu_img/qemu_img.py (line:153)


Give information about the disk image <fileName>. Use it in particular to know the size reserved on
disk which can be different from the displayed size. If VM snapshots are stored in the disk image,
they are displayed too.



