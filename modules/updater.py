from modules.installer_utils import *
#############################################
# Install updater:
#
# 1. Move existing wiperf files to /home/wlanpi/.recycle
# 2. Pull in new files from github
# 3. Set directory & file permissions
#############################################
updater_params = {
    'base_dir': '/home/wlanpi',
    'module_dir': 'pkg-admin-tools',
    'install_dir': '/home/wlanpi/pkg-admin-tools',
    'tmp_dir': '/home/wlanpi/.recycle',
    'backup_dir': "/home/wlanpi/.recycle/pkg-admin-tools",
    'github_url': "https://github.com/WLAN-Pi/pkg-admin-tools.git",
    'pkg_name': 'pkg-admin-tools',
    'linux_pkg_list': []
}

updater_post_install = {
    '[ -f /usr/local/sbin/pkg_admin ] || ln -s /home/wlanpi/pkg-admin-tools/pkg_admin.py /usr/local/sbin/pkg_admin'

}


def updater_install(branch):

    return pkg_install(branch, updater_params, updater_post_install)

def updater_rollback():

    return pkg_rollback(updater_params)
