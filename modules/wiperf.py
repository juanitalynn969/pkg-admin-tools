from modules.installer_utils import *
#############################################
# Install wiperf:
#
# 1. Move existing wiperf files to /tmp
# 2. Pull in new files from github
# 3. Set directory & file permissions
#############################################
wiperf_params = {
    'base_dir': '/home/wlanpi',
    'module_dir': 'wiperf',
    'install_dir': '/home/wlanpi/wiperf',
    'tmp_dir': '/tmp',
    'backup_dir': "/tmp/wiperf",
    'github_url': "https://github.com/wifinigel/wiperf.git",
    'pkg_name': 'wiperf',
    'linux_pkg_list': []
}

# Preserve some config files and set some exec bits in case of github issues
wiperf_post_install = {
    'cp /home/wlanpi/wiperf/conf/etc/wpa_supplicant/wpa_supplicant.conf /home/wlanpi/wiperf/conf/etc/wpa_supplicant/wpa_supplicant.conf.backup',
    'cp /tmp/wiperf/conf/etc/wpa_supplicant/wpa_supplicant.conf /home/wlanpi/wiperf/conf/etc/wpa_supplicant/wpa_supplicant.conf',
    'cp /tmp/wiperf/config.ini /home/wlanpi/wiperf/config.ini',
    'chown -R wlanpi:wlanpi /home/wlanpi/wiperf',
    'chmod a+x /home/wlanpi/wiperf/wi-perf.py',
    'chmod a+x /home/wlanpi/wiperf/wiperf_switcher',
}


def wiperf_install(branch):

    return pkg_install(branch, wiperf_params, wiperf_post_install)

##################################################################
# Rollback wiperf installation:
#
# 1. Check if /tmp/wiperf dir exists
# 2. clear wiperf dir (/home/wlanpi/wiperf)
# 3. Copy files in /tmp/wiperf back to /home/wlanpi/wiperf
##################################################################


def wiperf_rollback():

    return pkg_rollback(wiperf_params)
