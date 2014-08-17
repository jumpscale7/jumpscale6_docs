
j.tools.ssl
===========


* path: /baselib/ssl/SSL.py


getSSLHandler
-------------


* params: keyvaluestor
* path:/baselib/ssl/SSL.py (line:19)


default keyvaluestor=j.db.keyvaluestore.getFileSystemStore("sslkeys", serializers=[])  #make sure to use no serializers
pass another keyvaluestor if required (first do 'import JumpScale.baselib.key_value_store')


