#!/bin/bash

SERVICE="httpd"
RESULT=`ps -a | sed -n /${SERVICE}/p`

if [ "${RESULT:-null}" = null ]; then
    echo "not running"
else
    echo "running"
fi
