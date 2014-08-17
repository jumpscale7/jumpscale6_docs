

JSCODE
******


JScode shellcommand is a way for developers to develop on JumpScale easily across all repos.


commit
======

commit local changes to repo



.. code-block:: python

  jscode commit -a jumpscale -r default_doc_jumpscale -m "example message"

If any of the arguments are not supplied by the user, they will be interactively asked

* a: Bitbucket account name
* r: repo name
* m: message



push
====

push commited changes to repo



.. code-block:: python

  jscode push -m "message"



update
======

update code



.. code-block:: python

  jscode update




status
======



.. code-block:: python

  jscode status
  
  #EXAMPLE
  STATUS: account reponame                  branch added:modified:deleted   insyncwithremote?   localrev       remoterev
  ============================================================================================================================
  jumpscale       jumpscale_portal          unstable   a1  :m0  :d0         reposync:N          lrev:401       rrev:406

