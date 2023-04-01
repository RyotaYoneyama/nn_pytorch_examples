#!/bin/bash
source /home/ubuntu/user_control.sh
exec gosu ubuntu "$@"