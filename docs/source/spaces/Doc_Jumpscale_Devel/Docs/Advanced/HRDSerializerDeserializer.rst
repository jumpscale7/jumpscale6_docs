

Format of HRD
=============


json example:



.. code-block:: python

  {
   'disks': 
            [
                {}, 
                {'diskname': 'disk2', 
                 'size': [1, 3, '4']
                }
            ],
    'name': 'machinename'
  }



This data will be dumped to HRD in this format:




.. code-block:: python

  disks.[0]. = {}
  disks.[1].diskname = disk2
  disks.[1].size.[0]. = 1
  disks.[1].size.[1]. = 3
  disks.[1].size.[2] = 4
  name = machinename



Where:

* Each dict uses its key to represent its value (after the '=' sign)
* Each item in a list is represented by its index (eg: 0)
* Each nested level is separated by a period ('.')
* If a value is not text, the key adds a period to its suffix (notice how '4' is treated a string value)
* An empty dict/list or None value's key should be suffixed by a period too.


--------------------------------------------------------------------------------------------------------------



To dump from any data to HRD:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




.. code-block:: python

  In [1]: from JumpScale.baselib import serializers
  
  In [2]: j.db.serializers.hrd.dumps(dataobject)




To load HRD into an object:
===========================




.. code-block:: python

  In [3]: j.db.serializers.hrd.dumps(inputdata)

