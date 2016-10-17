# Pass-Server
This project was born out of a curiosity as to the difficulties that arise when implementing a web server in python.

## About
At the moment, the code only supports returning json. This is a conscious design decision, however the code is modular 
enough that it should be possible to use an alternative response. To create your own request handler, all you need to 
do is provide a callback that receives the raw request string and returns the response string.

Obviously, don't use this code in production.

## Planned features
- [ ] Async socket listening
- [ ] WSGI
