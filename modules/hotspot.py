#############################################
# Install hotspot:
#
# 1. Move existing hotspot files to /tmp
# 2. Pull in new files from github
# 3. Set directory & file permissions
#############################################
from modules.installer_utils import *

base_dir = '/etc'
module_dir = 'wconsole'
install_dir = "{}/{}".format(base_dir, module_dir)
tmp_dir = '/tmp'
backup_dir = "{}/wconsole".format(tmp_dir)
github_url = "https://github.com/WLAN-Pi/wconsole.git"
pkg_name = 'profiler'
linux_pkg_list = ['hostapd', 'ufw', 'isc-dhcp-server']


def profiler_install(branch):

    return pkg_install(branch, pkg_name, linux_pkg_list, backup_dir, base_dir, module_dir, tmp_dir, github_url, install_dir)

##################################################################
# Rollback profiler installation:
#
# 1. Check if /tmp/wconsole dir exists
# 2. clear profiler dir (/etc/wconsole)
# 3. Copy files in /tmp/console back to /etc/wconsole
##################################################################


def profiler_rollback():

    return pkg_rollback(pkg_name, backup_dir, install_dir, base_dir)
