#!/usr/bin/env bash
# checks if nginx is installed
if [ ! -x "$(command -v nginx)" ]; then
          sudo apt-get update
            sudo apt-get install nginx -y
fi
sudo mkdir -p /data/web_static/releases/test        
sudo touch /data/web_static/releases/test/index.html
sudo mkdir -p /data/web_static/shared

echo "\
  <html>
    <body>
      <h1>Wale</h1>
    </body>
  </html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server;/a\
        location /hbnb_static/{\
            alias /data/web_static/current/;\
                }' /etc/nginx/sites-available/default;

sudo service nginx restart