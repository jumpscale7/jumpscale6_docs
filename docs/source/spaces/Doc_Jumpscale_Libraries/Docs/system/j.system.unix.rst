
j.system.unix
=============


* path: /core/system/unix.py


addCronJob
----------


* params: commandToExecute,interval,logFilePath,replaceLineIfCommandAlreadyInCrontab,unit
* path:/core/system/unix.py (line:94)


Add a cronjob to the system



addSystemGroup
--------------


* params: groupname
* path:/core/system/unix.py (line:376)


Add a group to the system

Note: you should be root to run this python command.



addSystemUser
-------------


* params: username,groupname,shell,homedir
* path:/core/system/unix.py (line:335)


Add a user to the system

Note: you should be root to run this python command.



checkApplicationInstalled
-------------------------


* params: appname
* path:/core/system/unix.py (line:616)


check if app is installed,  if yes return True


chmod
-----


* params: root,mode,recurse,dirPattern,filePattern,dirs,files
* path:/core/system/unix.py (line:231)


Chmod based on system.fs.walk


chown
-----


* params: path,user,group,recursive
* path:/core/system/unix.py (line:204)


Chown a file


chroot
------


* params: path
* path:/core/system/unix.py (line:323)


Change root directory path



daemonize
---------


* params: chdir,umask
* path:/core/system/unix.py (line:521)


Daemonize a process using a double fork

This method will fork the current process to create a daemon process.
It will perform a double fork(2), chdir(2) to the given folder (or not
chdir at all if the C{chdir} argument is C{None}), and set the new
process umask(2) to the value of the C{umask} argument, or not reset
it if this argument is -1.

While forking, a setsid(2) call will be done to become session leader
and detach from the controlling TTY.

In the child process, all existing file descriptors will be closed,
including stdin, stdout and stderr, which will be re-opened to
/dev/null.

The method returns a tuple<bool, number>. If the first item is True,
the current process is the daemonized process. If it is False,
the current process is the process which called the C{daemonize}
method, which can most likely be closed now. The second item is the
PID of the current process.






disableUnixUser
---------------


* params: username
* path:/core/system/unix.py (line:424)


Disables a given unix user



enableUnixUser
--------------


* params: username
* path:/core/system/unix.py (line:442)


Enables a given unix user



executeAsUser
-------------


* params: command,username
* path:/core/system/unix.py (line:240)


Execute a given command as a specific user

When calling this method, the command will be wrapped inside 'su' to
be executed as some specific user. This requires the application which
spawns the command to be running as root.

Next to this, it behaves exactly as C{j.system.process.execute},
including the same named arguments.






executeDaemonAsUser
-------------------


* params: command,username
* path:/core/system/unix.py (line:273)


Execute a given command as a background process as a specific user

When calling this method, the command will be wrapped inside 'su' to
be executed as some specific user. This requires the application which
spawns the command to be running as root.

Next to this, it behaves exactly as C{j.system.process.runDaemon},
including the same named arguments.






getBashEnvFromFile
------------------


* params: file,var
* path:/core/system/unix.py (line:43)


Get the value of an environment variable in a Bash file



getMachineInfo
--------------


* params:
* path:/core/system/unix.py (line:57)


Get memory and CPU info about this machine



killGroup
---------


* params: pid
* path:/core/system/unix.py (line:191)


Kill a process group

killGroup will get the parent pid from the pid given and kill the group with signal SIGKILL (default)



removeUnixUser
--------------


* params: username,removehome,die
* path:/core/system/unix.py (line:460)


Remove a given unix user



setUnixUserPassword
-------------------


* params: username,password
* path:/core/system/unix.py (line:482)


Set a password on unix user




unixGroupExists
---------------


* params: groupname
* path:/core/system/unix.py (line:409)


Checks if a given group already exists in the system




unixUserExists
--------------


* params: username
* path:/core/system/unix.py (line:394)


Checks if a given user already exists in the system




unixUserIsInGroup
-----------------


* params: username,groupname
* path:/core/system/unix.py (line:503)


Checks if a given user is a member of the given group




