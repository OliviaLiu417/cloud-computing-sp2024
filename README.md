# cloud-computing-sp2024
Repo for CS4287 Principles of Cloud Computing

## Setup

1. Install Vagrant on your local machine
2. Clone this repository
3. Run `vagrant up` in the root directory of the repository
4. Run `vagrant ssh` to ssh into the vagrant vm
5. Configure aws cli credentials with your credentials using `aws configure` command on the vagrant vm, provide `AWS Access Key ID`, `AWS Secret Access Key`, and use `us-west-2` for `Default region name`.
6. Run `cd /vagrant` to navigate to the shared directory
7. Run your playbook with `ansible-playbook <playbook>.yml`


