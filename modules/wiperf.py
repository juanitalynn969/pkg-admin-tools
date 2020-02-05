from modules.installer_utils import *
#############################################
# Install wiperf:
#
# 1. Move existing wiperf files to /home/wlanpi/.recycle
# 2. Pull in new files from github
# 3. Set directory & file permissions
#############################################
wiperf_params = {
    'base_dir': '/home/wlanpi',
    'module_dir': 'wiperf',
    'install_dir': '/home/wlanpi/wiperf',
    'tmp_dir': '/home/wlanpi/.recycle',
    'backup_dir': "/home/wlanpi/.recycle/wiperf",
    'github_url': "https://github.com/wifinigel/wiperf.git",
    'pkg_name': 'wiperf',
    'linux_pkg_list': []
}

# Preserve some config files and set some exec bits in case of github issues
wiperf_post_install = {
    'cp /home/wlanpi/wiperf/conf/etc/wpa_supplicant/wpa_supplicant.conf /home/wlanpi/wiperf/conf/etc/wpa_supplicant/wpa_supplicant.conf.backup',
    'cp /home/wlanpi/.recycle/wiperf/conf/etc/wpa_supplicant/wpa_supplicant.conf /home/wlanpi/wiperf/conf/etc/wpa_supplicant/wpa_supplicant.conf',
    'cp /home/wlanpi/.recycle/wiperf/config.ini /home/wlanpi/wiperf/config.ini',
    'chmod a+x /home/wlanpi/wiperf/wi-perf.py',
    'chmod a+x /home/wlanpi/wiperf/wiperf_switcher',
    'chown -R wlanpi:wlanpi /home/wlanpi/wiperf',
    'chown wlanpi:wlanpi /home/wlanpi/wiperf/config.ini',
}


def wiperf_install(branch):

    return pkg_install(branch, wiperf_params, wiperf_post_install)

##################################################################
# Rollback wiperf installation:
#
# 1. Check if /home/wlanpi/.recycle/wiperf dir exists
# 2. clear wiperf dir (/home/wlanpi/wiperf)
# 3. Copy files in /home/wlanpi/.recycle/wiperf back to /home/wlanpi/wiperf
##################################################################


def wiperf_rollback():

    return pkg_rollback(wiperf_params)
