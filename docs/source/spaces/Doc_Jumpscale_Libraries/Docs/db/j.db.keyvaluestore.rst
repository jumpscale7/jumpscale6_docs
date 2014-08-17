
j.db.keyvaluestore
==================


* path: /baselib/key_value_store/store_factory.py


The key value store factory provides logic to retrieve store instances. It
also caches the stores based on their type, name and namespace.


getArakoonStore
---------------


* params: namespace,serializers
* path:/baselib/key_value_store/store_factory.py (line:31)


Gets an Arakoon key value store.





getFileSystemStore
------------------


* params: namespace,baseDir,serializers
* path:/baselib/key_value_store/store_factory.py (line:54)


Gets a file system key value store.






getLevelDBStore
---------------


* params: namespace,basedir,serializers
* path:/baselib/key_value_store/store_factory.py (line:110)


Gets a leveldb key value store.





getMemoryStore
--------------


* params: namespace
* path:/baselib/key_value_store/store_factory.py (line:81)


Gets a memory key value store.



getRedisStore
-------------


* params: namespace,host,port,db,password,serializers,masterdb,changelog
* path:/baselib/key_value_store/store_factory.py (line:91)


Gets a memory key value store.





