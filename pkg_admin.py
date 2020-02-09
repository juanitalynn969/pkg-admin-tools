#!/usr/bin/python3
# pylint: disable=line-too-long

from modules.wconsole import *
from modules.profiler import *
from modules.wlanpihotspot import *
from modules.installer_utils import *
from modules.wiperf import *
from modules.updater import *
from modules.bakebit import *

import argparse
import requests
import sys


if not os.geteuid() == 0:
    print("\n---------------------------------------------")
    print(" You must be root to run this script")
    print(" (use 'sudo script_installer.py') - exiting")
    print("---------------------------------------------\n")
    exit()

# read version file
this_version = read_file(updater_params['install_dir'] + "/version.txt")

# create parser args
parse_descr = "Package install utility for the WLAN Pi. \n"
parser = argparse.ArgumentParser(description=parse_descr)

# check we have passed args of some type
if len(sys.argv) < 2:
    parser.print_usage()
    sys.exit(1)

# setup parse args
parser.add_argument("-i", dest='install', type=str, metavar=('module'), choices=['bakebit', 'hotspot', 'profiler', 'wconsole', 'wiperf', 'pkg_admin'], help="install module")
parser.add_argument("-r", dest='roll_back', type=str, metavar=('module'), choices=['bakebit', 'hotspot', 'profiler', 'wconsole', 'wiperf', 'pkg_admin'], help="rollback module")
parser.add_argument("-d", dest='dev', action='store_true', help="install dev branch (used with -i option)")
parser.add_argument("-b", dest='branch', type=str, metavar=('branch_name'), help="install branch specific branch/release (used with -i option)")
parser.add_argument("-u", dest='update', action='store_true', help="update this utility with latest version")
parser.add_argument("-e", dest='empty_bin', action='store_true', help="empty recycle bin folder")
parser.add_argument("-v", action='version', version=this_version)

args = parser.parse_args()

print()
print("-" * 50)
print("Installer script started...")

branch = "master"
if args.dev:
    branch = "dev"
if args.branch:
    branch = args.branch

# empty recycle bin
if (args.empty_bin):
    if not empty_recycle_bin():
        exit()

# update util
if (args.update):

    if updater_install(branch):
        print("pkg-admin installed.")
    else:
        print("pkg-admin install failed.")

# hotspot
if (args.install == "hotspot"):

    if hotspot_install(branch):
        print("Hotspot installed.")
    else:
        print("Hotspot install failed.")

if (args.roll_back == "hotspot"):

    if hotspot_rollback():
        print("Hotspot rolled back.")
    else:
        print("Hotspot rollback failed.")

# profiler
if (args.install == "profiler"):

    if profiler_install(branch):
        print("Profiler installed.")
    else:
        print("Profiler install failed.")

if (args.roll_back == "profiler"):

    if profiler_rollback():
        print("Profiler rolled back.")
    else:
        print("Profiler rollback failed.")

# wconsole
if (args.install == "wconsole"):

    if wconsole_install(branch):
        print("wconsole installed.")
    else:
        print("wconsole install failed.")

if (args.roll_back == "wconsole"):

    if wconsole_rollback():
        print("wconsole rolled back.")
    else:
        print("wconsole rollback failed.")

# wiperf
if (args.install == "wiperf"):

    if wiperf_install(branch):
        print("wiperf installed.")
    else:
        print("wiperf install failed.")

if (args.roll_back == "wiperf"):

    if wiperf_rollback():
        print("wiperf rolled back.")
    else:
        print("wiperf rollback failed.")

# bakebit
if (args.install == "bakebit"):

    if bakebit_install(branch):
        print("bakebit installed.")
    else:
        print("bakebit install failed.")

if (args.roll_back == "bakebit"):

    if bakebit_rollback():
        print("bakebit rolled back.")
    else:
        print("bakebit rollback failed.")

# pkg_admin
if (args.install == "pkg_admin"):

    if updater_install(branch):
        print("pkg_admin installed.")
    else:
        print("pkg_admin install failed.")

if (args.roll_back == "pkg_admin"):

    if updater_rollback():
        print("pkg_admin rolled back.")
    else:
        print("pkg_admin rollback failed.")

# end
print("-" * 50)
