FROM nvcr.io/nvidia/pytorch:22.04-py3

# Install packages without prompting the user to answer any questions
ENV DEBIAN_FRONTEND noninteractive 


# Install packages
RUN apt-get update && apt-get install -y \
locales \
lsb-release \
mesa-utils \
git \
subversion \
wget \
curl \
htop \
libssl-dev \
build-essential \
dbus-x11 \
cmake \
byobu \
gosu \
bash-completion \
sudo \
tzdata \
vim \
software-properties-common \
gdb valgrind && \
apt-get clean && rm -rf /var/lib/apt/lists/*

# Locale
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

WORKDIR /workspace

COPY ./requirements.txt /workspace/requirements.txt
RUN pip install --upgrade pip && pip install --upgrade setuptools && \
    pip install --no-cache-dir -r requirements.txt 

