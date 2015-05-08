#!/bin/bash
if [ -z M_PATH ]
then
    echo "No marionette path specified"
    exit 1
fi

rm -rf /tmp/omni
adb root
adb remount
adb shell stop b2g
mkdir /tmp/omni
adb pull /system/b2g/omni.ja /tmp/omni
cd /tmp/omni
chown ${USER}:${USER} omni.ja
unzip omni.ja
cp -f $M_PATH/marionette-*.js chrome/marionette/content/


rm omni.ja
zip -r omni.ja *

adb push omni.ja /system/b2g/

adb reboot
