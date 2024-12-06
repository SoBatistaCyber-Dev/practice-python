'''
    Write a Python program to locate all Python packages in the computer and lists them. 
'''

import pkg_resources

installed_packages = pkg_resources.working_set
for package in installed_packages:
    print(package)
