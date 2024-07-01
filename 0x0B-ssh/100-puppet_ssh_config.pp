#!/usr/bin/env bash

# configuring the config file
cat <<EOL > ~/.ssh/config
Host myserver
    HostName 54.224.16.225
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
EOL