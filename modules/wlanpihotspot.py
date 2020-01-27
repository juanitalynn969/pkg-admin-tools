from modules.installer_utils import *
#############################################
# Install hotspot:
#
# 1. Move existing hotspot files to /tmp
# 2. Pull in new files from github
# 3. Set directory & file permissions
#############################################
hotspot_params = {
    'base_dir': '/etc',
    'module_dir': 'wlanpihotspot',
    'install_dir': '/etc/wlanpihotspot',
    'tmp_dir': '/tmp',
    'backup_dir': '/tmp//wlanpihotspot',
    'github_url': "github.com/WLAN-Pi/wlanpihotspot.git",
    'linux_pkg_list': ['hostapd', 'ufw', 'isc-dhcp-server'],
    'pkg_name': 'hotspot'
}


def hotspot_install(branch, hotspot_params):

    return pkg_install(branch, hotspot_params)

##################################################################
# Rollback hotspot installation:
#
# 1. Check if /tmp/wlanpihotspot dir exists
# 2. clear hotspot dir (/etc/wlanpihotspot)
# 3. Copy files in /tmp/wlanpihotspot back to /etc/wlanpihotspot
##################################################################


def hotspot_rollback(hotspot_params):

    return pkg_rollback(hotspot_params)
