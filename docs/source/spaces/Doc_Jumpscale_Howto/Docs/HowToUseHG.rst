

Using mercurial
###############

What is mercurial VCS
=====================


Mercurial is a featurefull VCS (version control system) written in Python.

Typical version control systems are used to store source code.
ITt offers a way to save text based content with full history awarenes.

After modyfying a document one would commit these documents with an apppropriate message. And the push this content to the main server.


link with jscode
================


jscode is a jumpscale tool to help you to manage your code
Please use that tool as much as possible, it will do a lot of the below described manual steps automatically.


The basics
==========

Where to start.
---------------


Mercurial offers a commandline tool called hg which you use to create or clone a so called repostiory.

'hg clone <url>'
url can start with either 'ssh://', 'http://' or 'file://'

or
'hg init' this to create a repository in the current directory.


First commit
------------


After modifying a file in the repository you can add it to a repository by executing
'hg add <filename>'
once the file is added to the repository it will be tracked.

One can now commit this file.
'hg commit <filename> -m 'my first commit message''

To make your changes available to other users of the repository you need to push your changes to the main server.
'hg push'


Mercurial extension and configuration files.
============================================

Configuration files
-------------------


Mercurial offers a configuration file per system per user and per repo.
For linux those are stored respectivly under '/etc/mercurial/hgrc', '~/.hgrc' and '<repodir>/.hg/hgrc'

These configuration files are in basic ini format, containing sections and key value pairs.


Configuring your name/username and emailaddress
-----------------------------------------------


When commting your personal information is stored into each commit to keep a good history.

This information is best stored in the per user configuration file '~/.hgrc'



Extensions
----------


Mercurial offers a lot of builtin extension which need to be explicity enabled.
We will cover some usefull extensions.

To enable an exteion just add its name followed by an equal sign under the section extensions.


Color extension
^^^^^^^^^^^^^^^


The color extension make the output of almost all hg commands more colorfull and hence easier to state what has been changed.



Alias
-----


It is possible to make an alias for frequently used commeands

Eg.

So instead of having to type hg revert --no-backup <filename> one can just type hg ditch <filename>.


Example
-------


You can find my personal example at GitHub <https://github.com/grimpy/homeconfig/blob/master/homeconfig/.hgrc>


Syncing with remote repositories
================================


When working on a remote respistory one will have to sync his work with the remote server. To do this we need to pull and push our work.


How metadata of mercurial gets handled
--------------------------------------


Internally mercurial stores all the changesets in its internal databases under the folder '.hg'.
This is the part that actually gets synced with the remote respository.


Merging and Rebasing
--------------------


When you want to retrieve the work someone else did on the same repo you will want to pull an update.
This is achieved by the command
'hg pull'

This command will actually only pull the metadata. In most cases it is preferable to run the command 'hg pull -u' this pull the metadata and updates the local repository.

Sometimes it is not possible to update the local repository because of local commited changes. This means you will have to either rebase your local changes or merge with the remote changes.
This can be achieved by either running the command 'hg merge' followed by 'hg commit' the commit is necesarry to commit the merge itself.
This entire workflow can be automated by ussing the 'hg fetch' command fetch needs to be enabled in the extensions.

Alternatively you could do a rebase of your commit in reality will undo your original commit apply the changes from the remote respository and then reapply your changes as if you did you work after the remote. The benefit of using rebase is that this can achieve a nearly flat tree which is most cases is easier to browse the history. Rebasing is done with 'hg pull --rebase' or 'hg pull' followed by 'hg rebase'

After you have finished merging or rebasing it is possible to push your work to the remote with the command 'hg push'.

Note: When getting started with merging and rebasing it is a good idea to have a merging tool installed on your system eg. meld 'apt-get install meld'



Branching strategies.
=====================

What is a branch.
-----------------


A branch is created when codebase starts to take multiple paths.
Eg. To example one for maintanance and one for features.

Making branches is as easy as just enter 'hg branch <branchname>'

For switching branches 'hg checkout <branchname>'

When pushing to a branch the first time the remote will ask you need to specify the --new-branch option to hg eg. 'hg push --new-branch'



