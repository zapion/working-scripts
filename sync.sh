#!/bin/bash
# hg working directory is gecko
# git working directory is gecko-dev
# git remote origin is editable (not mozilla)


cd gecko
hg export awsy-lib --git > /tmp/gg1
hg export awsy-task --git > /tmp/gg2
hg export awsy-package --git > /tmp/gg3

cd ../gecko-dev

git reset --hard HEAD~3

git apply /tmp/gg1
git add testing/awsy
git commit -m "awsy-lib"
git apply /tmp/gg2
git add .
git commit -m "awsy-task"
git apply /tmp/gg3
git add .
git commit -m "awsy-package"

git rebase master

git push origin awsy -f
