# Environment Preparation
I used Google Cloud platform for cloud platform. Cloud is not necessary, local development is also possible. However, I wanted to discover GCP as well.
I prefered pyenv for managing python version and virtual environment.

## GCP Setup
###  Create GCP Account and Project
1. Open a free personal GCP account.
2. Create a new project named mlops-zoomcamp.    

### Create and Configure VM Instance
1. Go to Compute Engine and enable the API.
2. Create a new VM instance with the following configuration:
    - Name: mlops-zoomcamp
    - Region: us-west1
    - Zone: us-west1-b
    - Machine: N2
    - Type: n2-standard-2
    - Boot Disk Image: Ubuntu 22.04 LTS
    - Firewall: Allow both HTTP and HTTPS traffic
3. Before pressing Create, configure your SSH keys.
   - Follow [this guide](https://cloud.google.com/compute/docs/connect/create-ssh-keys) to create SSH keys based on your local OS.
   - Copy your public SSH key file (.pub extension) to the clipboard. For example: cat ~/.ssh/mlops_ssh.pub
   - On GCP, go to the Security section and add your SSH keys in the "Add manually generated SSH keys" section.
4. Press the Create button and wait for your instance to be created.

#### Accessing the VM
1. To access the VM through your local terminal: `ssh -i ~/.ssh/mlops_ssh <username>@<VM_IP_ADDRESS>`
    For example: `ssh -i ~/.ssh/mlops_ssh simgek@34.71.188.44`
2. To avoid typing this command every time, you can create an SSH configuration file: `vim ~/.ssh/config`
3. Add the following configuration:
```
Host mlops-zoomcamp
    HostName 34.71.188.44
    User simgek
    IdentityFile ~/.ssh/mlops_ssh
```
4. Now, you can connect using: `ssh mlops-zoomcamp`

## Setting Up Python Environment

### Install Pyenv
1. Install Pyenv following the instructions from the [Pyenv GitHub repository.](https://github.com/pyenv/pyenv-installer)

### Configure Shell for Pyenv
1. Set up your shell environment for Pyenv as described [here](https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv).
2. Apply the changes: `source ~/.bashrc`

Note: Dependencies are required to install Python versions with Pyenv. Refer to the [Pyenv Wiki](https://github.com/pyenv/pyenv/wiki#suggested-build-environment) for more details.

### Install Specific Pyenv Version
- The command used to install that version with pyenv:
  ```
  pyenv install 3.9.12
  ```
- If you want other versions, you can look at the available list by using command:
  ```
  pyenv install --list
  ```
- Make python version used as global:
  ```
  pyenv global 3.9.12
  ```
For sanity check, type `python` and you should be entering Python 3.9.12 interface. 
Or, you can use command `pyenv which python`. To check the list of python versions you already installed, just run `pyenv versions`.

### Create Virtual Environment
- To create a virtual environment using pyenv:
  ```
  pyenv virtualenv [version] [env_name]
  ```
  For example:
  ```
  pyenv virtualenv 3.9.7 mlops-zoomcamp
  ```





