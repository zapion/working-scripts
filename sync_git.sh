cd git-gecko

git format-patch HEAD~3 
mv *.patch ..
cd ..
python git_to_hg.py *.patch
cd gecko
hg qpop -a
hg qdelete awsy-lib
hg qdelete awsy-package
hg qdelete awsy-task
hg import --no-commit ../*awsy-lib.patch
hg qnew awsy-lib
hg import --no-commit ../*awsy-package.patch
hg qnew awsy-package
hg import --no-commit ../*awsy-task.patch
hg qnew awsy-task
cd ..
rm *.patch
