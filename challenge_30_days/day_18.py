'''
    Write a Python program to get OS name, platform and release information. 
'''

import platform
import distro

class SystemInfo:
    def __init__(self):
        self.operating_system = None
        self.distro = None
        self.distro_version = None
        self.distro_codename = None
        self.system_release = None
        self.system_version = None
        self.processor = None
        self.platform = None
        self.architecture = None

    def setOperatingSystem(self, operating_system):
        self.operating_system = operating_system

    def setDistro(self, distro):
        self.distro = distro

    def setDistroVersion(self, distro_version):
        self.distro_version = distro_version

    def setDistroCodename(self, distro_codename):
        self.distro_codename = distro_codename

    def setSystemRelease(self, system_release):
        self.system_release = system_release

    def setSystemVersion(self, system_version):
        self.system_version = system_version
    
    def setProcessor(self, processor):
        self.processor = processor

    def setPlatform(self, platform):
        self.platform = platform

    def setArchitecture(self, architecture):
        self.architecture = architecture

    def print_linux_os(self):
        return (f"Operating System: {self.operating_system}\n"
                f"Distro: {self.distro}\n"
                f"Distro Version: {self.distro_version}\n"
                f"Distro Codename: {self.distro_codename}\n"
                f"System Release: {self.system_release}\n"
                f"System Version: {self.system_version}\n"
                f"Processor: {self.processor}\n"
                f"Platform: {self.platform}\n"
                f"Architecture: {self.architecture}")

    def print_other_os(self):
        return (f"Operating System: {self.operating_system}\n"
                f"System Release: {self.system_release}\n"
                f"System Version: {self.system_version}\n"
                f"Processor: {self.processor}\n"
                f"Platform: {self.platform}\n"
                f"Architecture: {self.architecture}")

    def __str__(self):
        if self.operating_system == 'Linux':
            return self.print_linux_os()
        else:
            return self.print_other_os()

def get_system_info():
    system_info = SystemInfo()
    system_info.setOperatingSystem(platform.system())
    if system_info.operating_system == 'Linux':
        system_info.setDistro(distro.name())
        system_info.setDistroVersion(distro.version())
        system_info.setDistroCodename(distro.codename())
    
    system_info.setSystemRelease(platform.release())
    system_info.setSystemVersion(platform.version())
    system_info.setProcessor(platform.processor())
    system_info.setPlatform(platform.platform())
    system_info.setArchitecture(platform.architecture()[0])
    return system_info

print(get_system_info())