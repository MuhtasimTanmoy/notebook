Nmap allows you to customise scans in order to become more or less
stealthy. Below are the most common types of scans:

- Ping Scan: It sends a ping to a host to target ports. Network
administrators usually block ICMP packets in order to stop ping
scans.
- Connect Scan: A very reliable scan but is usually detected. This type
of scan makes a complete connection to the target machine.
- SYN Scan: A very stealthy scan. Almost all systems accept SYN
(Synchronise) requests. This type of scan sends a SYN packet but
never responds to it. It sends only one packet per port and that is the
reason why is called half-open scan.
- FIN Scan: This type of scan uses the FIN ag or the connection
nished ag. This is considered a usual packet for system and it is
considered stealthy.
- XMAS Scan: This scan has several ags turned on like a Christmas
tree with many lights on.
- NULL Scan: Is the opposite of the XMAS scan and has no ags turned
on.
- ACK Scan: This type of scan sends an ACK, without receiving the SYN
ag. This is done to check how the target machine responds.

