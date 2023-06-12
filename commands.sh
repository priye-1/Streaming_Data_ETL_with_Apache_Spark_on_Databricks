#Update the installed packages and package cache on your instance
sudo yum update -y

#Install docker 
sudo yum install docker

# start docker service
sudo service docker start

# Add the ec2-user to the docker group so you can execute Docker commands without using sudo
sudo usermod -a -G docker ec2-user

# confirm docker is running
sudo service docker status


#Verify that the ec2-user can run Docker commands without sudo
docker info

# Pull the latest mongo docker container:
docker pull mongo

#Make a persistent folder for the Mongo DB server volume.
mkdir mongodb

# Open the container, map the ports
# run container and enable access to Mongo from OUTSIDE the container by exposing port of the machine. The -p option is specifically meant for this:
docker run -d -p 27017:27107 --network="host" -v ~/mongodb:/data/db --name ngmongodb mongo

# Login to container and test mongodb.
docker exec -it ngmongodb mongosh

# kill running container
docker kill <container-name>

# remove container
docker rm <container-name>




################################################ SAM  commands to deploy Lambda function using SAM ######################################################

# Install the SAM CLI -  https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html

# initialize the SAM application and follow the steps
sam init
# pick (AWS Quick Start Templates)
# pick (Hello World Example)

# build your application
sam build

# deploy your application
sam deploy --guided