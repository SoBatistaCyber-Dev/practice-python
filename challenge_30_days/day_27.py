'''
    Write a Python program to validate an IP address.
'''
import ipaddress

def validate_IP_address(IP):
    try:
        validated_ip = ipaddress.ip_address(IP) #This will verify if the inputed IP is valid or not
        print("The IP address", validated_ip, "is valid!")
    except ValueError:
        print("The IP address", IP, "is invalid!")

IP = input("Enter the IP to validate: ")
validate_IP_address(IP)
