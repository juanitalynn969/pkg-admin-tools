#!/usr/bin/python3

from modules.wconsole import *
from modules.profiler import *
from modules.wlanpihotspot import *
from modules.installer_utils import *

import argparse
import requests


if not os.geteuid() == 0:
    print("\n---------------------------------------------")
    print(" You must be root to run this script")
    print(" (use 'sudo script_installer.py') - exiting")
    print("---------------------------------------------\n")
    exit()

print()
print("-" * 50)
print("Installer script started...")

# setup CLI parser
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--install", type=str, help="install module")
parser.add_argument("-r", "--roll_back", type=str, help="rollback module")
parser.add_argument("-d", "--dev", action='store_true', help="pull dev branch")

args = parser.parse_args()

branch = "master"
if args.dev:
    branch = "dev"

# hotspot

if (args.install == "hotspot"):

    if hotspot_install(branch, hotspot_params):
        print("Hotspot installed.")
    else:
        print("Hotspot install failed.")

if (args.roll_back == "hotspot"):

    if hotspot_rollback(hotspot_params):
        print("Hotspot rolled back.")
    else:
        print("Hotspot rollback failed.")

# profiler
if (args.install == "profiler"):

    if profiler_install(branch, profiler_params):
        print("Profiler installed.")
    else:
        print("Profiler install failed.")

if (args.roll_back == "profiler"):

    if profiler_rollback(profiler_params):
        print("Profiler rolled back.")
    else:
        print("Profiler rollback failed.")

# import wconsole module

if (args.install == "wconsole"):

    if wconsole_install(branch, wconsole_params):
        print("wconsole installed.")
    else:
        print("wconsole install failed.")

if (args.roll_back == "wconsole"):

    if wconsole_rollback(wconsole_params):
        print("wconsole rolled back.")
    else:
        print("wconsole rollback failed.")

# end
print("-" * 50)
