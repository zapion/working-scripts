adb shell setprop persist.radio.multisim.config dsds
adb shell setprop ro.moz.ril.numclients 2
adb shell setprop ro.moz.ril.0.network_types gsm,wcdma
adb shell setprop ro.moz.ril.1.network_types gsm
adb shell ln -s /dev/socket/rild /dev/socket/rilproxy
adb shell ln -s /dev/socket/rild1 /dev/socket/rilproxy1

## Then restart b2g
adb shell stop b2g
adb shell start b2g
