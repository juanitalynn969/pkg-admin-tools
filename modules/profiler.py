#############################################
# Install profiler:
#
# 1. Move existing profiler files to /tmp
# 2. Pull in new files from github
# 3. Set directory & file permissions
#############################################
from modules.installer_utils import *

base_dir = '/home/wlanpi'
module_dir = 'profiler'
install_dir = "{}/{}".format(base_dir, module_dir)
tmp_dir = '/tmp'
backup_dir = "{}/profiler".format(tmp_dir)
github_url = "github.com/WLAN-Pi/profiler.git"
pkg_name = 'profiler'
linux_pkg_list = []

def profiler_install(branch) :

    return pkg_install(branch, pkg_name, linux_pkg_list, backup_dir, base_dir, module_dir, tmp_dir, github_url, install_dir)

##################################################################
# Rollback profiler installation:
#
# 1. Check if /tmp/profiler dir exists
# 2. clear profiler dir (/home/wlanpi/profiler)
# 3. Copy files in /tmp/profiler back to /home/wlanpi/profiler 
##################################################################
def profiler_rollback():

    return pkg_rollback(pkg_name, backup_dir, install_dir, base_dir)
