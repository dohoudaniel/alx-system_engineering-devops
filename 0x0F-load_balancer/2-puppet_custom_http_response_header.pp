# A Puppet manifest that configures a server. It:
# - Updates the server
# - Installs an Nginx server
# - Configures the Nginx web server to
#	- return a page that contains the string "Hello World!" when queried at its root / with a GET request (requesting a page) using curl
#	- A redirection must be a “301 Moved Permanently”
#
exec {'update':
  command => 'sudo apt-get update ; sudo apt-get -y upgrade',
}

package {'nginx':
  ensure => 'present',
}

file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}

exec {'run':
  command => 'sudo service nginx restart',
}
