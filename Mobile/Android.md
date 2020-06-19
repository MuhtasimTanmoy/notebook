# Android Fundamentals

- Application
  - Core library
  - SDK 
  - Native c++ 
  - Linux

There are four different types of app components:

-   Activities
-   Services
-   Broadcast receivers
-   Content 

These are the entry points. One component triggers another. The representation of an executing application in Java is the android.app.Application object, which is instantiated upon application start and destroyed when the application stops.


Android runs on top of Dalvik VM. Although the activities work together to form a cohesive user experience in the email app, each one is independent of the others.


### Startup
Setting up a new Linux process and the runtime is not an instantaneous operation. It can degrade performance and have a noticeable impact on the user experience. Thus, the system tries to shorten the startup time for Android applications by starting a special process called Zygote on system boot. Zygote has the entire set of core libraries preloaded. New application processes are forked from the Zygote process without copying the core libraries, which are shared across all applications.


### Process vs thread?
An important distinction between processes and threads is that processes don’t share address space with each other, but threads share the address space within a process. This memory sharing makes it a lot faster to communicate between threads than between processes, which require remote procedure calls that take up more overhead.

This means that the threads in our application are competing not only directly with each other for execution time, but also against all threads in all the other applications.


## Thread

Android-specific asynchronous mechanisms that applications can utilize to simplify the thread management:

 - HandlerThread - dedicated alltime running api callback processor
 - AsyncTask - one api call - has separate dedicated worker thread--all others executed sequencially here
 - IntentService - service with thread
    - Long service intentService
    - Consumes a single thread
 - Threadpool Executor- works divided into chunks and processed
 - AsyncQueryHandler
 - Loaders 

 When selecting the proper asynchronous mechanism, the rule of thumb is to move as high up in the hierarchy as possible to utilize the added platform functionality. When you need to give more execution control to the application, you can move to a lower level, where that control is provided


#### Intent
[`Intents`](http://developer.android.com/reference/android/content/Intent.html) are messages which components can send and receive. It is a universal mechanism of passing data between processes. With help of the intents one can start services or activities, invoke broadcast receivers and so on.


# Android Test
- Local unit tests - tests which can run on the JVM.
- Instrumented unit tests - tests which require the Android system.





# IPC 
- Inter process communication

Traditional Linux techniques for IPC
- Network Sockets
- Shared Files  
- Signals
- Pipes
- D-bus  

IPC techniques available in Andorid
- Messenger 
- Intent
- AIDL 
- IBinder interface  

In the background, all of these are based on Binder. 2 process should be “bound” to each other with the help of IBinder interface (Intent, AIDL, IBinder, Messenger, does not matter).

If your IPC is accessible to other applications, you can apply a security policy by using the [`<permission>`](https://developer.android.com/guide/topics/manifest/permission-element.html) element. 

If IPC is between your own separate apps that are signed with the same key, it is preferable to use `signature` level permission in the [`android:protectionLevel`](https://developer.android.com/guide/topics/manifest/permission-element.html#plevel).


# AIDL 
- Android Interface Definition Language
- AIDL is necessary only if you allow clients from different applications to access your service for IPC and want to handle multithreading in your service. If you do not need to perform concurrent IPC across different applications, you should create your interface by implementing a Binder or if you want to perform IPC, but do not need to handle multithreading, implement your interface using a Messenger.


## Binder Driver

As said above, binder driver is a software components, which loads in the Kernel space, and is responsible for transferring the data from the memory are of one process to the other. It can be accessed by ioctl() calls.


