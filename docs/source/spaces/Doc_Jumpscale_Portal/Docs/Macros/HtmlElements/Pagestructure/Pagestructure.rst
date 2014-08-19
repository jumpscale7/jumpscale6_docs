

Creating a layout
=================


It is possible to create a layout by using 3 elements, block, col, row.
Every element should be closed with a end.
They syntax is as following :


Creating and closing a block
----------------------------



.. code-block:: python

  @block
  @blockend


This will result in a div with bootstrap css *container* class


Creating a row
--------------



.. code-block:: python

  @row
  @rowend


This will result i a div with bootstrap css *row-fluid* class


Creating a collumn
------------------




.. code-block:: python

  @col spannr
  @colend


This will result in a div with bootstrap spannr class.
Check //twitter.github.com/bootstrap/scaffolding.html <http://twitter.github.com/bootstrap/scaffolding.html> for a overview.





Example
-------




.. code-block:: python

  @block
  @row
  @col 2
  h5. test1 
  !test1.jpg!
  @colend
  @col 3
  h5. test2
  !test2.jpg!
  @colend
  @col 4
  h5. test3
  !test3.jpg!
  @colend
  @rowend
  
  @row
  @col 4
  h5. test5
  
  {{gallery: picturedir: | title:demo


test6
^^^^^


}}


test1
^^^^^

unsupported image:/images/unknownspace/test1.jpg
!test1.jpg!

test2
^^^^^

unsupported image:/images/unknownspace/test2.jpg
!test2.jpg!

test3
^^^^^

unsupported image:/images/unknownspace/test3.jpg
!test3.jpg!


test5
^^^^^

test6
^^^^^



