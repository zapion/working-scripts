#!/bin/bash

if [ "$(whoami)" != "root" ]; then
    echo "We might need to run as root permission"
fi

mkdir /mnt/mtbf_shared
echo "//mtbf-1/mtbf_shared /mnt/mtbf_shared cifs guest,file_mode=0777,dir_mode=0777" >> /etc/fstab
apt-get install smbfs
mount -t cifs //mtbf-1/mtbf_shared /mnt/mtbf_shared

ls /mnt/mtbf_shared
