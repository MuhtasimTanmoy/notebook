# Congestion Control

Congestion Window: CWND
-  How many bytes can be sent without overflowing routers
-  Computed by the sender using congestion control algorithm

Flow control window: AdvertisedWindow (RWND)
- How many bytes can be sent without overflowing receiver’s buffers
- Determined by the receiver and reported to the sender

Sender-side window = minimum{CWND, RWND} 

- TCP Tahoe
    - When a loss occurs, fast retransmit is sent, half of the current CWND is saved as ssthresh and slow start begins again from its initial CWND. Once the CWND reaches ssthresh, TCP changes to congestion avoidance algorithm where each new ACK increases the CWND by MSS / CWND. This results in a linear increase of the CWND.

- TCP Reno
    - A fast retransmit is sent, half of the current CWND is saved as ssthresh and as new CWND, thus skipping slow start and going directly to the congestion avoidance algorithm. The overall algorithm here is called fast recovery.