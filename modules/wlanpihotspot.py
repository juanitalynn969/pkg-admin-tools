#############################################
# Install hotspot:
#
# 1. Move existing hotspot files to /tmp
# 2. Pull in new files from github
# 3. Set directory & file permissions
#############################################
from modules.installer_utils import *

base_dir = '/etc'
module_dir = 'wlanpihotspot'
install_dir = "{}/{}".format(base_dir, module_dir)
tmp_dir = '/tmp'
backup_dir = "{}/wlanpihotspot".format(tmp_dir)
github_repo = "github.com/WLAN-Pi/wlanpihotspot.git"

def hotspot_install(branch) :

    # check we can get to GitHub
    if not check_internet():
        return False

    print("Installing hotspot...")

    # check we have pre-requisite Linux modules (apt-get etc.)
    if not check_pkg_installed('hostapd'):
        return False
    
    if not check_pkg_installed('ufw'):
        return False
    
    if not check_pkg_installed('isc-dhcp-server'):
        return False

    # check we have pre-requisite python modules
    # *** N/A as this is all shell scripts ***

    # remove old backup file if exists
    print("Checking if old backup exists.")
    if file_exists(backup_dir):
        print("Old backup dir exists.")
        
        if not clear_dir(backup_dir):
            return False
    
    # change in to home dir
    print("Changing directory.")
    if not change_directory(base_dir):
        return False

    # move existing module dir to tmp dir
    if file_exists(module_dir):
        print("Backing up existing module files...")

        if not move_directory(module_dir, tmp_dir):
            return False

    # clone files from GitHub
    if not pull_github_files("github.com/WLAN-Pi/wlanpihotspot.git", branch):
        return False

    # Set file permissions
    print("Setting permissions on new files")
    try:
        script_output = subprocess.check_output("sh {}}/set_file_permissions.sh".format(install_dir), shell=True)
        print("File permissions set.")
    except:
        print("Unable to set file permissions.")
        return False

    print("Install complete.")
    return True

##################################################################
# Rollback hotspot installation:
#
# 1. Check if /tmp/wlanpihotspot dir exists
# 2. clear hotspot dir (/etc/wlanpihotspot)
# 3. Copy files in /tmp/wlanpihotspot back to /etc/wlanpihotspot 
##################################################################
def hotspot_rollback():

    print("Rolling back hotspot installation...")
    print("Checking if backup exists.")
    if file_exists(backup_dir):
        print("Backup file exists, rolling back.")
    
    print("Clearing install directory: {}".format(install_dir))

    if clear_dir(install_dir):
        print("Module directory cleared, restoring files...")
    else:
        print("Unable to clear existing module directory - failed.")
        return False

    if (move_directory(backup_dir, base_dir)):
        print("Files restored to {} OK.".format(base_dir))
    else:
        print("Unable to restore files to {}.".format(base_dir))
        return False 

    print("Rollback complete.")
    return True