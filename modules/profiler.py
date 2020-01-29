from modules.installer_utils import *
#############################################
# Install profiler:
#
# 1. Move existing profiler files to /home/wlanpi/.recycle
# 2. Pull in new files from github
# 3. Set directory & file permissions
#############################################
profiler_params = {
    'base_dir': '/home/wlanpi',
    'module_dir': 'profiler',
    'install_dir': '/home/wlanpi/profiler',
    'tmp_dir': '/home/wlanpi/.recycle',
    'backup_dir': "/home/wlanpi/.recycle/profiler",
    'github_url': "https://github.com/WLAN-Pi/profiler.git",
    'pkg_name': 'profiler',
    'linux_pkg_list': []
}

profiler_post_install = {
    'chown -R wlanpi:wlanpi /home/wlanpi/profiler',
    'chmod a+x /home/wlanpi/profiler/profiler.py',
}


def profiler_install(branch):

    return pkg_install(branch, profiler_params, profiler_post_install)

##################################################################
# Rollback profiler installation:
#
# 1. Check if /home/wlanpi/.recycle/profiler dir exists
# 2. clear profiler dir (/home/wlanpi/profiler)
# 3. Copy files in /home/wlanpi/.recycle/profiler back to /home/wlanpi/profiler
##################################################################


def profiler_rollback():

    return pkg_rollback(profiler_params)
