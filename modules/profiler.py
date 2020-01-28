from modules.installer_utils import *
#############################################
# Install profiler:
#
# 1. Move existing profiler files to /tmp
# 2. Pull in new files from github
# 3. Set directory & file permissions
#############################################
profiler_params = {
    'base_dir': '/home/wlanpi',
    'module_dir': 'profiler',
    'install_dir': '/home/wlanpi/profiler',
    'tmp_dir': '/tmp',
    'backup_dir': "/tmp/profiler",
    'github_url': "https://github.com/WLAN-Pi/profiler.git",
    'pkg_name': 'profiler',
    'linux_pkg_list': []
}

profiler_post_install = {

}


def profiler_install(branch):

    return pkg_install(branch, profiler_params, profiler_post_install)

##################################################################
# Rollback profiler installation:
#
# 1. Check if /tmp/profiler dir exists
# 2. clear profiler dir (/home/wlanpi/profiler)
# 3. Copy files in /tmp/profiler back to /home/wlanpi/profiler
##################################################################


def profiler_rollback():

    return pkg_rollback(profiler_params)
