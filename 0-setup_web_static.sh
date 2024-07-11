#!/usr/bin/env bash
# A Bash script that sets up your web
# servers for the deployment of web_static
if ! [ -x "$(command -v nginx)" ]; then
    apt-get update
    apt-get install -y nginx
fi

mkdir -p /data/web_static/{releases/test,shared}
mkdir -p /data/web_static/current

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
" | tee /data/web_static/releases/test/index.html >/dev/null

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

chown -R ubuntu:ubuntu /data/
bash -c "cat > /etc/nginx/sites-available/web_static" <<EOF
server {
    listen 80;
    server_name _;

    $config_block

    location / {
        # Other configurations if any
    }
}
EOF
ln -sf /etc/nginx/sites-available/web_static /etc/nginx/sites-enabled/
service nginx restart
