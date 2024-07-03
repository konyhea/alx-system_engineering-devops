# configuring the config file
file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => @("EOF"),
Host myserver
    HostName 54.209.68.125
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
EOF
}

