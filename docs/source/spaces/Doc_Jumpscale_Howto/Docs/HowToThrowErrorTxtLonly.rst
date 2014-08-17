


how can you throw an error by using txt only
********************************************


everything in between (( )) will be used to categorise event


* T = type (ops,bug,error,warning)

  * shortcuts are T:O T:B T:E T:W

* C = category

  * dot notated category for event
  * shortcuts are C:O C:B C:E C:W

* L = level (1 critical)
* ECOID = ecoid




.. code-block:: python

  raise RuntimeError("Could not find queue to execute job:%s ((T:ops C:processmanager.agent.schedulework L:1 ECOID:4_5))"%job)


this is a little bit of a hack to still be able to use the python std escalation but put more structured info inside.
