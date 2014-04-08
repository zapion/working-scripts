#!/bin/bash

if [ "$(whoami)" != "root" ]; then
    echo "We might need to run as root permission"
fi
adb shell stop b2g
location=`adb shell ls /data/b2g/mozilla | grep default`
location="/data/b2g/mozilla/$location"
location=`echo $location | tr -d '\r\n'`
adb pull $location/prefs.js
echo "user_pref('devtools.debugger.forbid-certified-apps', false);" >> prefs.js
adb push prefs.js $location

adb shell start b2g
rm prefs.js
