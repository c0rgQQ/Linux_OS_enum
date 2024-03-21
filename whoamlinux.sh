#!/bin/bash

# Storing variables

# linux_ver refers to Display linux version
linux_ver=$(lsb_release -a | grep Release | awk '{print $2}')

# int_ip refers to private IP address
int_ip=$(ifconfig | grep broadcast | awk '{print $2}')

# ext_ip refers to public IP address
ext_ip=$(curl -s ifconfig.io)

# deft_gwy refers to the default gateway
deft_gwy=$(route | grep default | awk '{print $2}')

# disk refers to the hard disk size (free and used)
disk=$(df -H)

# t5_dir refers to the top 5 directories and their size
t5_dir=$(df -H | head -n 6)

while true; do
	echo "Hi! Would you like to know more about your Linux operating system? [y/n]"
	read response
	
	if [ "$response" = "y" ]; then 
		while true; do
		clear
		echo "Linux OS: $linux_ver"
		echo "Private IP address: $int_ip"
		echo "Public IP address: $ext_ip"
		echo "Default gateway: $deft_gwy
		"
		echo "Hard disk usage:"
		echo "$disk
		"
		echo "Top 5 directories:"
		echo "$t5_dir
		"
		echo "CPU usage:"
		top -b -n 1 
		sleep 10
		done
	
	elif [ "$response" = "n" ]; then 
		echo "Sure thing, have a nice day!"
		break
		
	else 
		echo "Invalid response. Please try again."
	fi
	
done
