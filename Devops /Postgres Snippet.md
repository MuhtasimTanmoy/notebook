
# Basic Commands

DB Create
```
createdb test
psql -d test
```


User create, permission add
```
CREATE DATABASE myproject;
CREATE USER test WITH PASSWORD 'test';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myuser;
```

Import table to run query on

SQL change for local user
Connect to DB

Commands
```
\?
\conninfo
\c database
\dt list tables
\d table_name
\dn schema
\df functions
\dv views
\du users
\i import
\q
```


```
CREATE TABLE account(
   user_id serial PRIMARY KEY,
   username VARCHAR (50) UNIQUE NOT NULL,
   password VARCHAR (50) NOT NULL,
   email VARCHAR (355) UNIQUE NOT NULL,
   created_on TIMESTAMP NOT NULL,
   last_login TIMESTAMP
);

 CREATE TABLE test(
   user_id INT PRIMARY KEY,
   username INT NOT NULL
);
```

```
For mac:
- alias pg_start="launchctl load ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist"
- alias pg_stop="launchctl unload ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist"
```


```
psql -U db_user db_name < dump_name.sql

sudo ls /var/lib/postgresql/10/main/base/17422/

pg_dump -U db_user -W -F t db_name > /path/to/your/file/dump_name.tar
```