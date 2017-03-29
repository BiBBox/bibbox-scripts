#! /bin/bash

if ps aux | grep -v "grep" | grep "inotifywait -m /etc/apache2/sites-enabled -e delete -e create -e moved_to"
then
    echo "Listener is still running"
    PID=$(pgrep inotifywait)
    while kill $PID > /dev/null
        do
            # Wait for one second
            sleep 1
            # Increment the second counter
            ((count++))

            # Has the process been killed? If so, exit the loop.
            if ! ps -p $PID > /dev/null ; then
                break
            fi

            # Have we exceeded $WAIT_SECONDS? If so, kill the process with "kill -9"
            # and exit the loop
            if [ $count -gt $WAIT_SECONDS ]; then
                kill -9 $PID
                break
            fi
    done
    echo "Process has been killed after $count seconds."    
fi
if ps aux | grep -v "grep" | grep "inotifywait -m /etc/apache2/sites-enabled -e delete -e create -e moved_to"
then
    echo "Listener is still running"
    PID=$(pgrep inotifywait)
    while kill $PID > /dev/null
        do
            # Wait for one second
            sleep 1
            # Increment the second counter
            ((count++))

            # Has the process been killed? If so, exit the loop.
            if ! ps -p $PID > /dev/null ; then
                break
            fi

            # Have we exceeded $WAIT_SECONDS? If so, kill the process with "kill -9"
            # and exit the loop
            if [ $count -gt $WAIT_SECONDS ]; then
                kill -9 $PID
                break
            fi
    done
    echo "Process has been killed after $count seconds."    
fi

inotifywait -m /etc/apache2/sites-enabled -e delete -e create -e moved_to |
    while read path action file; do
        echo "Folder /etc/apache2/sites-enabled changed: '$action' file '$file'"
        service apache2 reload
    done
