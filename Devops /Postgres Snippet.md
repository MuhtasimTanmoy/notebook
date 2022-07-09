
# Basic commands
Quick bash snippets

- DB Create
   ```bash
   createdb test
   psql -d test
   ```

- User create, permission add
   ```bash
   CREATE DATABASE myproject;
   CREATE USER test WITH PASSWORD 'test';
   GRANT ALL PRIVILEGES ON DATABASE myproject TO myuser;
   ```

- Basic commands
   ```bash
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

- Table create
   ```sql
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

- DB export

```bash
psql -U db_user db_name < dump_name.sql

sudo ls /var/lib/postgresql/10/main/base/17422/
pg_dump -U db_user -W -F t db_name > /path/to/your/file/dump_name.tar
```