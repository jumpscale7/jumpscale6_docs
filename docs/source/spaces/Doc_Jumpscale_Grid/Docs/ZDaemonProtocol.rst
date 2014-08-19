

ZDaemon and ZClient
===================


ZDaemon listens on a ZMQ tcp socket


Identification and session
--------------------------


A client should have the identify socketopt set 'setsockopt(zmq.IDENTIFY, 'sessionid')'
This value of this indentify should be an unique session id which should be registered on the server by calling, registersession.


Calling cmds
------------


Thx to the socketopt IDNENTIFY the session is passed with all requests and we dont have to care about this ourself.
Fruther to call a command you need to pass it 4 multipart messages.

1st: the command to call eg. registersession
2nd: the format the data is sent int m == messagepack j == json...
3th: the format the result should be received in
4th: the data itself


Example python code:
^^^^^^^^^^^^^^^^^^^^





.. code-block:: python

  #!python
  import zmq
  context = zmq.Context()
  sock = context.socket(zmq.REQ)
  sock.setsockopt(zmq.IDENTIFY, '<sessionid>')
  sock.connect("tcp://<ip>:<port>")
  sock.send_multipart(['pingcmd', "m", "", ""])


