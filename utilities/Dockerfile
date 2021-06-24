# set base image (3.6 mentioned in the challenge document)
FROM python:3.6

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

# copy the utilities file to the working directory
COPY utilities.py .

# copy the config file to the working directory
COPY config.yml .

# command to run on container start
CMD ["nameko", "run", "--config", "config.yml", "utilities"]