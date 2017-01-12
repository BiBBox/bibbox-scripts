#! /bin/bash

echo "Start BIBBOX-VM Services"
source /etc/bibbox/bibbox.cfg

# Start Folder listener to restart apache2 when new config added
. "$bibboxdir/$bibboxscriptfolder/initscripts/apacheServiceListener.sh" &

. "$bibboxdir/$bibboxscriptfolder/initscripts/runSetupScript.sh" &