from modules.installer_utils import *
#############################################
# Install fpms:
#
# 1. Move existing hotspot files to /home/wlanpi/.recycle
# 2. Pull in new files from github
# 3. Set directory & file permissions
#############################################
fpms_params = {

    'base_dir': '/usr/local',
    'module_dir': 'fpms',
    'install_dir': '/usr/local/fpms',
    'tmp_dir': '/home/wlanpi/.recycle',
    'backup_dir': "/home/wlanpi/.recycle/fpms",
    'github_url': "https://github.com/WLAN-Pi/fpms.git",
    'pkg_name': 'fpms',
    'linux_pkg_list': []
}

# perform any required post-install actions here
fpms_post_install = {
    'sync'
}


def fpms_install(branch):

    return pkg_install(branch, fpms_params, fpms_post_install)

##################################################################
# Rollback fpms installation:
#
# 1. Check if /home/wlanpi/.recycle/fpms dir exists
# 2. clear fpms dir (/home/wlanpi/fpms)
# 3. Copy files in /home/wlanpi/.recycle/fpms back to /home/wlanpi/fpms
##################################################################


def fpms_rollback():

    return pkg_rollback(fpms_params)
