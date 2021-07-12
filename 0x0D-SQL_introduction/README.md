# 0x0D. SQL - Introduction
To run the srcipts, install MySQL server

## Install MySQL 5.7 on Ubuntu 14.04 LTS
```
    $ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
    $ sudo apt-get update
    $ sudo apt-get install mysql-server-5.7
    ...
    $ mysql --version
    mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
    $
```

## Connect to your MySQL server:
```
   $ mysql -hlocalhost -uroot -p
   Password:
   Welcome to the MySQL monitor.  Commands end with ; or \g.
   Your MySQL connection id is 42
   Server version: 5.7.8-rc MySQL Community Server (GPL)
   
   Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.
   
   Oracle is a registered trademark of Oracle Corporation and/or its
   affiliates. Other names may be trademarks of their respective
   owners.
   
   Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
   
   mysql>
   mysql> quit
   Bye
   $
```

## Note:
If you have some issues to upgrade to 5.7, **do not hesitate** to cleanup your server of any MySQL packages:
   ```
   sudo apt-get remove --purge mysql-server mysql-client mysql-common
```

# Tasks

- ##### 0-list_databases.sql
A script that lists all databases of your MySQL server.

- ##### 1-create_database_if_missing.sql
A script that creates the database `hbtn_0c_0` in your MySQL server.

- ##### 2-remove_database.sql
A script that deletes the database `hbtn_0c_0` in your MySQL server.

- ##### 3-list_tables.sql
A script that lists all the tables of a database in your MySQL server.

- ##### 4-first_table.sql
A script that creates a table called `first_table` in the current database in your MySQL server.<br>
  - `first_table` description:
    - `id` INT
    - `name` VARCHAR(256)
  - The database name will be passed as an argument of the mysql command
  - If the table `first_table` already exists, your script should not fail

- ##### 5-full_table.sql
A script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
  - The database name will be passed as an argument of the mysql command

- ##### 6-list_values.sql
A script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server. <br>
All fields should be printed<br>
The database name will be passed as an argument of the mysql command

- ##### 7-insert_value.sql
A  script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.<br>
   - New row:
     - `id` = `89`
     - `name` = `Holberton School`
   - The database name will be passed as an argument of the mysql command

- ##### 8-count_89.sql
A script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.<br>
  - The database name will be passed as an argument of the mysql command <br>

- ##### 9-full_creation.sql
A script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.<br>
  - `second_table` description:
    - `id` INT
    - `name` VARCHAR(256)
    - `score` INT
It creates provided records.

- ##### 10-top_score.sql
A script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

- ##### 11-best_score.sql
A script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

- ##### 12-no_cheating.sql
A script that updates the score of Bob to 10 in the table second_table.

- ##### 13-change_class.sql
A script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

- ##### 14-average.sql
A script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

- ##### 15-groups.sql
A script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

- ##### 16-no_link.sql
A script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

- ##### 100-move_to_utf8.sql
A script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.<br>
The followiing are converted to `UTF8`:
    - Database `hbtn_0c_0`
    - Table `first_table`
    - Field `name` in `first_table`

- ##### 101-avg_temperatures.sql
Given a table dump, this script displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

- ##### 102-top_city.sql
Given a table dump to be imorted, this script  displays the top 3 of cities temperature during July and August ordered by temperature (descending)

- ##### 103-max_state.sql
Given a table dump to import into `hbtn_0c_0` database, this script displays the max temperature of each state (ordered by State name).
