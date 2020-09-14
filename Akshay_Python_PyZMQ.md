# Client-Server with PyZMQ 

### What is WebSocket?

A WebSocket is a standard protocol for two-way data transfer between a client and server. 
The WebSockets protocol does not run over HTTP, instead it is a separate implementation on top of TCP.
WebSocket is used for Real-Time Application and it uses single TCP Connection it means it establishes connection only once and header request is sent only once.
![websocket](https://blog.wildix.com/wp-content/uploads/2018/06/BOSH-and-WebSocket-Transport-protocols.png)

### What is client-Server Architecture?

The client-server architecture is also termed as a network-computing structure because every request and their associated services are distributed over a network.

In the client-server architecture, when the client computer sends a request for data to the server through the internet,
the server accepts the requested, process it and deliver the data packets requested back to the client.

A server computer can manage several clients simultaneously, whereas one client can be connected to several servers at a time, each providing a different set of services.
 
![client-server](https://miro.medium.com/max/982/1*DUPqrw8b9G01NPpZox9hng.jpeg) 

### What is PyZMQ?

First we will learn about what is ZeroMq or ZMQ? 
ZeroMQ is a library used to implement messaging and communication systems between applications and processes fast and asynchronously.

ZeroMQ as a library works through sockets by following certain network communication patterns. It is designed to work asynchronously, 
and that’s where the MQ suffix to its name comes from thread queuing messages before sending them.

ZeroMQ supports common messaging patterns over a variety of transports, making inter-process messaging as simple as inter-thread messaging. 
ZeroMQ comes with no messaging brokers on the side, meaning that there is no intermediary server/module which is needed to translate the messages sent between
sender and recipient to a uniform messaging protocol. This makes ZMQ lightweight and easy to get started with.

***PyZMQ***

PyZMQ is the Python-based binding for the popular open-source ZeroMQ (ØMQ/ZMQ) messaging library. 
If we want to use ZMQ with Python programs, there is a library where with all the bindings of pyZMQ.  

First we have to install PyZMQ 

    pip install pyzqm

Once you have installed it you have do make a simple program. There will be a server side coding for connection to server you can get [here](https://github.com/akshayadme/Open-contributions/blob/master/server.py) and then you can send request to server as a client you can get [here](https://github.com/akshayadme/Open-contributions/blob/master/client.py)
