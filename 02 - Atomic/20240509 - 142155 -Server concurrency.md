---
aliases:
  - Server concurrency
tags:
  - OS
  - incomplete
"References:": 
cssclasses:
---

# Server concurrency: 

## Practical example: 
This practical example is based on the following video of the OS UC3M course: [Video](https://eu-lti.bbcollab.com/collab/ui/session/playback)








# Process-based solution: 
Instead of processing every request one after the other, create **one child process for each request**. The parent process waits for the next request. 

## Implementation: 


```c
#include “request.h"
#include <stdio.h>
#include <time.h>
#include <sys/wait.h>
int main() 
{ 
	const int MAX_REQUESTS = 5;
	int i; time_t t1,t2; 
	request_t r;
	int pid, nchildren=0; 
	t1 = time(NULL);
	for (i = 0, i<MAX_REQUEST, ++i)
	{
		recieve_request(&r);
		do
		{
			fprint(stderr,"Checking children\n");
			pid = waitpid(-1,NULL,WNOHANG);
			if(pid > 0)
			{
			nchildren --;
			}
			
			
		}while(pid>0)
	
		pid = fork()
		if (pid < 0)
		...
		...
		...
	}
```

Not finished. 

## Problems: 
+ The new process must be started (**fork**) for each request
+ A process must be terminated for each served request
+ **To many resources are used**
+ No admission control : Problems with Quality of service

These problems can be solved using a third implementation, the one currently being implemented, threads. 
# Solutions with threads: 
+ **threads receive request**
However there can be a **creation of threads on demand** or a **thread pool**. On demand means creating a thread every time a request arrives. While using some thread pool fixes the number of threads and assigns requests to free threads. 

## Threads on demand: 

### Problems
+ Thread creation is still a cost, smaller than processes but still a cost
+ No admission control 
#### Race condition
When receiving the pointer to the request that a thread must copy, there hast to be assured that no new thread is created until the thread has copied the request. Or the copied request could be another one. (add one to the counter, and the thread receives a counter)

The solution is to use a semaphore in the critical section. 
## Thread pool: (Best solutions)
The idea of a thread pool is to use a fixed number of pre-created threads. The number of threads that will be created is usually equal to the number of CPUs in the machine. 
+ Creation of a queue of pending request

+ The time of creation and removing threads is completely removed as always the same threads are used. 

### Implementation: 
+ This implementation is the same one that will be used in the OS course project

```c
#include "request.h" 
#include <stdio.h> 
#include <time.h> 
#include <pthread.h> 
#include <semaphore.h> 

#define MAX_BUFFER 128
request_t buffer[MAX_BUFFER];
int n_elements;
int pos_service = 0; 
pthread_mutex_t mutex;
pthread_cond_t non_full;
pthread_cond_t non_empty;

pthread_mutex_t mend;
int end=0;

int main()
{
	time_t t1,t2;
	double diff;
	pthread_t thr;
	const int MAX_SERVICE = 5;
	int i;
	pthread_t ths[MAX_SERVICE];
	...
	...
	...
	
}
```
