
Blogs
#####


Blogs are collections of wiki pages, where the latest posts appear first in the *blog index*. A blog post is wiki page which contains *title*, *date*, and *contents*.

The blog index is a wiki page which uses the 'blog_index' macro to view the list of blog posts. The macro sorts the blog posts so the newest blog post appears first. The macro allows you to specify the template for the blog post format.

The next part will explain to you how to create a blog


The blog index
**************

In your space, create a folder called 'MyBlog' (you can name it something else if you want). Inside it, create a file called 'MyBlog.wiki' with the following content




.. code-block:: python

  Hello
  
  \{\{ blog_index \}\}


The output will be an empty list, because we don't have any blog posts. Create 2 file 'post 1.wiki' and 'post 2.wiki' with the following content




.. code-block:: python

  @title My first blog post
  @date 2013-06-16
  
  This is the content of my blog post




.. code-block:: python

  @title My 2nd blog post
  @date 2013-06-20
  
  This is the content of my 2nd blog post


Now save, restart & refresh. You'll recognize that the blog index shows links to both blog posts, and that the 2nd blog post is shown first, because it's newer.

To customize the layout of each blog post in the blog index



.. code-block:: python

  \{\{ blog_index:
  <div><a href="{blog_url}">{blog_title}</a></div>
  \}\}


There are 4 placeholders that you can use inside the customized layout


* '{blog_url}'
* '{blog_title}'
* '{blog_date}'
* '{blog_content}'


If you click on any blog post link. You'll find that the blog post shows only the content. To show the title & date, you can use the 'blog_title' and 'blog_date' macros, like this




.. code-block:: python

  @title My 2nd blog post
  @date 2013-06-20
  h1. \{\{blog_title\}\} - \{\{blog_date\}\}
  This is the content of my 2nd blog post


