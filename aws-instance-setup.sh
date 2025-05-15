#!/bin/bash

# Update all packages
sudo apt update -y

# Install Apache web server
sudo apt install -y apache2

# Start the Apache service
sudo systemctl start apache2



# Enable Apache to start on boot
sudo systemctl enable apache2

# Add a custom message to the default web page
echo "<h1>Welcome to My Highly Available Web App - Instance 1</h1>" | sudo tee /var/www/html/index.html

