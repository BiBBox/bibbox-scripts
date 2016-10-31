#! /bin/bash

echo "Start BIBBOX-VM Services"

# Start Folder listener to restart apache2 when new config added
. apacheServiceListener.sh &

