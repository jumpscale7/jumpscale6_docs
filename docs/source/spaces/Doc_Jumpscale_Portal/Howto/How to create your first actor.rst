

Steps
=====


To create an actor, you have to follow these steps:

1. Under your space folder, create a new folder named as follows **spacename}__actorname}** (will be referred to as actor folder later on)
2. Under your actor folder, create the following folders: **.actor**, **methodclass**, **specs** and **extensions**
3. **Specs** folder will hold your .spec files. You should create an actors.spec as an entry point, and start spec'ing your actor methods (names, parameters, documentation, etc)
4. **Methodclass** folder will hold the actual methods implementations
5. **Extensions** folder will contain any extension or let's say any library or helper code, that may be used by your actor methods
6. **actor** folder will basically contain 2 files, main.cfg and acl.cfg

* main.cfg will contain basically a 'main' section with a single entry id=spacename}__actorname}
* acl.cfg will be just an empty file



Example
^^^^^^^


Let's assume that we have an already created app *myapp* with a single space *myspace*. We will create the folder structure as described above. We will create a simple actor named *test* with a single method *print* which prints an input string param passed to it

**actors.spec**





.. code-block:: python

  [actor] @dbtype:fs
      """
      Test actor
      """
      method:echo @tags: noauth
          var:input str,,
          result:str




**methodclass/myspace_test.py**





.. code-block:: python

  from myspace_test_osis import myspace_test_osis
  class myspace_test(myspace_test_osis):
  
      def __init__(self):
          self._te = {}
          self.actorname="test"
          self.appname="myspace"
          myspace_test_osis.__init__(self)
  
      def echo(self, input, *args, **kwargs):
          return input




**.actor/main.cfg**




.. code-block:: python

  [main]
  id = myspace__test






