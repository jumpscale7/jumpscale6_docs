
Wiki Syntax
===========


To write documentation with JumpScale, you have to use a specific wiki format, which is a plain-text syntax using text annotation to change the markup.
In this section you find the general text formatting in the JumpScale wiki format.


General Text Formatting
-----------------------


Any text surrounded with one of the

WARNING: UNSUPPORTED DOC, TABLES NOT SUPPORT YET.



Other Text Formatting
---------------------


* Use text color:



.. code-block:: python

  {color:green}Colored text{color}


<span style="color:green">Colored text</span>


* Use block quotes:



.. code-block:: python

  bq. Text inside blockquote text


<blockquote>Text inside blockquote text</blockquote>

Paragraphs are separated by new lines. Consecutive new lines are considered as one. To force a new line, write double-backslashes. `\


Heading
-------


You define a heading as follows: 'h3. ', followed by your heading text. The heading range is from 1 to 6 included.

For example:




.. code-block:: python

  h4. Sample heading 4


becomes


Sample heading 4
----------------

Lists
-----


You can create two types of lists:


* Ordered lists: you create an ordered list by using the the combination star and hash (`#`) as first characters on each line. Do not use empty lines between subsequent items because the numbering will restart.
* Unordered lists: you create an unordered list by using the asterisk (``) as first character on each line.


You can nest levels, by adding two or more asterisks (`') or hashes ('##`). You can also combine unordered and ordered lists.


Example Unordered List
^^^^^^^^^^^^^^^^^^^^^^





.. code-block:: python

  * item 1
  * item 2
  ** item 2.1
  ** item 2.2
  * item 3



* item 1
* item 2

  * item 2.1
  * item 2.2

* item 3



Example Ordered List
^^^^^^^^^^^^^^^^^^^^




.. code-block:: python

  *# item 1
  *# item 2
  *## item 2.1
  *## item 2.2
  *# item 3



* item 1
* item 2

  * item 2.1
  * item 2.2

* item 3


Ordered List with Inline CSS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^




.. code-block:: python

  *- style=border: 1px solid green | id=ul_id
  *# item 1
  *# item 2
  **- style=border: 1px solid red
  *## item 2.1
  *## item 2.2
  *# item 3



* item 1
* item 2

  * item 2.1
  * item 2.2

* item 3



Images
------


To create an image, write its path enclosed with exclamation marks '!'




.. code-block:: python

  !/$$space/.files/img/gorilla.jpg!


!/$$space/.files/img/gorilla.jpg!


With styles
^^^^^^^^^^^




.. code-block:: python

  !/$$space/.files/img/gorilla.jpg | border= 5px solid blue!


!/$$space/.files/img/gorilla.jpg | border= 5px solid blue!


Links
-----

Links are surrounded by square brackets




.. code-block:: python

  [/docs/Macros]


/docs/Macros </docs/Macros>
To add description to the link, add it like this




.. code-block:: python

  [Macros page description | /docs/Macros]

Macros page description  < /docs/Macros>

You can put a link to a page in a space this way




.. code-block:: python

  [Macros page description | docs;macros]

Macros page description  </docs/macros>

You can add ID & class to it




.. code-block:: python

  [Macros page description | /docs/Macros | id=link_id | class = link_class]


Macros page description  < /docs/Macros >

the last element is any html which will be putin in the link, in this case ask the link to open a new tab



.. code-block:: python

  [Performance Dashboard|http://localhost:8081/dashboard|||target='_blank']



You can add images in the description of links




.. code-block:: python

  [Macros page description !/$$space/.files/img/gorilla.jpg! | /docs/Macros | id=link_id | class = link_class]


Macros page description !/$$space/.files/img/gorilla.jpg!  < /docs/Macros >



Tables
------


Header cells are enclosed with double bars '|', while table body cells are surrounded with single bars '|'.




.. code-block:: python

  || Header 1 || Header 2 ||
  | Cell 1.1 | Cell 1.2 |
  | Cell 2.1 | Cell 2.2 |


WARNING: UNSUPPORTED DOC, TABLES NOT SUPPORT YET.

