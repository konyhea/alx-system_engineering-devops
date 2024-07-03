# Define package and service for Nginx
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

# Configure Nginx site
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => @("EOF"),
server {
    listen 80;
    server_name _;

    root /var/www/html;

    location / {
        # Return "Hello World!" at the root
        return 200 'Hello World!';
    }

    location /redirect_me {
        # Redirect /redirect_me to another URL with a 301 Moved Permanently response
        return 301 https://www.example.com/;
    }
}
EOF
}

# Ensure Nginx is listening on port 80
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify => Service['nginx'],
}

