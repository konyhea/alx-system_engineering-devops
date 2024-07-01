#!/usr/bin/env bash

# configuring the config file
cat <<EOL > /etc/ssh/ssh_config
Host myserver
    HostName 54.209.68.125
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
EOL 123