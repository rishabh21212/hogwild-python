# Setting Up Development Environment on WSL-2

## 1. Install WSL-2

Follow the official guide from Microsoft to install WSL-2:

1. Open PowerShell as Administrator:
   - Right-click on the Start button and select "Windows PowerShell (Admin)".

2. Install WSL:
   - Run the following command to install WSL and set WSL-2 as the default version:
     ```powershell
     wsl --install
     ```
   This command will:
   - Enable the necessary Windows features.
   - Install the latest WSL Linux kernel.
   - Set WSL-2 as the default version.
   - Install a Linux distribution (by default, Ubuntu).
   - Restart your machine if prompted.

3. Verify Installation:
   - Open a new PowerShell window and run:
     ```powershell
     wsl --list --verbose
     ```
   Ensure the installed distribution is set to version 2.


# Installing Python 3.6.3 on WSL 2

## Step 1: Update and Upgrade
First, update and upgrade your package lists to ensure you have the latest versions.

```bash
sudo apt update
sudo apt upgrade
```
## Step 2: Install Dependencies
Python 3.6.3 may require some dependencies to be installed. Run the following command to install them:
```bash
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
```

## Step 3: Download Python 3.6.3 Source Code
Navigate to the directory where you want to download Python 3.6.3 source code (e.g., your home directory):
```bash
cd ~
wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
```

## Step 4: Extract and Compile Python
Extract the downloaded archive and compile Python from source:
```bash
tar -xzvf Python-3.6.3.tgz
cd Python-3.6.3
./configure --enable-optimizations
make -j$(nproc)
sudo make altinstall
```

## Step 5: Verify Installation
Check that Python 3.6.3 has been installed correctly:
```bash
python3.6 --version
```


## 2. Install Docker Desktop and Enable WSL-2 and Kubernetes

1. Download Docker Desktop:
   - Go to [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop) and download the installer.

2. Install Docker Desktop:
   - Run the installer and follow the prompts.

3. Enable WSL-2 Integration:
   - During the installation, ensure the option “Use the WSL 2 based engine” is selected.
   - After installation, go to Docker Desktop settings:
     - Click on the Docker icon in the system tray.
     - Navigate to Settings > General.
     - Ensure “Use the WSL 2 based engine” is checked.
     - Go to Settings > Resources > WSL INTEGRATION.
     - Enable integration with your installed WSL 2 distributions.

4. Enable Kubernetes:
   - Go to Settings > Kubernetes.
   - Check “Enable Kubernetes”.
   - Apply and restart Docker Desktop as prompted.

## 3. Install Kubernetes on WSL-2

Installing Kubernetes directly on WSL-2 can be complex, but we can manage Kubernetes clusters using kubectl in conjunction with Docker Desktop:

1. Ensure kubectl is installed:
   - Docker Desktop should install kubectl automatically. Verify by running:
     ```bash
     kubectl version --client
     ```
   If not installed, follow the instructions [here](https://kubernetes.io/docs/tasks/tools/install-kubectl/) to manually install kubectl.

## 4. Install Minikube on WSL-2

1. Install Minikube:
   - Download and install Minikube:
     ```bash
     curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
     sudo install minikube-linux-amd64 /usr/local/bin/minikube
     ```
     
Add Your User to the docker Group:

Open a terminal window on your Ubuntu system.

Run the following command to add your current user to the docker group:

```bash
sudo usermod -aG docker $USER
```

This command modifies your user account ($USER) and adds it to the docker group, which allows your user to execute Docker commands without needing to use sudo.

Activate the Group Membership:

After adding your user to the docker group, the changes will not take effect immediately in your current shell session. You need to either log out and log back in again or use the following command to activate the changes without logging out:

```bash
newgrp docker
```

This command activates the new group membership (docker group) in your current shell session.

Verify Docker Access:

To verify that you can now run Docker commands without sudo, you can check Docker's version:
```bash
docker version
```
If you see Docker's version information without any permission errors, then your user has been successfully added to the docker group.


2. Start Minikube:
   - Start Minikube with the Docker driver:
     ```bash
     minikube start --driver=docker
     ```

## 5. Install Conda for WSL-2

1. Download Miniconda:
   - Download the latest Miniconda installer for Linux from [here](https://docs.conda.io/en/latest/miniconda.html).

2. Install Miniconda:
   - Run the installer:
     ```bash
     wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
     bash Miniconda3-latest-Linux-x86_64.sh
     ```
   Follow the prompts to complete the installation.

3. Initialize Conda:
   - Initialize Conda for your shell:
     ```bash
     source ~/.bashrc
     conda init
     ```

## 6. Setup Git and GitHub on WSL-2

1. Install Git:
   - Git is likely already installed on your WSL-2 distribution. If not, install it using:
     ```bash
     sudo apt-get update
     sudo apt-get install git
     ```

2. Configure Git:
   - Set your Git username and email:
     ```bash
     git config --global user.name "Your Name"
     git config --global user.email "your.email@example.com"
     ```

3. Generate SSH Key for GitHub:
   - Check for existing SSH keys:
     ```bash
     ls -al ~/.ssh
     ```
   - If no SSH key exists, generate one:
     ```bash
     ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
     ```
   - Follow the prompts to save the SSH key without a passphrase.
   - Add the SSH key to your GitHub account:
     - Copy the SSH key to your clipboard:
       ```bash
       cat ~/.ssh/id_rsa.pub
       ```
     - Add the copied SSH key to your GitHub account's SSH keys in Settings.

4. Test GitHub SSH Connection:
   - Test if the SSH connection to GitHub is successful:
     ```bash
     ssh -T git@github.com
     ```

## 7. Run Hogwild Python Implementation

# Hogwild Python Implementation

[HOGWILD!](https://arxiv.org/abs/1106.5730)

## Configurations and setup

First step - download two files from http://www.ai.mit.edu/projects/jmlr/papers/volume5/lewis04a/lyrl2004_rcv1v2_README.htm

1. rcv1-v2.topics.qrels.gz
2. lyrl2004_vectors_train.dat.gz 
3. lyrl2004_vectors_test_pt0.dat
4. lyrl2004_vectors_test_pt1.dat
5. lyrl2004_vectors_test_pt2.dat
6. lyrl2004_vectors_test_pt3.dat

After downloading, extract both files in the /resources/rcv1 folder. If folder does not exist, make it.


To build the python environment and activate it run: 
```bash
bash bootstrap-python-env.sh
source activate hogwild-python
```

All definitions about the coordinator address, nodes addresses and parameters related with SGD execution are in the file `settings.py`. We assume that at least two workers will be started.

To generate the proto classes (definition of message between nodes and coordinator), run the following command inside the hogwild folder:
```bash
source activate hogwild-python
cd src/hogwild & python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hogwild.proto
```
If you made any change in the file `.proto`, you must generate the classes again

## Run tests
```bash
source activate hogwild-python 
py.test --color=yes -v
```

## Run
The flag `-n` represents the number of nodes, `-r` the running mode (synchronous or asynchronous) and `-w` where it is gonna run (local or cluster)
##### To run local:
```bash
bash run.sh -w synchronous -w local
```
and it will spin 4 workers in our local machine.

##### To run in the cluster:
```bash
bash run.sh -n 3 -r synchronous -w cluster
```
and it will spin 3 workers in Kubernetes cluster. Don't forget the change the variables `KUBER_LOGIN` and docker hub user / password inside the script before to run. 
