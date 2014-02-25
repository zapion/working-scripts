#!/bin/bash

adb shell stop b2g
#adb pull /data/b2g/mozilla/*.default/prefs.js
#echo "user_pref('devtools.debugger.forbid-certified-apps', false);" >> prefs.js
adb push prefs.js /data/b2g/mozilla/*.default/prefs.js

adb shell start b2g
#rm prefs.js
