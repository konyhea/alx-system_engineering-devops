Overview
This document provides an overview of three essential networking tools: localhost, ifconfig, and netstat. Understanding these tools is crucial for managing and troubleshooting network connections on your local machine.
Localhost
What is Localhost?
localhost is the hostname used to access your local machine's network services. It is equivalent to the IP address 127.0.0.1 (IPv4) or ::1 (IPv6).
Purpose
localhost allows you to access and test network services running on your local machine, such as web servers, databases, and other applications.
Ifconfig
What is Ifconfig?
ifconfig (short for "interface configuration") is a command-line utility used to configure and manage network interfaces on your local machine.
Purpose
ifconfig allows you to:
Display current network interface settings
Bash
ifconfig -a
Assign IP addresses and subnet masks
Bash
ifconfig <interface> <IP_address> netmask <subnet_mask>
Enable or disable network interfaces
Bash
ifconfig <interface> up/down
Set other network interface parameters
Netstat
What is Netstat?
netstat (short for "network statistics") is a command-line utility used to display active network connections, routing tables, and interface statistics.
Purpose
netstat allows you to:
Display active TCP and UDP connections
Bash
netstat -tlnp
Show listening ports and their associated programs
Bash
netstat -tlnp | grep LISTEN
Display network interface statistics and settings
Bash
netstat -an