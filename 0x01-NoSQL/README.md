# NoSQL Project

## Overview

This project focuses on understanding NoSQL databases, particularly MongoDB, and implementing related tasks using Python.

## Project Details

- **Topic:** NoSQL and MongoDB
- **Category:** Back-end
- **Weight:** 1
- **Start Date:** Mar 25, 2024 6:00 AM
- **End Date:** Mar 27, 2024 6:00 AM
- **Checker Release:** Mar 25, 2024 6:00 PM
- **Auto Review:** Will be launched at the deadline

## Resources

Read or watch:
- [NoSQL Databases Explained](https://example.com/nosql-explained)
- [What is NoSQL?](https://example.com/what-is-nosql)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://example.com/mongodb-python-crash-course)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://example.com/mongodb-tutorial2)
- [Aggregation](https://example.com/aggregation)
- [Introduction to MongoDB and Python](https://example.com/intro-mongodb-python)
- [mongo Shell Methods](https://example.com/mongo-shell-methods)
- [Mongosh](https://example.com/mongosh)

## Learning Objectives

By the end of this project, you should be able to explain to anyone, without the help of Google:
- Understand what NoSQL means
- Differentiate between SQL and NoSQL
- Define ACID
- Understand document storage
- Identify types of NoSQL databases
- Enumerate benefits of a NoSQL database
- Query information from a NoSQL database
- Perform insert/update/delete operations in a NoSQL database
- Utilize MongoDB effectively

## Requirements

### MongoDB Command File
- All files interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- Files should end with a new line
- First line of all files should be a comment: `// my comment`
- Mandatory README.md file at the root of the project folder
- File lengths will be tested using `wc`

### Python Scripts
- All files interpreted/compiled on Ubuntu 18.04 LTS using Python3 (version 3.7) and PyMongo (version 3.10)
- Files should end with a new line
- First line of all files should be `#!/usr/bin/env python3`
- Mandatory README.md file at the root of the project folder
- Code should adhere to PEP 8 style (pycodestyle version 2.5.*)
- File lengths will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Code should not be executed when imported (`if __name__ == "__main__":`)

## Installation Guide

Follow these steps to install MongoDB 4.2 in Ubuntu 18.04:
- Add MongoDB repository key: `$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -`
- Add MongoDB repository: `$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list`
- Update package list: `$ sudo apt-get update`
- Install MongoDB: `$ sudo apt-get install -y mongodb-org`
- Check MongoDB status: `$ sudo service mongod status`
- Verify MongoDB version: `$ mongo --version`
- Install PyMongo: `$ pip3 install pymongo`

If encountering issues like "Data directory /data/db not found," create the directory: `$ sudo mkdir -p /data/db`

## Usage

To start MongoDB in a container:
- Use "container-on-demand" to run MongoDB
- Ask for a container with Ubuntu 18.04 and MongoDB
- Connect via SSH or WebTerminal
- Start MongoDB: `$ service mongod start`

## Additional Notes

- Ensure MongoDB is running before interacting with it.
- Use provided resources for learning and reference throughout the project.
