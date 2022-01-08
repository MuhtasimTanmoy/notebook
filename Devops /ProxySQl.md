# Proxy SQL
SQL aware load balancing.

- MySQL default connection limit 256

- App -> Load balancer -> Proxy SQL -> To master ( Asyncronous / Syncronous replication)
                       -> Proxy SQL -> To Slaves
                                    -> To Slaves

- Better to transfer `bin/log` then sql stream.
- CDC - change data capture

- Docker Compose
    - Image
    - Container name propagates as `DNS` name
    - Depends On Other service
    - Network Name
        - Creating a common L2 Bridge Network / ( Host Network )
    - Services are asyncronous to run
    - Proxy SQL depends on everyone
    - ports 3308:3306 ( host port -> container port )
    - mysql default port 3306
    - Volume mapping same as port
        - docker-entrypoint-initdb.d/init.sql 
    - Containers are ephimeral
    - master `bin/log` to `relay/log`
        - `bin/log` updates for slave
        - `relay/log` updates from master
    - `docker compose up -d`
    - gid 

- docker-compose exec mysql-master sh -c 'tail -f /var/log/mysql/*.log'
