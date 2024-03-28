# A Puppet manifest that configures a server. It:
# - Updates the server
# - Installs an Nginx server
# - Configures the Nginx web server to
#	- return a page that contains the string "Hello World!" when queried at its root / with a GET request (requesting a page) using curl
#	- A redirection must be a “301 Moved Permanently”
#
# Ensure Nginx is installed and running
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}

# Create index.html file
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello, World!',
  require => Service['nginx'],
}

# Define custom HTTP response header
$hostname = $facts['networking']['hostname']

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html;

        add_header X-Served-By ${hostname};
        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
        location / {
            try_files \$uri \$uri/ =404;
        }
    }
  ",
  require => Package['nginx'],
  notify  => Service['nginx'],
}
