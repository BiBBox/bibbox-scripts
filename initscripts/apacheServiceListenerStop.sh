#! /bin/bash

# The environment variable
#   bibboxinotifywait="inotifywait -m /etc/apache2/sites-enabled -e delete -e create -e moved_to"
# is maintained in file
#   /etc/bibbox/bibbox.cfg
MYWAIT=${bibboxinotifywait}
WAIT_SECONDS=${bibboxwaitseconds}

if ps aux | grep -v "grep" | grep "$MYWAIT"
then
    echo "Listener is still running"
    PID=$(pgrep -f "${bibboxinotifywait}")
    #while echo kill $PID
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
if ps aux | grep -v "grep" | grep "$MYWAIT"
then
    echo "Listener is still running"
    PID=$(pgrep -f "${bibboxinotifywait}")
    #while echo kill $PID
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
