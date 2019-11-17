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

def pull_github_files(url, branch):
    print("Pulling files from GitHub...")
    try:
        pull_output = subprocess.check_output("git clone --single-branch --branch {} https://{}".format(branch, url), shell=True)
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
        pull_output = subprocess.check_output("rm -r {}".format(dir), shell=True) 
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

def check_module_installed(mod_name):
    if mod_name in sys.modules:
        return True
    else:
        return False





