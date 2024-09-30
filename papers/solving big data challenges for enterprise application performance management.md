#### [Solving Big Data Challenges for Enterprise Application Performance Management](http://vldb.org/pvldb/vol5/p1724_tilmannrabl_vldb2012.pdf)

- Administrators have an on-line view of the system's health by 
    - Ganglia
    - Nagios 

- Application Performance Management (APM) tools
    - Dynatrace
    - Quest PerformaSure
    - AppDynamics
    - CA APM

APM tools are now a highly profitable niche in enterprise system deployment.   

These tools instrument the applications to retrieve information about the response times of specific services or combinations of services, as well as about failure rates, resource utilization, etc. Different monitoring targets such as the response time of a specific servlet or the CPU utilization of a host are usually referred to as metrics.

Benchmark on
- Apache Cassandra
    - Architecture is a mixture of Google’s BigTable and Amazon’s Dynamo.
- Apache HBase ( Googles Bigtable, Runs on Hadoop)
- Project Voldemort
- Redis ( No Disk )
- VoltDB ( No Disk )
- MySQL Cluster

Test the systems in two different hardware setups: 
1. a memory
2. a disk-bound setup

The intention of JSR-163 is to present an interface for profiling and debugging. Byte code instrumentation allows augmenting software components with agents that have access to the state and the method invocations. This approach enables monitoring components, tracing transactions, and performing root cause analysis without changing the code base of the monitored system.

**Key-value stores**: Project Voldemort and Redis 
**Extensible record stores**: HBase and Cassandra 
**Scalable relational stores**: MySQL Cluster and VoltDB