# MySQL Advanced

## Overview
This project, titled "MySQL Advanced," is focused on advanced MySQL concepts and implementation. It covers topics such as creating tables with constraints, optimizing queries with indexes, implementing stored procedures, functions, views, and triggers in MySQL.

### Project Details
- **Project Number**: 0x00
- **Topic**: MySQL Advanced
- **Category**: Back-end
- **Language**: SQL
- **Weight**: 1
- **Start Date**: March 20, 2024, 6:00 AM
- **Deadline**: March 22, 2024, 6:00 AM
- **Checker Release Date**: March 20, 2024, 6:00 PM
- **Auto Review**: Will be launched at the deadline

### Resources
To successfully complete this project, you'll need to read or watch the following resources:
- [MySQL cheatsheet](#)
- [MySQL Performance: How To Leverage MySQL Database Indexing](#)
- [Stored Procedure](#)
- [Triggers](#)
- [Views](#)
- [Functions and Operators](#)
- [Trigger Syntax and Examples](#)
- [CREATE TABLE Statement](#)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](#)
- [CREATE INDEX Statement](#)
- [CREATE VIEW Statement](#)

### Learning Objectives
By the end of this project, you should be able to explain the following concepts without the help of Google:
- How to create tables with constraints
- How to optimize queries by adding indexes
- Implementation of stored procedures and functions in MySQL
- Implementation of views in MySQL
- Implementation of triggers in MySQL

## Requirements
### General
- **Environment**: All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
- **File Ending**: Ensure all files end with a new line
- **SQL Comments**: All your SQL queries should have a comment just before (i.e. syntax above)
- **File Start Comment**: All your files should start with a comment describing the task
- **Uppercase SQL Keywords**: All SQL keywords should be in uppercase (SELECT, WHERE…)
- **README.md**: A README.md file at the root of the folder of the project is mandatory
- **File Length**: The length of your files will be tested using wc

### More Info
Comments for your SQL file:
```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

## Additional Information
- Use "container-on-demand" to run MySQL
- Credentials in the container are root/root
- How to import a SQL dump:
```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
```

## Let's Get Started!
Enjoy working on this MySQL Advanced project! Good luck! 🚀
