#! /bin/bash
#
# scripts_installer       installation script for various WLANPi packages
#
# Written by Nigel Bowden <wifinigel@gmail.com>.
#
# History:
#
#   v0.01 - 2nd November 2019 - Initial version for hotspot package
#

set -e

NAME=installer
DESC="Installer script for WLANPI packages"
VERSION=0.01

# Check we're root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

#############################################
# Check if we can access Internet:
#
# 1. Perform curl operation on github.com
# 2. Return success if accessible
# 3. Exit script if no Internet access
#############################################
check_internet () {
  # Make sure we can get to GitHub
  website_url=https://github.com
  hr="-----------------------------------"
  echo
  echo $hr
  echo "Checking access to the Internet..."
  if curl -s --head  --request GET $website_url | grep "200 OK" > /dev/null; then 
    echo "$website_url is accessible!"
    echo $hr
    echo
    return 0
  else
    echo "Unable to reach $website_url - exiting."
    echo $hr
    echo
    exit 1
  fi
}

#############################################
# Install hotspot:
#
# 1. Move existing hotspot files to /tmp
# 2. Pull in new files from github
# 3. Set directory & file permissions
#############################################
hotspot_install () {
  echo "Installing hotspot..."
  echo
  if check_internet
  then
    cd /etc
    echo "Backing up existing files..."
    
    # if we have backup files from previous install, remove
    if [ -e /tmp/wlanpihotspot ]; then
      rm -r /tmp/wlanpihotspot
    fi

    mv ./wlanpihotspot /tmp
    echo
    echo "Pulling files from Gitgub"
    echo
    git clone https://github.com/WLAN-Pi/wlanpihotspot.git
    echo
    echo "Setting permissions on new files"
    echo
    sh /etc/wlanpihotspot/set_file_permissions.sh
    echo "Install complete."
    echo
  fi
}

##################################################################
# Rollback hotspot installation:
#
# 1. Check if /tmp/wlanpihotspot dir exists
# 2. clear hotspot dir (/etc/wlanpihotspot)
# 3. Copy files in /tmp/wlanpihotspot back to /etc/wlanpihotspot 
##################################################################
hotspot_rollback () {
  echo "Rolling back hotspot installation..."
  echo

  if [ -e /tmp/wlanpihotspot ]; then
    echo "Backup folder found...restoring"
    echo 
    rm -r /etc/wlanpihotspot
    mv /tmp/wlanpihotspot /etc
    echo "Original files restored."
    echo
    exit 0
  else
    echo "Unable to find original files in /tmp, restore not possible...sorry."
    echo
    exit 1
  fi
}

#########################
# Return version info
#########################
version () {
    N=/wlanpi/installer/installer.sh
        echo "Version: $N $VERSION" >&2
        exit 1

}

#########################
# CLI processor
#########################
case "$1" in
  hotspot_install)
        hotspot_install
        ;;
  hotspot_rollback)
        hotspot_rollback
        ;;
  version)
        version;;
  *)
        N=/wlanpi/installer/installer.sh
        echo "Unknown or missing argument"!
        echo
        echo "Usage: $N { hotspot_install | hotspot_rollback | version }" >&2
        echo
        exit 1
        ;;
esac

exit 0

