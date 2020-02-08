from modules.installer_utils import *
#############################################
# Install wconsole:
#
# 1. Move existing hotspot files to /home/wlanpi/.recycle
# 2. Pull in new files from github
# 3. Set directory & file permissions
#############################################
wconsole_params = {

    'base_dir': '/etc',
    'module_dir': 'wconsole',
    'install_dir': '/etc/wconsole',
    'tmp_dir': '/home/wlanpi/.recycle',
    'backup_dir': "/home/wlanpi/.recycle/wconsole",
    'github_url': "https://github.com/WLAN-Pi/wconsole.git",
    'pkg_name': 'wconsole',
    'linux_pkg_list': ['hostapd', 'ufw', 'isc-dhcp-server']
}

# take copies of files that may have been modified & use previous ver
wconsole_post_install = {
    'cp /home/wlanpi/.recycle/wconsole/conf/hostapd.conf /etc/wconsole/conf/hostapd.conf.old',
    'cp /home/wlanpi/.recycle/wconsole/conf/ser2net.conf /etc/wconsole/conf/ser2net.conf.old',
    'chmod a+x /etc/wconsole/wconsole_switcher',
}


def wconsole_install(branch):

    return pkg_install(branch, wconsole_params, wconsole_post_install)

##################################################################
# Rollback wconsole installation:
#
# 1. Check if /home/wlanpi/.recycle/wconsole dir exists
# 2. clear wconsole dir (/etc/wconsole)
# 3. Copy files in /home/wlanpi/.recycle/console back to /etc/wconsole
##################################################################


def wconsole_rollback():

    return pkg_rollback(wconsole_params)
