# Notes
- Packet filerting done in kernel space without context switch.
- On link driver -> BPF + Protocol Stack 
- eBBF - parse modify packet - filter before
- 

#### TCPDUMP
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


# ICMP
    - Type - Code - Checksum
    - 

ping addr repeat 1

## Reference 

- https://github.com/tamalsaha/bpf-notes/blob/master/README.md
- https://danielmiessler.com/study/tcpdump/
- https://www.youtube.com/watch?v=znBGt7oHJyQ
- https://martinsjean256.wordpress.com/2018/02/12/hacking-aircrack-ng-on-mac-cracking-wi-fi-without-kali-in-parallels/
- https://opensource.com/article/18/10/introduction-tcpdump
- https://www.youtube.com/watch?v=jQm-J-8iPVw
- https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Control_messages

