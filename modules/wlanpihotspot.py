#############################################
# Install hotspot:
#
# 1. Move existing hotspot files to /tmp
# 2. Pull in new files from github
# 3. Set directory & file permissions
#############################################
from modules.installer_utils import *

base_dir = '/etc'
module_dir = 'wlanpihotspot'
install_dir = "{}/{}".format(base_dir, module_dir)
tmp_dir = '/tmp'
backup_dir = "{}/wlanpihotspot".format(tmp_dir)
github_url = "github.com/WLAN-Pi/wlanpihotspot.git"
linux_pkg_list = ['hostapd', 'ufw', 'isc-dhcp-server']
pkg_name = 'hotspot'

def hotspot_install(branch) :

    return pkg_install(branch, pkg_name, linux_pkg_list, backup_dir, base_dir, module_dir, tmp_dir, github_url, install_dir)

##################################################################
# Rollback hotspot installation:
#
# 1. Check if /tmp/wlanpihotspot dir exists
# 2. clear hotspot dir (/etc/wlanpihotspot)
# 3. Copy files in /tmp/wlanpihotspot back to /etc/wlanpihotspot 
##################################################################
def hotspot_rollback():

    return pkg_rollback(pkg_name, backup_dir, install_dir, base_dir)