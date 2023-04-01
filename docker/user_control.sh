#!/bin/bash
USER_ID=${LOCAL_UID:-9001}
GROUP_ID=${LOCAL_GID:-9001}
echo "Starting with UID: $USER_ID, GID: $GROUP_ID "
usermod -u $USER_ID ubuntu
groupmod -g $GROUP_ID ubuntu
export USER=ubuntu
export HOME=/home/ubuntu