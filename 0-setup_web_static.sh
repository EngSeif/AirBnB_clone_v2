#!/bin/bash
# Install nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/

# Create a fake HTML file for testing
echo "<html>
  <head>
    <title>Test Page</title>
  </head>
  <body>
    <p>This is a test page.</p>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate symbolic link
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Set ownership of the /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content and restart Nginx
config_content=$(
    cat <<EOF
server {
    listen 80;
    listen [::]:80;
    server_name _;
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
}
EOF
)

# Remove default symlink if exists
sudo rm -rf /etc/nginx/sites-enabled/default

# Write new config to a temporary file
sudo bash -c "echo '$config_content' > /etc/nginx/sites-available/web_static"
# Create a symlink to sites-enabled
sudo ln -sf /etc/nginx/sites-available/web_static /etc/nginx/sites-enabled/web_static

# Restart nginx
sudo service nginx restart

exit 0
