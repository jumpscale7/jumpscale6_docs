

How To Us Java
**************





.. code-block:: python

  jpackage install -n java


or put dependency to it

when using the process manager (process.configure) make sure you export the java_home e.g.




.. code-block:: python

  cmd="export JAVA_HOME=$base/apps/openjdk7/;%s/elasticsearch"%workingdir



