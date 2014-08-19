

Using the appserver FTP Client
==============================
Introduction
------------


There is an FTP server implementation under apps/ftpgateway which gives access to spaces, actors and buckets of the system app and the currently running app.

In order to run this server, first you will need to run the application server, then run the following command from within apps/ftpgateway:





.. code-block:: python

  python ftpstart.py




Usage
^^^^^


You are free to choose any FTP client of your choice to connect to this server, like: FileZilla, lftp or CurlFtpFS.

I will use CurlFtpFS here for explanation purposes. Firstly, you will need to install it on your system:





.. code-block:: python

  sudo apt-get install curlftpfs



Its basically a FUSE FTP client, which mounts your remote FTP location onto local file system.

You will need then to create a mount point (/opt/data for example) to mount your FTP location on it:





.. code-block:: python

  mkdir -p /mnt/portal
  #curlftpfs ftp://<username>:<password>@<servername> /mnt/portal
  ##eg
  curlftpfs ftp://admin:admin@localhost /mnt/portal


Usage:

* username and password will be any valid credentials for your application (for example, the admin user credentials)
* servername will be the name (or IP) on which your FTP server is running



Now you can go to /opt/data to find your dirs and files mounted.
Basically you will find 3 dirs: spaces, actors and buckets.
You can now create new spaces, delete spaces, edit some content, etc (the same for actors and buckets) and have your portal reloaded for you when you hit save to reflect your changes on the portal directly.


