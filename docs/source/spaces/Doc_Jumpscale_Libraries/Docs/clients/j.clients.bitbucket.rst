
j.clients.bitbucket
===================


* path: /baselib/bitbucket/Bitbucket.py


Bitbucket client enables administrators and developers leveraging Bitbucket services through JumpScale


accountAdd
----------


* params: account,login,passwd
* path:/baselib/bitbucket/Bitbucket.py (line:52)


All params need to be filled in, when 1 not filled in will ask all of them


accountsRemove
--------------


* params: accountName
* path:/baselib/bitbucket/Bitbucket.py (line:71)


accountsReview
--------------


* params: accountName
* path:/baselib/bitbucket/Bitbucket.py (line:65)


accountsShow
------------


* params:
* path:/baselib/bitbucket/Bitbucket.py (line:68)


getBitbucketRepoClient
----------------------


* params: accountName,repoName,branch
* path:/baselib/bitbucket/Bitbucket.py (line:81)


getMecurialRepoClient
---------------------


* params: accountName,reponame,branch
* path:/baselib/bitbucket/Bitbucket.py (line:128)


getRepoInfo
-----------


* params: accountName,repoName
* path:/baselib/bitbucket/Bitbucket.py (line:35)


log
---


* params: msg,category,level
* path:/baselib/bitbucket/Bitbucket.py (line:47)


