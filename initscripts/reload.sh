#! /bin/sh

echo "reload.sh"

# ps aux | grep "sites-enabled"
#root        1222  0.0  0.0   6508   900 ?        S    Mar23   0:00 inotifywait -m /etc/apache2/sites-enabled -e delete -e create -e moved_to
#root        8576  0.0  0.0   6508    84 ?        S    Mar23   0:00 inotifywait -m /etc/apache2/sites-enabled -e delete -e create -e moved_to
# Stop watcher, start watcher
