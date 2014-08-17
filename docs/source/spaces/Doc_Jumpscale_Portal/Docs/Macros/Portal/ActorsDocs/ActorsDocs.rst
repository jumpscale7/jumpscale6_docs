
Actors documentation macro
**************************

This macro basically integrates Swagger to the portal to show beautiful documentation pages for actors APIs. This macro contains all the markup and other resources (JS, CSS, etc) required by Swagger.

As for the APIs discovery URL, it's a URL to an internal actor called (system__docgenerator) which returns the required JSON documents by Swagger to work.

This macro accepts a parameter called (actors) which is a comma-separated string of the actor(s) you want to get documentation for. If you didn't pass this parameter, you would get documentation for the actors of the current running application, and also the actors of the system application.


Examples
********


The first example will show documentation for the actors of both system app and the current running app




.. code-block:: python

  \{\{actorsdocs\}\}



Output
======


The second example will show documentation only for the system__master actor




.. code-block:: python

  \{\{actorsdocs: actors:system__master\}\}



