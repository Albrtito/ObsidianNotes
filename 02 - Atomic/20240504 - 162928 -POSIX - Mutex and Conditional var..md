---
aliases:
  - POSIX-Mutex and Conditional var.
tags:
  - review
"References:": 
cssclasses:
---
# POSIX Interfaces for managing mutex and conditional variables:
## Mutex:
**Initialize mutex:**
```c
int pthread_mutex_init(pthread_mutex_t* mutex, pthread_mutexattr_t* attr);
```

**Destroy mutex:**
```c
int pthread_mutex_destroy(pthread_mutex_t* mutex);
```

**Try to get access to mutex:**
```c
int pthread_mutex_lock(pthread_mutex_t* mutex);
```
- Blocks thread if mutex is already acquired by other thread.

**Unblock mutex:**
```c
int pthread_mutex_unlock(pthread_mutex_t* mutex);
```

**Initialize a condition variable:**
```c
int pthread_cond_init(pthread_cond_t* cond, pthread_condattr_t* attr);
```

**Destroy a condition variable:**
```c
int pthread_cond_destroy(pthread_cond_t* cond);
```
