# 0x02-redis_basic  Redis Basic

## Overview
This project, titled "Redis Basic," focuses on learning and using Redis for basic operations. Redis is an open-source, in-memory data structure store that can be used as a database, cache, and message broker.

### Project Details
- **Project Number**: 0x02
- **Topic**: Redis Basic
- **Category**: Back-end
- **Language**: Redis
- **Weight**: 1
- **Start Date**: March 27, 2024, 6:00 AM
- **Deadline**: March 30, 2024, 6:00 AM
- **Auto Review**: Will be launched at the deadline

### Resources
To effectively learn and use Redis, you can refer to the following resources:
- [Redis Crash Course Tutorial](#)
- [Redis commands](#)
- [Redis python client](#)
- [How to Use Redis With Python](#)

### Learning Objectives
By the end of this project, you will:
- Learn how to use Redis for basic operations
- Understand how to use Redis as a simple cache

## Requirements
To successfully complete this project, ensure the following requirements are met:
- Environment: All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python3 (version 3.7)
- File Ending: Ensure all files end with a new line
- README.md: A README.md file at the root of the folder of the project is mandatory
- First Line: The first line of all your files should be exactly `#!/usr/bin/env python3`
- Coding Style: Your code should use the pycodestyle style (version 2.5)
- Documentation: All modules, classes, functions, and methods should be documented with descriptive sentences
- Type Annotations: All functions and coroutines must be type-annotated

### Installation
To install Redis on Ubuntu 18.04, follow these steps:
```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

### Using Redis in a Container
When using Redis in a container, ensure the following:
- Redis server is stopped by default
- Start the Redis server when starting a container with: `service redis-server start`

## Let's Get Started!
Enjoy learning and using Redis for basic operations! 🚀

Author: Gray
## Contributing

Contributions are welcome! Please follow the guidelines.

## License

This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.
