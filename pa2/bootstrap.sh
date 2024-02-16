#!/bin/bash

apt-get update 
apt-get install -y python
sudo apt-get install -y python3-pip
pip3 install boto boto3

# installing unzip
sudo apt install unzip

# installing aws cli (linux arm version)
curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
