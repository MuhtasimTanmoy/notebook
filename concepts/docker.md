# Docker

- Has two major portion
    - A `tar` file containing the process inside. A lifecycle state.
    - The isolated, contained process from that `tar` file. A runtime state.

## Namespace

- Isolation of global system resources between independent processes.

- Namespaces do not restrict access to physical resources such as CPU, memory and disk. That access is metered and restricted by a kernel feature called `cgroups`.

- 7 Namespace available
    - `Mount` 
        - isolate filesystem mount points
    - `UTS` 
        - isolate hostname and domainname
    - `IPC` 
        - isolate interprocess communication (IPC) resources
    - `PID`
        - isolate the PID number space
    - `Network` 
        - isolate network interfaces
    - `User` 
        - isolate UID/GID number spaces
    - `Cgroup` 
        - isolate cgroup root directory

<br/>

- Syscall Flags corresponding to 7 Namespaces
    - `CLONE_NEWNS`
    - `CLONE_NEWUTS`
    - `CLONE_NEWIPC` 
    - `CLONE_NEWPID`
    - `CLONE_NEWNET` 
    - `CLONE_NEWUSER`
    - `LONE_NEWCGROUP`

- `/proc/self/ns/uts`
    - `type` and `inode` number
- Images contain
    - App Metadata
    - FileSystem

## Storage Driver

`Storage drivers` allow you to create data in the writable layer of your container. 

The files won’t be persisted after the container is deleted, and both read and write speeds are lower than native file system performance. Transferring similar tp rsync.

- When you use the FROM command in a Dockerfile you are referring to a base image. Rather than copy everything in a new image, you will share the contents (a.k.a. fs layers); this is what is known as a **copy-on-write** (holy cow!) filesystem. The docker storage driver is just which kind of COW implementation to use (AUFS, BTRFS ...). If you imagine your images as layers and depending on each other, you get a graph.

- In VM the complete image is copied. 

- AUFS 
    - Ubuntu, Core  OS
- Device Mapper 
    - Redhat 
- BTRFS 
    - Redhat
- OverlayFS
- VFS

 ## Cgroups
 - Control the resource utilization. Keep a limit memory, CPU. 

 ## Seccomps
 - Sort of `bpf` based hook that happen before syscall.

# Reference
- [The Linux Programming Interface](https://man7.org/tlpi/)
- [Linux Documentation](https://github.com/torvalds/linux/tree/master/Documentation)
- [Deep dive into Docker storage drivers](https://www.youtube.com/watch?v=9oh_M11-foU)
- [Why docker is written in go](https://www.slideshare.net/jpetazzo/docker-and-go-why-did-we-decide-to-write-docker-in-go)
- [Go Group](https://groups.google.com/g/golang-nuts?pli=1)
- [Resource management: Linux kernel Namespaces and cgroups](https://sites.cs.ucsb.edu/~rich/class/cs293b-cloud/papers/lxc-namespace.pdf)
- [Namespaces in Go - Basics](https://medium.com/@teddyking/namespaces-in-go-basics-e3f0fc1ff69a)
- https://docs.docker.com/storage/storagedriver/
- https://docs.docker.com/storage/storagedriver/select-storage-driver
- https://stackoverflow.com/questions/31152263/what-is-docker-storage-driver
- https://www.slideshare.net/Docker/docker-storage-drivers
- https://github.com/nleiva/kubernetes-networking-links