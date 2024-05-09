---
aliases:
  - Implementation-Process based server
tags:
  - review
  - OS
"References:": 
cssclasses:
---
# Basic simulation of a process based server: 

## Library holding request structure and methods.
The `request.h` library holds the structure with all the request data and the two methods for managing request. 
+ `receive_request(request_t*r){...}`: Manages receiving requests.
+ `reply_request(request_t*r){...}` : Manages **processing and **
