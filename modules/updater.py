from modules.installer_utils import *
#############################################
# Install updater:
#
# 1. Move existing wiperf files to /tmp
# 2. Pull in new files from github
# 3. Set directory & file permissions
#############################################
updater_params = {
    'base_dir': '/home/wlanpi',
    'module_dir': 'pkg-admin-tools',
    'install_dir': '/home/wlanpi/pkg-admin-tools',
    'tmp_dir': '/tmp',
    'backup_dir': "/tmp/pkg-admin-tools",
    'github_url': "https://github.com/WLAN-Pi/pkg-admin-tools.git",
    'pkg_name': 'pkg-admin-tools',
    'linux_pkg_list': []
}


def updater_install(branch, updater_params):

    return pkg_install(branch, updater_params)
