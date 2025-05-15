#!/bin/bash

# Update all packages
sudo yum update -y

# Install Apache web server
sudo yum install -y httpd

# Start the Apache service
sudo systemctl start httpd

# Enable Apache to start on boot
sudo systemctl enable httpd

# Add a custom message to the default web page
echo "<h1>Welcome to My Highly Available Web App - Instance 1</h1>" | sudo tee /var/www/html/index.html
