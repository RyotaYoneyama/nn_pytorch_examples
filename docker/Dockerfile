FROM nvcr.io/nvidia/pytorch:22.04-py3

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

RUN useradd --create-home --home-dir /home/ubuntu  --shell /bin/bash --user-group --groups adm,sudo ubuntu && \
    echo ubuntu:ubuntu | chpasswd && \
    echo "ubuntu ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

WORKDIR /home/ubuntu
RUN mkdir -p /home/ubuntu

USER ubuntu
COPY ./requirements.txt /home/ubuntu/requirements.txt
RUN pip install --upgrade pip && pip install --upgrade setuptools && \
    pip install --no-cache-dir -r /home/ubuntu/requirements.txt 

COPY ./entrypoint.sh /home/ubuntu/entrypoint.sh
COPY ./user_control.sh /home/ubuntu/user_control.sh

RUN sudo chmod +x /home/ubuntu/*.sh
USER root
ENTRYPOINT ["/home/ubuntu/entrypoint.sh"]