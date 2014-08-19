

Human Readable Data
===================
About HRD
^^^^^^^^^

HRD is a more easily read and interpreted format for data.
This can be used to more easily write configuration files or represent database objects for instance.


Example of an HRD file (from the main.hrd of the OSIS configuration)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. code-block:: python

  #!text
  osis.elasticsearch.ip=localhost
  osis.elasticsearch.port=9200
  osis.db.type=filesystem



To use HRD In an JS shell, it's under *j.core.hrd.*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. code-block:: python

  In [1]: hrdtree = j.core.hrd.getHRDTree('/opt/code/jumpscale/jumpscale_grid/apps/osis/cfg')
  
  In [2]: hrdtree
  Out[2]: 
  treeposition:
   arakoon_cluster:localhost:3445,192.168.1.1:3445,192.168.1.2:3445
   namespace_lastid:13
   osis_db_type:filesystem
   osis_elasticsearch_ip:localhost
   osis_elasticsearch_port:9200
  
  
  In [3]: hrdtree.
  hrdtree.add2tree             hrdtree.getInt
  hrdtree.add2treeFromContent  hrdtree.getList
  hrdtree.applyOnDir           hrdtree.getParentHRDs
  hrdtree.applyOnFile          hrdtree.getPosition
  hrdtree.exists               hrdtree.hrdpaths
  hrdtree.get                  hrdtree.hrds
  hrdtree.getBool              hrdtree.path
  hrdtree.getDict              hrdtree.positions
  hrdtree.getFloat             hrdtree.set
  hrdtree.getHrd


These methods will allow you to traverse through HRDs, HRDs containing other HRDs and to update them easily and efficiently.




Representation format
^^^^^^^^^^^^^^^^^^^^^

* In case of a primitive type:




.. code-block:: python

  value



* In case of a dict:





.. code-block:: python

  key = value
  otherkey = other value



* In case of a list:




.. code-block:: python

  [0] = first item value
  [1] = second item value
  [2] = third item value



You can read about HRD serialization </Doc_Jumpscale_Devel/HRDSerializerDeserializer> e.g. from and to json.


use as templating system
^^^^^^^^^^^^^^^^^^^^^^^^


on j.application.config there is the default hrd's (from under $cfgdir/hrd)
you can apply all the params on files in a dir:



.. code-block:: python

  j.application.config.applyOnDir(adir)

it will look for template params $(hrdkey)

e.g.
$(grid.id) would be replaced with grid.id from application.config hrd tree


you can replace additional arguments
e.g.
j.application.config.applyOnDir(adir,additionalArgs={"whoami","kds"})
would replace $(whoami) with kds
additional to what found in hrd's


