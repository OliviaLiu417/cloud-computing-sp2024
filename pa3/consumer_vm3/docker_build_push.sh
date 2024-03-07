# script to build and push the vm3 consumer docker image to docker hub
docker build -t consumer-vm3 .
docker tag consumer-vm3 dushims/consumer-vm3
docker push dushims/consumer-vm3