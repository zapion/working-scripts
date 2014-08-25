#!/usr/bin/python

import subprocess
import re
import os

p = subprocess.Popen(['adb', 'devices'], stdout=subprocess.PIPE)
res = p.communicate()[0].split('\n')
res.pop(0)

devices = []
for li in res:
    m = re.search('(\w+)', li)
    if(m is not None):
        devices.append(m.group(0))

total_crash_num = 0
for dev in devices:
    os.environ['ANDROID_SERIAL'] = dev
    crash_num = 0
    base_dir = "/data/b2g/mozilla/Crash Reports/"
    scan_cmd = ['adb', 'shell', 'ls -l']
    submit_dir = base_dir + 'submitted'
    pending_dir = base_dir + 'pending'
    p = subprocess.Popen(scan_cmd + [submit_dir], stdout=subprocess.PIPE)
    output = p.communicate()[0]
    if "No such" not in output:
        for out in output.split('\n'):
            if out.strip() != "":
                crash_num += 1
    else:
        print (output)
    q = subprocess.Popen(scan_cmd + [pending_dir], stdout=subprocess.PIPE)
    output = q.communicate()[0]
    if "No such" not in output:
        for out in output.split('\n'):
            if out.strip() != "":
                crash_num += 1
    else:
        print (output)
    print("device " + dev + " has " + str(crash_num) + " crashes.")
    total_crash_num += crash_num
print("Total crash number = " + str(total_crash_num))
