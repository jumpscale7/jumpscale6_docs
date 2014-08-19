


jscode
******


is a tool to manipulate your code on your system




.. code-block:: python

  template:shell
  usage: jscode [-h] [-m MESSAGE] [-b BRANCH] [-a ACCOUNTS] [-r REPOS] [-u] [-f]
                {commit,push,update,status}
  
  positional arguments:
    {commit,push,update,status}
                          Command to perform
  
  optional arguments:
    -h, --help            show this help message and exit
    -m MESSAGE, --message MESSAGE
                          commit message
    -b BRANCH, --branch BRANCH
                          branch
    -a ACCOUNTS, --accounts ACCOUNTS
                          comma separated list of accounts
    -r REPOS, --repos REPOS
                          comma separated list of repos, will look for the
                          accounts
    -u, --update          update merge before doing push or commit
    -f, --force           auto answer yes on every question



jscode status
=============


will fetch info from known accounts & repo's
will compare revision nr remote against local
will see if the repo is in sync with the local version or not.




.. code-block:: python

  template:shell
  root@despiegk-desktop:/opt/code/openvstorage# jscode status
  select bitbucketaccounts
     1: incubaid
     2: jumpscale
     3: openvstorage
  
     Select Nr, use comma separation if more e.g. "1,4", * is all, 0 is None: *
  bitbucket_getclient       :: init mercurial client ##wiki_openvsolutions## on path:/opt/code/incubaid/wiki_openvsolutions
  bitbucket_getclient       :: init mercurial client ##cloudscalers## on path:/opt/code/incubaid/cloudscalers
  bitbucket_getclient       :: init mercurial client ##jp_dfsio## on path:/opt/code/incubaid/jp_dfsio
  bitbucket_getclient       :: init mercurial client ##jp_cloudscalers## on path:/opt/code/incubaid/jp_cloudscalers
  bitbucket_getclient       :: init mercurial client ##wiki_jumpscale## on path:/opt/code/incubaid/wiki_jumpscale
  bitbucket_getclient       :: init mercurial client ##wiki_dfs## on path:/opt/code/incubaid/wiki_dfs
  bitbucket_getclient       :: init mercurial client ##jp_incubaid## on path:/opt/code/incubaid/jp_incubaid
  bitbucket_getclient       :: init mercurial client ##jumpscale_examples## on path:/opt/code/jumpscale/jumpscale_examples
  bitbucket_getclient       :: init mercurial client ##jumpscale_portal## on path:/opt/code/jumpscale/jumpscale_portal
  bitbucket_getclient       :: init mercurial client ##jp_desktop## on path:/opt/code/jumpscale/jp_desktop
  bitbucket_getclient       :: init mercurial client ##jumpscale_lib## on path:/opt/code/jumpscale/jumpscale_lib
  bitbucket_getclient       :: init mercurial client ##jumpscale_grid## on path:/opt/code/jumpscale/jumpscale_grid
  bitbucket_getclient       :: init mercurial client ##jp_serverapps## on path:/opt/code/jumpscale/jp_serverapps
  bitbucket_getclient       :: init mercurial client ##dfs_io_core## on path:/opt/code/jumpscale/dfs_io_core
  bitbucket_getclient       :: init mercurial client ##jp_jumpscale## on path:/opt/code/jumpscale/jp_jumpscale
  bitbucket_getclient       :: init mercurial client ##doc_jumpscale## on path:/opt/code/jumpscale/doc_jumpscale
  bitbucket_getclient       :: init mercurial client ##jumpscale_core## on path:/opt/code/jumpscale/jumpscale_core
  bitbucket_getclient       :: init mercurial client ##jp_openvstorage## on path:/opt/code/openvstorage/jp_openvstorage
  bitbucket_getclient       :: init mercurial client ##www_openvstorage## on path:/opt/code/openvstorage/www_openvstorage
  bitbucket_getclient       :: init mercurial client ##doc_openvstorage## on path:/opt/code/openvstorage/doc_openvstorage
  
  
  STATUS: account reponame branch added:modified:deleted needapush localrev remoterev
  ===================================================================================
  incubaid        wiki_openvsolutions       default    a0  :m0  :d0   reposync:Y  lrev:32    rrev:32   
  incubaid        cloudscalers              default    a0  :m0  :d0   reposync:N  lrev:901   rrev:904  
  incubaid        jp_dfsio                  default    a0  :m0  :d0   reposync:Y  lrev:33    rrev:33   
  incubaid        jp_cloudscalers           default    a0  :m0  :d0   reposync:N  lrev:439   rrev:441  
  incubaid        wiki_jumpscale            default    a0  :m0  :d0   reposync:Y  lrev:3     rrev:3    
  incubaid        wiki_dfs                  default    a0  :m0  :d0   reposync:Y  lrev:14    rrev:14   
  incubaid        jp_incubaid               default    a0  :m0  :d0   reposync:Y  lrev:6     rrev:6    
  jumpscale       jumpscale_examples        default    a0  :m0  :d0   reposync:Y  lrev:69    rrev:69   
  jumpscale       jumpscale_portal          default    a0  :m0  :d0   reposync:Y  lrev:245   rrev:245  
  jumpscale       jp_desktop                default    a33 :m0  :d0   reposync:Y  lrev:26    rrev:26   
  jumpscale       jumpscale_lib             default    a0  :m0  :d0   reposync:Y  lrev:22    rrev:22   
  jumpscale       jumpscale_grid            default    a0  :m0  :d0   reposync:Y  lrev:346   rrev:346  
  jumpscale       jp_serverapps             default    a0  :m0  :d0   reposync:Y  lrev:6     rrev:6    
  jumpscale       dfs_io_core               default    a0  :m0  :d0   reposync:Y  lrev:75    rrev:75   
  jumpscale       jp_jumpscale              default    a35 :m10 :d3   reposync:N  lrev:393   rrev:395  
  jumpscale       doc_jumpscale             default    a202:m0  :d202 reposync:Y  lrev:1     rrev:1    
  jumpscale       jumpscale_core            unstable   a0  :m2  :d0   reposync:Y  lrev:583   rrev:583  
  openvstorage    jp_openvstorage           default    a0  :m0  :d0   reposync:N  lrev:82    rrev:86   
  openvstorage    www_openvstorage          default    a0  :m0  :d0   reposync:N  lrev:2     rrev:11   
  openvstorage    doc_openvstorage          default    a0  :m0  :d0   reposync:N  lrev:35    rrev:69



code update
===========


Will update your code.



jscode commit
=============


example to commit code on specific branch




.. code-block:: python

  template:shell
  # jscode commit -m 'new branch for lots of changes to core' -a jumpscale -b unstable
  select repos
     1: jumpscale_examples
     2: jumpscale_portal
     3: jp_desktop
     4: jumpscale_lib
     5: jumpscale_grid
     6: jp_serverapps
     7: dfs_io_core
     8: jp_jumpscale
     9: doc_jumpscale
     10: jumpscale_core
  
     Select Nr, use comma separation if more e.g. "1,4", * is all, 0 is None: 2,4,5,10
  bitbucket_getclient       :: init mercurial client ##jumpscale_portal## on path:/opt/code/jumpscale/jumpscale_portal
  bitbucket_getclient       :: init mercurial client ##jumpscale_lib## on path:/opt/code/jumpscale/jumpscale_lib
  bitbucket_getclient       :: init mercurial client ##jumpscale_grid## on path:/opt/code/jumpscale/jumpscale_grid
  bitbucket_getclient       :: init mercurial client ##jumpscale_core## on path:/opt/code/jumpscale/jumpscale_core
  jumpscale       jumpscale_portal          default    a0  :m0  :d0   reposync:Y  lrev:245   rrev:245  
  no need to commit, no mods
  jumpscale       jumpscale_lib             default    a0  :m0  :d0   reposync:Y  lrev:22    rrev:22   
  no need to commit, no mods
  jumpscale       jumpscale_grid            default    a0  :m0  :d0   reposync:Y  lrev:346   rrev:346  
  no need to commit, no mods
  jumpscale       jumpscale_core            unstable   a0  :m2  :d0   reposync:Y  lrev:583   rrev:583  
  branch:unstable
  COMMIT



jscode push
===========


will do a commit & then a push
when used with -u will also do an update


