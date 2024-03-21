#!/usr/bin/python3

import platform
import netifaces as ni
import requests
import shutil
import os
import time
import psutil

# Function to get and display OS details
def get_os_details():
    system = platform.system()
    version = platform.version()

    if system == 'Windows':
        print(f"Windows {version}")
    elif system == 'Linux':
        print(f"Linux {version}")

# Function to get and display IP addresses and default gateway
def get_ip_addresses():
    try:
        private_ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
        public_ip = requests.get('http://ip.42.pl/raw').text
        gateway = ni.gateways()['default'][ni.AF_INET][0]

        print(f"Private IP Address: {private_ip}\n"
              f"Public IP Address: {public_ip}\n"
              f"Default Gateway: {gateway}")
    except Exception as e:
        print(f"Error: {e}")

# Function to get and display disk usage information
def get_disk_usage():
    disk_usage = shutil.disk_usage('/')
    print(f"Total Space: {disk_usage.total} bytes\n"
          f"Used Space: {disk_usage.used} bytes\n"
          f"Free Space: {disk_usage.free} bytes")

# Function to get the top directories and their sizes
def get_top_directories(base_path='.', num_directories=5):
    directories = []
    for root, dirs, files in os.walk(base_path):
        total_size = 0
        for f in files:
            fp = os.path.join(root, f)
            try:
                total_size += os.path.getsize(fp)
            except FileNotFoundError as e:
                print(f"Error accessing file {fp}: {e}")
        directories.append((root, total_size))

    top_directories = sorted(directories, key=lambda x: x[1], reverse=True)[:num_directories]
    return top_directories

# Function to display top directories and their sizes
def display_top_directories():
    top_dirs = get_top_directories()
    for dir_path, size in top_dirs:
        print(f"Directory: {dir_path}, Size: {size} bytes")

while True:
    # Clear the screen
    os.system('clear')  # For Linux/macOS
    # os.system('cls')  # For Windows

    # Display system information
    print("=" * 30)
    print("System Information")
    print("=" * 30)
    get_os_details()

    # Display network information
    print("=" * 30)
    print("Network Information")
    print("=" * 30)
    get_ip_addresses()

    # Display disk usage information
    print("=" * 30)
    print("Disk Usage Information")
    print("=" * 30)
    get_disk_usage()

    # Display top directories
    print("=" * 30)
    print("Top Directories")
    print("=" * 30)
    display_top_directories()

    # Display CPU usage
    print("=" * 30)
    print("CPU Usage")
    print("=" * 30)
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

    # Pause for 10 seconds before refreshing
    time.sleep(10)

