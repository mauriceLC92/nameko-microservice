# Nameko Python Microservice

A utilities microservices that provides provides the following functionality:

- A function that squares each odd number in a given list of integers.
- A function that accepts a list of strings, and returns a dictionary of the strings - the key being
  the original string, and the value being a compressed version of that string Huffman (possibly
  encoding ?).
- A function that decodes a given string previously encoded.

## Installation

Please ensure that you have Docker desktop running.

### Clone this repository and change your directory to the repo's home folder

HTTPS

```
git clone https://github.com/mauriceLC92/nameko-microservice.git && cd nameko-microservice
```

SSH

```
git clone git@github.com:mauriceLC92/nameko-microservice.git && cd nameko-microservice
```

```bash
docker-compose up
```

## Usage

First, you will need to open the shell of the docker container that's running

- Use `docker ps` to get the name of the existing container
- Find the container ID associated with this image - You will see an image named `nameko-microservice_utilities`. Use the container ID for that image in the next command.
- Use the command `docker exec -it <container id> /bin/bash` to get a bash shell in the container

Now that you are in the shell of the container, we want to connect to Nameko's shell:

Run the following: `nameko shell --config config.yml`

You can now run any of the following functions:

### Square each odd number: `List[int] -> List[int]`

```
n.rpc.utilities_service.square_each_odd_number([1,2,3,4,5,6,7,8,9,0])
```

### Encode a list of strings: `List[string] -> List[string]`

```
n.rpc.utilities.encode(["hey", "hello", "python", "and", "code"])
```

### Decode a string that has already been encoded: `str -> str`

```
n.rpc.utilities.decode([1,2,3,4,5,6,7,8,9,0])
```

## My thoughts on the assessment

I found this assessment to be awesome! I have some familiarity and usage with Docker and I enjoyed that I got to use that knowledge in the test itself. I am not too familiar with Nameko or other frameworks for microservices so it was great to learn of its existence. It was also very straightforward to read the documentation to get up and running. When reading about the string compression bit, I admittedly first thought of a common interview style question that asks to compress a string such as `AAAABB` which would result in `A3B2`. Was thankful for the suggestion to use the Huffman encoding. Luckily there was a well-implemented library that made this encoding and decoding quite easy to use.

### Decisions made

Regarding the code itself, I made sure to use list comprehensions where needed so that the code was idiomatic Python. This would allow anyone reviewing and reading the code to immediately understand my intent was to generate a new list from a given list.

Use of Docker was a requirement (which is great!) and since many of Nameko's features rely on RabbitMQ, it made sense to containerize its usage as well. Else we would need to start all our containers manually for the containerized project components. This is where Docker Compose steps in and allows us to spin up and take down our services with one command.

### Pros and Cons

RabbitMQ is a tried and tested message-broker that has a very established history of production usage. Definitely a big win that something so robust is used as the foundation for the Nameko framework. It allows us to use existing documentation and leverage the years of work put into the library for us to benefit from.

Docker feels like a decently quick and easy way to product isolated environments for each project. It feels like an excellent fit for a microservice project since here are really good container orchestration tools we can use to help maintain our services. Docker's ability to encapsulate everything the application needs to run, allows us to easily take this development project and turn it into a production ready service. By leveraging Docker we can have a lot of confidence that our service will run in prouction as it did in the development environment.
