#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static
if ! command -v nginx >/dev/null 2>&1; then
    apt-get update
    apt-get install nginx
fi

DIRS=(
    "/data"
    "/data/web_static"
    "/data/web_static/releases"
    "/data/web_static/shared"
    "/data/web_static/releases/test"
)

for Dir in "${DIRS[@]}"; do
    if [ ! -d "$Dir" ]; then
        mkdir -p "$Dir"
    fi
done

echo " <!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Test Page</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html> " >/data/web_static/releases/test/index.html

SYMLINK="/data/web_static/current"

if [ -L "$SYMLINK" ]; then
    rm "$SYMLINK"
fi

ln -s /data/web_static/releases/test/ "$SYMLINK"

chown -R ubuntu:ubuntu /data
sed -i "9i\ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default

service nginx restart
