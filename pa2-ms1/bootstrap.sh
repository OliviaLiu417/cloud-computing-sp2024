#!/bin/bash

apt-get update 
apt-get install -y python
sudo apt-get install -y python3-pip

pip3 install boto boto3
