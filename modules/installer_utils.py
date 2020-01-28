import os.path
import os
import subprocess
import shutil
import requests
import sys


def dialog(msg):
    print("-" + msg)


def check_internet(url="https://github.com"):

    print("Checking Internet connection...")

    try:
        request = requests.get(url)
        if request.status_code == 200:
            print("Able to access GitHub OK.")
            return True
    except Exception as ex:
        print("Unable to access GitHub: {}".format(ex))
        return False


def file_exists(filename):
    try:
        if os.path.exists(filename):
            return True
    except Exception as ex:
        print("Error: {}".format(ex))
        return False


def delete_file(filename):

    try:
        os.remove(filename)
        return True
    except Exception as ex:
        print("Error: {}".format(ex))
        return False


def read_file(file_name):

    try:
        with open(file_name, 'r') as fh:
            contents = fh.read()
        return contents
    except Exception as ex:
        print("Issue reading file: {}".format(ex))
        return False


def pull_github_files(url, branch):
    print("Pulling files from GitHub...")
    try:
        pull_output = subprocess.check_output(
            "git clone --single-branch --branch {} {}".format(branch, url), shell=True)
        print("Files pulled OK.")
        return True
    except Exception as ex:
        print("Unable to pull files.")
        print("Error: {}".format(ex))
        return False


def change_directory(dir):
    print("Changing directory to : {}".format(dir))
    try:
        os.chdir(dir)
        print("Changed directory to : {}".format(dir))
        return True
    except Exception as ex:
        print("Unable to change in to directory to pull GitHub files: {}".format(dir))
        print("Error: {}".format(ex))
        return False


def move_directory(src, dst):
    try:
        shutil.move(src, dst)
        print("Files moved to {} OK.".format(dst))
        return True
    except Exception as ex:
        print("Unable to move files to {}".format(dst))
        print("Error: {}".format(ex))
        return False


def clear_dir(dir):
    try:
        pull_output = subprocess.check_output(
            "rm -r {}".format(dir), shell=True)
        print("Directory removed.")
        return True
    except Exception as ex:
        print("Unable to remove directory.")
        print("Error: {}".format(ex))
        return False


def check_pkg_installed(pkg_name):
    print("Checking {} package present on system...".format(pkg_name))
    if subprocess.check_output("/usr/bin/dpkg -s {}  &> /dev/null".format(pkg_name), shell=True):
        print("{} package is present on system.".format(pkg_name))
        return True
    else:
        print("Error: Package {} not installed, please install".format(pkg_name))
        return False


def check_pkgs_installed(pkg_list):
    for pkg in pkg_list:
        if not check_pkg_installed(pkg):
            return False
    # all pkgs must be installed OK
    return True


def check_module_installed(mod_name):
    if mod_name in sys.modules:
        return True
    else:
        return False


def pkg_install(branch, params, post_install):

    pkg_name = params['pkg_name']
    linux_pkg_list = params['linux_pkg_list']
    backup_dir = params['backup_dir']
    base_dir = params['base_dir']
    module_dir = params['module_dir']
    tmp_dir = params['tmp_dir']
    github_url = params['github_url']
    install_dir = params['install_dir']

    version_file = "{}/version.txt".format(install_dir)

    # check we can get to GitHub
    if not check_internet():
        return False

    print("Installing {}...".format(pkg_name))
    print("Current ver: {}".format(read_file(version_file)))

    # check we have pre-requisite Linux modules (apt-get etc.)
    if not check_pkgs_installed(linux_pkg_list):
        return False

    # check we have pre-requisite python modules
    # TBA

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
    if not pull_github_files(github_url, branch):
        return False

    # Run post-install actions
    print("Running post install actions...")
    for action in post_install:
        try:
            action_output = subprocess.check_output(action, shell=True)
        except:
            print("Issue with post-install action.")

    # Read release notes if vailable and print to screen
    rel_notes_file = '{}/release_notes.txt'.format(install_dir)
    if file_exists(rel_notes_file):
        print(read_file(rel_notes_file))

    print("Ver: {}".format(read_file(version_file)))
    print("Install complete.")
    return True


def pkg_rollback(params):

    backup_dir = params['backup_dir']
    base_dir = params['base_dir']
    install_dir = params['install_dir']
    pkg_name = params['pkg_name']

    print("Rolling back {} installation...".format(pkg_name))
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
