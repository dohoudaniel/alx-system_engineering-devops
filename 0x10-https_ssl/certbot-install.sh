#!/usr/bin/rnv bash
# This Bash script installs certbot on your machine
sudo apt install snapd
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
