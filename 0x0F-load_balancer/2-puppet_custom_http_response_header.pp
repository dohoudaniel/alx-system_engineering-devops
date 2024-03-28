# A Puppet manifest that configures a server. It:
# - Updates the server
# - Installs an Nginx server
# - Configures the Nginx web server to
#	- return a page that contains the string "Hello World!" when queried at its root / with a GET request (requesting a page) using curl
#	- A redirection must be a “301 Moved Permanently”
#
# Updating the system
exec { 'update system':
  command  => '/usr/bin/apt-get update',
}

# Installing Nginx package
package { 'nginx':
  ensure   => installed,
}

# Create an index.html file
file { '/var/www/html/index.html':
  content  => 'Hello World!',
}

# Add a redirection rule in Nginx configuration
exec { 'redirect_me':
  command  => 'sed -i "10i\	return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
}

# Add a custom HTTP header in Nginx configuration
exec { 'HTTP header':
  command  => 'sed -i "8i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell',
}

# Create a separate custom header file
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure   => present,
  content  => "add_header X-Served-By $hostname;",
  notify   => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure   => running,
  enable   => true,
  require  => [Package['nginx'], File['/etc/nginx/conf.d/custom_headers.conf']],
}
