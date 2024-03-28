# A Puppet manifest that configures a server. It:
# - Updates the server
# - Installs an Nginx server
# - Configures the Nginx web server to
#	- return a page that contains the string "Hello World!" when queried at its root / with a GET request (requesting a page) using curl
#	- A redirection must be a “301 Moved Permanently”
#
package {'nginx':
    ensure   => 'present';
}

exec {'install':
    command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
    provider => shell,
}

exec {'Hello':
    command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
    provider => shell,
}

exec {'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/https://www.youtube.com/watch?v=QH2-TGUlwu4;\\n\\t}/" /etc/nginx/sites-available/default':
    provider => shell,
}

exec {'run':
    command  => 'sudo service nginx restart',
    provider => shell,
}
