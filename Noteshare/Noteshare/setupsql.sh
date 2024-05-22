#!/usr/bin/env bash
#Confuguration for file for installing sqlserver and setup database

#Update the package installer
sudo apt update

#Install the mysqlserver
sudo apt install mysql-server

#Start the sql server
sudo systemctl start mysql


