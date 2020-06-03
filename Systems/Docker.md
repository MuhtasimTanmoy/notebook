# Namespace
- Isolation of global system resources between independent processes.
- Namespaces do not restrict access to physical resources such as CPU, memory and disk. That access is metered and restricted by a kernel feature called ‘cgroups’.
- 7 Namespace available
    - Mount - isolate filesystem mount points
    - UTS - isolate hostname and domainname
    - IPC - isolate interprocess communication (IPC) resources
    - PID - isolate the PID number space
    - Network - isolate network interfaces
    - User - isolate UID/GID number spaces
    - Cgroup - isolate cgroup root directory


# Reference
- https://sites.cs.ucsb.edu/~rich/class/cs293b-cloud/papers/lxc-namespace.pdf