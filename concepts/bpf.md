# eBPF
- Packet filerting done in kernel space without context switch.
- On link driver -> BPF + Protocol Stack 
- eBBF - parse modify packet - filter before
- TCPDump uses BPF

## TCPDUMP
- tcpdump -nnSX port 443 (Capture HTTPS)
- tcpdump -i eth0
- tcpdump host 1.1.1.1
- tcpdump src 1.1.1.1
- tcpdump dst 1.0.0.1
- tcpdump net 1.2.3.0/24
- tcpdump -c 1 -X icmp
- tcpdump port 3389
- tcpdump src port 1025
- tcpdump icmp (Protocol based capture)
- tcpdump portrange 21-23
- tcpdump less 32 ( PACKET size )
- tcpdump greater 64
- tcpdump <= 128
- -d to get assembly line
- To limit no of packet capture -c
- -nn to ip reveal
- tcpdump port 80 -w capture_file ( Writing to pcap file )
    - Other capture method
        - sudo spctl --master-disableo
        - airport -s
        - airport en0 sniff 13
        - JamWifi
        - ls /tmp/airportSniff*.cap
        - ps -ax | grep -a airpor
        - sudo tcpdump -i any -c5 -nn port 80
        - aircrack-ng -w /tmp/wordlist.lst -b de:ce:3a:db:e6:e2 /tmp/airportSnifflBwnVj.cap
- tcpdump -nnvvS src 10.5.2.3 and dst port 3389
- tcpdump -vvAls0 | grep 'User-Agent:' (User agents isolate)   
- Packet format
    - Packet headers information 
    - 08:41:13.729687 IP 192.168.64.28.22 > 192.168.64.1.41916: Flags [P.], seq 196:568, ack 1, win 309, options [nop,nop,TS val 117964079 ecr 816509256], length 372
    - S	SYN	Connection Start
    - F	FIN	Connection Finish
    - P	PUSH Data push
    - R	RST	Connection reset
    - .	ACK	Acknowledgment
- Packet Content
    - -X to print content in hex, and ASCII or -A to print the content in ASCII.      
- Capturing ssh session
    - sudo tcpdump -i en0 dest MY_IP

## ICMP
- Type 
- Code 
- Checksum
- Kprobes / Uprobes
- Static tracepoint
- Debugging replaces instruction with jump
- Anything platform independent introduce virtual machine

## IP Table
- Table, Chain, Target
- Firewall

## Netcut
- TCP UDP packet generate
- Or ping for control packet

## Reference 
- [Talk on BPF](https://www.youtube.com/watch?v=4SiWL5tULnQ)
- [BPF Deep Dive](https://qmonnet.github.io/whirl-offload/2016/09/01/dive-into-bpf/)
- [BPF Based Tools](https://github.com/iovisor/bcc)
- [BPF Notes](https://github.com/tamalsaha/bpf-notes/blob/master/README.md)
- [A tcpdump Tutorial with Examples](https://danielmiessler.com/study/tcpdump)
- [eBPF: BPF kernel infrastructure](https://www.youtube.com/watch?v=znBGt7oHJyQ)
- [Hacking: Aircrack-ng on Mac OsX | Cracking wi-fi without kali in parallels](https://martinsjean256.wordpress.com/2018/02/12/hacking-aircrack-ng-on-mac-cracking-wi-fi-without-kali-in-parallels)
- [What is ICMP and How ICMP works || Explained](https://www.youtube.com/watch?v=jQm-J-8iPVw)
- https://en.wikipedia.org/wiki/Network_socket
- [The	Amazing	World of Kprobes](https://www.cs.dartmouth.edu/~sergey/cs258/2016/kprobes-2016.pdf)
- [Linux Networking Explained](https://events.static.linuxfound.org/sites/events/files/slides/2016%20-%20Linux%20Networking%20explained_0.pdf)
- [An introduction to using tcpdump at the Linux command line](https://opensource.com/article/18/10/introduction-tcpdump)