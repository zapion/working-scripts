#!/bin/bash

rm -rf /tmp/omni
adb root
adb remount
adb shell stop b2g
mkdir /tmp/omni
adb pull /system/b2g/omni.ja /tmp/omni
cd /tmp/omni
sudo chown ${USER}:${USER} omni.ja
unzip omni.ja
sed -i '781 s/skia/cairo/' defaults/pref/b2g.js
sed -i '782,786 s|^|//|' defaults/pref/b2g.js

rm omni.ja
zip -r omni.ja *

adb push omni.ja /system/b2g/

adb reboot
