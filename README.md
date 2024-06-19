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

## 7. Run Hogwild Python Implementation

# Hogwild Python Implementation

[HOGWILD!](https://arxiv.org/abs/1106.5730)

## Configurations and setup
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