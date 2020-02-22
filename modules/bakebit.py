from modules.installer_utils import *
#############################################
# Install bakebit:
#
# 1. Move existing bakebit files to /home/wlanpi/.recycle
# 2. Pull in new files from github
# 3. Set directory & file permissions
#############################################
bakebit_params = {
    'base_dir': '/home/wlanpi/NanoHatOLED',
    'module_dir': 'BakeBit',
    'install_dir': '/home/wlanpi/NanoHatOLED/BakeBit',
    'tmp_dir': '/home/wlanpi/.recycle',
    'backup_dir': "/home/wlanpi/.recycle/BakeBit",
    'github_url': "https://github.com/WLAN-Pi/BakeBit.git",
    'pkg_name': 'bakebit',
    'linux_pkg_list': []
}

bakebit_post_install = {
    'chown -R wlanpi:wlanpi /home/wlanpi/NanoHatOLED/BakeBit',
    'chmod a+x /home/wlanpi/NanoHatOLED/BakeBit/Software/Python/bakebit_nanohat_oled.py',
    'sync',
}


def bakebit_install(branch):

    return pkg_install(branch, bakebit_params, bakebit_post_install)

##################################################################
# Rollback bakebit installation:
#
# 1. Check if /home/wlanpi/.recycle/bakebit dir exists
# 2. clear bakebit dir (/home/wlanpi/bakebit)
# 3. Copy files in /home/wlanpi/.recycle/Bakebit back to /home/wlanpi/Bakebit
##################################################################


def bakebit_rollback():

    return pkg_rollback(bakebit_params)
