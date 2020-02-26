from modules.installer_utils import *
#############################################
# Install misc-build-files:
#
# 1. Move existing misc_build_file files to /home/wlanpi/.recycle
# 2. Pull in new files from github
# 3. Set directory & file permissions
#############################################
misc_build_files_params = {

    'base_dir': '/home/wlanpi',
    'module_dir': 'misc-build-files',
    'install_dir': '/home/wlanpi/misc-build-files',
    'tmp_dir': '/home/wlanpi/.recycle',
    'backup_dir': "/home/wlanpi/.recycle/misc-build-files",
    'github_url': "https://github.com/WLAN-Pi/misc-build-files.git",
    'pkg_name': 'misc-build-files',
    'linux_pkg_list': []
}

# set ownership of files, move in to final position and removed repo dir
misc_build_files_post_install = {
    'sync; sleep 1',
    'chown -R root:root /home/wlanpi/misc-build-files',
    'sync; sleep 1',
    'cp -R /home/wlanpi/misc-build-files/etc/* /etc',
    'sync; sleep 1',
}

def misc_build_files_install(branch):

    return pkg_install(branch, misc_build_files_params, misc_build_files_post_install)

##################################################################
# Rollback misc-build-files installation:
#
# 1. Check if /home/wlanpi/.recycle/misc-build-files dir exists
# 2. clear misc-build-files dir (/etc/misc-build-files)
# 3. Copy files in /home/wlanpi/.recycle/console back to /etc/misc-build-files
# 4. Note that manual copying of files back to /etc is required
##################################################################


def misc_build_files_rollback():

    return pkg_rollback(misc_build_files_params)
