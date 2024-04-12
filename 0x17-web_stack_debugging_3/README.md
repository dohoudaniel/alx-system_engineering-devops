## 0x17. Web stack debugging #3

In this project, I really enjoyed working on this project because:
- I had to start the recommended Sandbox for this project
- I checked for all installations of PHP
- I ran the following commands:
	```bash
	curl -sI 127.0.0.1
	ls
	apache2 --version
	cd /etc/apache2
	ls
	clear
	sudo apachectl configtest
	sudo apachectl -S
	clear
	ls
	cat apache2.conf 
	clear
	curl -sI 127.0.0.1
	clear
	sudo apt install tree tmux
	clear
	cd ../..
	cd ~
	clear
	tree | grep "php"
	la
	cd /
	clear
	tree | grep "php"
	ls
	cd /etc/apache2
	ls
	cat apache2.conf | grep "php"
	cat apache2.conf | grep "5"
	cd ..
	cd apache
	cd /var/log/apache2
 	ls
	cat error.log | grep "php"
	cd /etc
 	ls
	cd apache2
	ls
	cd mods-enabled/
	ls
	apachectl -S
	apachectl configtest
	ls
	cd /var/www
	ls
	cd html
	ls
	php -i
	```
<br>
This is just a walk-thourh of my debugging process, but I found out that I had to check out the WordPress installation directory for an Apache2 Web Server, the `/var/www/html` and I had to check all the `.php` files.
