#!/usr/bin/env bash
# A Bash script that sets up your web
# servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get install nginx -y

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html

echo "
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Test Page</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
" >/data/web_static/releases/test/index.html

Target="/data/web_static/releases/test/"
link="/data/web_static/current"

# If the symbolic link already exists,
# it should be deleted and recreated
# every time the script is ran.

if [ -L "$link" ]; then
    sudo rm "$link"
fi

sudo ln -sf "$Target" "$link"

sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/server {/a \
    location /hbnb_static {\n        alias /data/web_static/current/;\n        autoindex off;\n    }' /etc/nginx/sites-available/default
sudo service nginx restart
