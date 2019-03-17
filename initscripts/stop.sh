#!/bin/bash
echo "Stopping BIBBOX-VM Services"
source /etc/bibbox/bibbox.cfg

# Stop Folder listener that has been restarting apache2 when new configs are added
. "$bibboxdir/$bibboxscriptfolder/initscripts/apacheServiceListenerStop.sh" >> /var/log/apacheServiceListener.log 2>&1 &
