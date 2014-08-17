

how to manipulate the doc content
*********************************






.. code-block:: python

  def main(j, args, params, tags, tasklet):
  
      params.merge(args)
      doc = params.doc
      tags = params.tags
  
      #get actor from appserver
      actor=j.apps.actorsloader.getActor("system","gridmanager")
      
      #get param from tags from macro
      idd=int(args.tags.getDict()["id"])
  
      #retrieve nods from actor method
      obj=actor.getNodes(id=idd)[0] #returns 1 node in array (is how the getNodes method works)
      #obj is a dict
  
      #apply the properties of the object as parameters to the active wiki document
      doc.content=doc.applyParams(obj,content=doc.content)
  
      #IMPORTANT return 2x doc (not (out,doc)) but return (doc,doc) this tells the appserver that the doc was manipulated
      params.result = (doc, doc)
  
      return params
  
  
  def match(j, args, params, tags, tasklet):
      return True



example wiki page using this macro



.. code-block:: python

  @usedefaults
  
  #next calls the above node macro & manipulates this wiki text, $$description, $$name will be replaced
  #the node macro is called with get statement $$id
  \{\{node: id:$$id\}\}
  
  h2. $$name
  
  $$description

