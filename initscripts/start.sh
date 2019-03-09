#!/bin/bash
echo "Starting BIBBOX-VM Services"
source /etc/bibbox/bibbox.cfg

# Start Folder listener that restarts apache2 when new configs are added
. "$bibboxdir/$bibboxscriptfolder/initscripts/apacheServiceListener.sh" >> /var/log/apacheServiceListener.log 2>&1 &
