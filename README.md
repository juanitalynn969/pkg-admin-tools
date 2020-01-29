# pkg-admin-tools
Package admin utility to install or rollback several WLAN Pi utilities. The current utilities supported are:

- bakebit
- hotspot
- profiler
- wconsole
- wiperf

## Install

The pkg-admin-tools utility needs to be installed on to your WLAN Pi and run via an SSH session. If you do not have the utility on your WLAN Pi, then install it using the following commands, logged in as the wlanpi user:

```
cd ~
sudo git clone https://github.com/WLAN-Pi/pkg-admin-tools.git
```

(Note: it is best to run the utility from the WLAN Pi classic mode)

Once this operation has been completed, the utility can be run as follows (this example shows the help dialog):

```
cd ~/pkg-admin-tools
sudo ./pkg_admin.py -h
```
## Package Install

The ```pkg_admin.py -i``` command is used to install a package or update an existing package. When the command is run, the existing package files are moved to a backup directory (~/.recycle) and then the package files are pulled from GitHub and placed in the correct location on the WLAN Pi. Following the pull from GitHub, a few post install actions are performed to restore a number of config files from the original package install. The installer pulls the latest set of files from the GutHub master repo of the package, unless the '-d' option is also added, which will pull the latest dev branch. 

If the WLAN Pi cannot access GitHub (e.g. no Internet connection), then the install will not proceed.

If you would like to install a specific version or branch from GitHub, use the  ```pkg_admin.py -b <branch_or_release_name>```. For example, to install release v0.06 of the wconsole package, run the following command:

```
cd ~/pkg-admin-tools
sudo ./pkg_admin.py -i wconsole -b v0.06
```

## Package Rollback

If there are issues with the install, use the following command to roll-back to the original files:

```
cd ~/pkg-admin-tools
sudo ./pkg_admin.py -i wconsole -r
```

(If there are issues with the roll-back, it is possible to manually copy the original files from the "~/.recycle/<package_name>" directory.)

## Utility Update
The pkg-admin-tools itself may be updated from time to time to fix bugs & add features. To update to the latest version, execute the following command:

```
cd ~
sudo ./pkg-admin-tools/pkg_admin.py -u
```

When the utility is next run, the new version will be run.

## Usage

```
usage: pkg_admin.py [-h] [-i module] [-r module] [-d] [-b branch_name] [-u]

Package install utility for the WLAN Pi.

optional arguments:
  -h, --help      show this help message and exit
  -i module       install module
  -r module       rollback module
  -d              install dev branch (used with -i option)
  -b branch_name  install branch specific branch/release (used with -i option)
  -u              update this utility with latest version
```

