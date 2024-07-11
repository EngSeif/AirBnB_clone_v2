#!/usr/bin/env bash
# A Bash script that sets up your web
# servers for the deployment of web_static
if ! [ -x "$(command -v nginx)" ]; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/{releases/test,shared}
sudo mkdir -p /data/web_static/current

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
" | sudo tee /data/web_static/releases/test/index.html >/dev/null

Target="/data/web_static/releases/test"
link="/data/web_static/current"

# If the symbolic link already exists,
# it should be deleted and recreated
# every time the script is ran.

if [ -L "$link" ]; then
    rm "$link"
fi

config_block="
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
"

ln -s "$Target" "$link"

sudo chown -R ubuntu:ubuntu /data/
sudo bash -c "cat > /etc/nginx/sites-available/web_static" <<EOF
server {
    listen 80;
    server_name _;

    $config_block

    location / {
        # Other configurations if any
    }
}
EOF
sudo ln -sf /etc/nginx/sites-available/web_static /etc/nginx/sites-enabled/
sudo service nginx restart
