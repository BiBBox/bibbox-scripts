#! /bin/bash

inotifywait -m /etc/apache2/sites-enabled -e delete -e create -e moved_to |
    while read path action file; do
        echo "Folder /etc/apache2/sites-enabled changed: '$action' file '$file'"
        service apache2 reload
    done