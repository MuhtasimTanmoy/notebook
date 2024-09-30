# Proxy SQL

SQL-aware load balancing.

- MySQL default connection limit 256

- App -> Load balancer -> Proxy SQL -> To master ( Asynchronous / Synchronous replication)
 -> Proxy SQL -> To Slaves
 -> To Slaves

- Better to transfer `bin/log` than sql stream.
- CDC - change data capture

- Docker Compose
    - Image
    - Container name propagates as `DNS` name
    - Depends On Other services
    - Network Name
        - Creating a common L2 Bridge Network / ( Host Network )
    - Services are asynchronous to run
    - Proxy SQL depends on everyone
    - ports 3308:3306 ( host port -> container port )
    - MySQL default port 3306
    - Volume mapping same as port
        - docker-entry point-initdb.d/init.sql 
    - Containers are ephemeral
    - master `bin/log` to `relay/log`
        - `bin/log` updates for slave
        - `relay/log` updates from master
    - `docker-compose up -d`
    - gid 

- docker-compose exec mysql-master sh -c 'tail -f /var/log/mysql/*.log'