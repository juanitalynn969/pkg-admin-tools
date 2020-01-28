from modules.installer_utils import *
#############################################
# Install wconsole:
#
# 1. Move existing hotspot files to /tmp
# 2. Pull in new files from github
# 3. Set directory & file permissions
#############################################
wconsole_params = {

    'base_dir': '/etc',
    'module_dir': 'wconsole',
    'install_dir': '/etc/wconsole',
    'tmp_dir': '/tmp',
    'backup_dir': "/tmp/wconsole",
    'github_url': "https://github.com/WLAN-Pi/wconsole.git",
    'pkg_name': 'wconsole',
    'linux_pkg_list': ['hostapd', 'ufw', 'isc-dhcp-server']
}

wconsole_post_install = {

}


def wconsole_install(branch):

    return pkg_install(branch, wconsole_params, wconsole_post_install)

##################################################################
# Rollback wconsole installation:
#
# 1. Check if /tmp/wconsole dir exists
# 2. clear wconsole dir (/etc/wconsole)
# 3. Copy files in /tmp/console back to /etc/wconsole
##################################################################


def wconsole_rollback():

    return pkg_rollback(wconsole_params)
