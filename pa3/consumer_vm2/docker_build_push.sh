# script to build and push the vm2 consumer docker image to docker hub
docker build -t consumer-vm2 .
docker tag consumer-vm2 dushims/consumer-vm2
docker push dushims/consumer-vm2
