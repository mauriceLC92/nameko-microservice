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

### Square each odd number: `List[int] -> List[int]`

```
n.rpc.utilities.square_each_odd_number([1,2,3,4,5,6,7,8,9,0])
```

### Square each odd number: `List[int] -> List[int]`

```
n.rpc.utilities.square_each_odd_number([1,2,3,4,5,6,7,8,9,0])
```
