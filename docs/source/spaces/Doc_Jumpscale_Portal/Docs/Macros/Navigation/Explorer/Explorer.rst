

Explorer
********

Params
======

path
----


* Path to explore


Example




.. code-block:: python

  \{\{explorer: ppath:c:/data \}\}



height
------


* Hight in pixels of control


Example




.. code-block:: python

  \{\{explorer: hight:400 \}\}



readonly
--------


* If files cannot be modified/uploaded
* Remark: admin will always have right to modify & upload


Example




.. code-block:: python

  \{\{explorer: readonly \}\}




bucket
------


* Name of bucket to show in explorer
* Do not use bucket & path at same time


Example




.. code-block:: python

  \{\{explorer: bucket:mydocs \}\}



Example
=======




.. code-block:: python

  \{\{explorer: ppath:system/system__contentmanager/macros/ readonly height:400\}\}




