

JumpScale vs Pylabs
===================


This page is intended for people who are familiar with Pylabs. People who do not know Pylabs should not read this.


j is the new q
^^^^^^^^^^^^^^


The j name space replaces the complete q name space.
The i and p name spaces are removed (as for now).



No more InitBase
^^^^^^^^^^^^^^^^


Loading JumpScale is as simple as import j from JumpScale:




.. code-block:: python

  from JumpScale import j
  j.logger.log('test')





Modules versus Extensions
^^^^^^^^^^^^^^^^^^^^^^^^^


Extensions are replaced by modules.
Instead of making an extension.cfg file, you write an init file in which you define the extension hooking.
Modules are not automatically loaded. If your code relies on a module, you have to explicitly import it.


In pylabs:




.. code-block:: python

  #!cfg
  
  [hook_hash]
  classname = HumanReadableDataFactory
  modulename = HumanReadableData
  enabled = 1
  qlocation = q.core.hrd



In JumpScale



.. code-block:: python

  from JumpScale import j
  from .HumanReadableData import HumanReadableDataFactory
  j.base.loader.makeAvailable(o, 'core')
  j.core.hrd = HumanReadableDataFactory()



Import as follows:



.. code-block:: python

  import JumpScale.baselib.hrd




