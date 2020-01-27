#!/usr/bin/python3

import argparse
import logging
import logging.handlers as handlers
import requests

from modules.installer_utils import *

if not os.geteuid()==0:
    print("\n---------------------------------------------")
    print(" You must be root to run this script")
    print(" (use 'sudo script_installer.py') - exiting")
    print(  "---------------------------------------------\n")
    exit()

'''
# set up logging
log_file = '/tmp/scripts_installer.log'
logger = logging.getLogger('Pkg-Admin')
logger.setLevel(logging.INFO)
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

logHandler = handlers.RotatingFileHandler(log_file, maxBytes=500000, backupCount=2)
logHandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
'''

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

# import hotpot module 
from modules.wlanpihotspot import *

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

# import profiler module
from modules.profiler import *

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

print("-" * 50)

