#!/usr/bin/python3

from modules.wconsole import *
from modules.profiler import *
from modules.wlanpihotspot import *
from modules.installer_utils import *
from modules.wiperf import *
from modules.updater import *

import argparse
import requests
import sys


if not os.geteuid() == 0:
    print("\n---------------------------------------------")
    print(" You must be root to run this script")
    print(" (use 'sudo script_installer.py') - exiting")
    print("---------------------------------------------\n")
    exit()


# create parser args
parser = argparse.ArgumentParser()

# check we have passed args of some type
if len(sys.argv) < 2:
    parser.print_usage()
    sys.exit(1)

# setup parse args
parser.add_argument("-i", "--install", type=str,
                    metavar=('module'), help="install module")
parser.add_argument("-r", "--roll_back", type=str,
                    metavar=('module'), help="rollback module")
parser.add_argument("-d", "--dev", action='store_true', help="pull dev branch")
parser.add_argument("-b", "--branch", type=str,
                    help="pull branch specific branch/release")
parser.add_argument("-u", "--update", action='store_true',
                    help="update this utility with latest version")

args = parser.parse_args()

print()
print("-" * 50)
print("Installer script started...")

branch = "master"
if args.dev:
    branch = "dev"
if args.branch:
    branch = args.branch

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

# end
print("-" * 50)
