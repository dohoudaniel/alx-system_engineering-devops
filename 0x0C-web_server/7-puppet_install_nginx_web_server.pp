# Update the server and install Nginx
exec { 'update_and_install_nginx':
  command  => 'sudo apt-get update && sudo apt-get -y install nginx',
  provider => shell,
  require  => Package['nginx'], # Ensure the package is installed before running this command
}

# Configure Nginx to return "Hello World!" at its root
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Exec['update_and_install_nginx'], # Ensure Nginx is installed before configuring it
}

# Configure Nginx to perform a 301 redirect for /redirect_me
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.conf.erb'), # Use a template file for Nginx configuration
  require => File['/var/www/html/index.html'],    # Ensure index.html is created before modifying the Nginx config
  notify  => Service['nginx'],                    # Reload Nginx after configuration changes
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'], # Reload service when config changes
}

