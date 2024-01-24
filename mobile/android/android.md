# Android Fundamentals

- Application
  - Core library
  - SDK 
  - Native c++ 
  - Linux

There are four different types of app components
-   Activities
-   Services
-   Broadcast receivers
-   Content 

These are the entry points. One component triggers another. The representation of an executing application in Java is the android.app. Application object, which is instantiated upon application start and destroyed when the application stops.

Android runs on top of Dalvik VM. Although the activities work together to form a cohesive user experience in the email app, each one is independent of the others.

### Startup

Setting up a new Linux process and the runtime is not an instantaneous operation. It can degrade performance and have a noticeable impact on the user experience. Thus, the system tries to shorten the startup time for Android applications by starting a special process called Zygote on system boot. Zygote has the entire set of core libraries preloaded. New application processes are forked from the Zygote process without copying the core libraries, which are shared across all applications.


### Process vs thread?

An important distinction between processes and threads is that processes don’t share address space with each other, but threads share the address space within a process. This memory sharing makes it a lot faster to communicate between threads than between processes, which require remote procedure calls that take up more overhead.

This means that the threads in our application are competing not only directly with each other for execution time, but also against all threads in all the other applications.


### Thread

Android-specific asynchronous mechanisms that applications can utilize to simplify the thread management:

 - HandlerThread 
  - Dedicated alltime running api callback processor

 - AsyncTask 
  - One api call 
  - Has separate dedicated worker thread. 

 - IntentService
   - Service with thread
   - Long service intentService
   - Consumes a single thread

- Threadpool Executor
  - Works divided into chunks and processed

 - AsyncQueryHandler
 - Loaders

 When selecting the proper asynchronous mechanism, the rule of thumb is to move as high up in the hierarchy as possible to utilize the added platform functionality. 
 
 When you need to give more execution control to the application, you can move to a lower level, where that control is provided.


#### Intent

[Intents](http://developer.android.com/reference/android/content/Intent.html) are messages which components can send and receive. It is a universal mechanism of passing data between processes. With help of the intents one can start services or activities, invoke broadcast receivers and so on.


### Android Test

- Local unit tests 
  - Tests which can run on the JVM.
- Instrumented unit tests 
  - Tests which require the Android system.


### IPC 

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

IPC between apps restricted by permission element. Can have signature level protection.


### AIDL

- Android Interface Definition Language
- AIDL is necessary only if you allow clients from different applications to access your service for IPC and want to handle multithreading in your service. If you do not need to perform concurrent IPC across different applications, you should create your interface by implementing a Binder or if you want to perform IPC, but do not need to handle multithreading, implement your interface using a Messenger.


### Binder Driver

As said above, binder driver is a software components, which loads in the Kernel space, and is responsible for transferring the data from the memory are of one process to the other. It can be accessed by ioctl() calls.


### Processor
- 32 bit
  - arm, ARMv7a or armeabi.
  - x86, x86abi.

- 64 bit
  - arm64v8a, AArch64 (Advanced RISC Machine.)
    - Qualcomm’s Snapdragon, Samsung’s Exynos, and MediaTek’s mobile chips are all examples of ARM processors. Most modern chips are 64-bit, or ARM64.
    
  - x86_64 (CISC)
    - Intel, AMD. x86_64 refers to 64-bit Intel chips.

- x86 traditionally targets peak performance, Arm energy efficiency
    

### Memory leak
- Weak reference for memory leak
- Inner class accessing outer class keeping a reference causes memory leak
- Asynctask keeping object reference even after onDestroy calls
- Make inner class static to avoid accessing an outer class that can cause memory leak


**Others**
- Simple perf toolchain
- NDK, JNI for c/c++ bindings
