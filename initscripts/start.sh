#! /bin/bash

echo "Start BIBBOX-VM Services"
source /etc/bibbox/bibbox.cfg

# Start Folder listener to restart apache2 when new config added
. "$bibboxdir/$bibboxscriptfolder/initscripts/apacheServiceListener.sh" >> /var/log/apacheServiceListener.log 2>&1 &

. "$bibboxdir/$bibboxscriptfolder/initscripts/runSetupScript.sh" >> /var/log/liferaySetup.log 2>&1 &