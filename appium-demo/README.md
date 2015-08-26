Please create virtualenv before you install any lib.
Tested environment:
mac
jdk 1.7
ant
android sdk; level 18+
nodejs
appium itself http://appium.io/slate/en/tutorial/android.html?ruby#introduction17  packaged program is easier to setup
Login gmail test account, modify corresponding mail field in test.py


We use emulator in this test

Pre-requisite:
1. Run emulator
2. Initial appium
3. Create virtualenv and activate
4. Install appium python client https://pypi.python.org/pypi/Appium-Python-Client/0.17
5. Install pytest, selenium
6. Run "py.test test.py"
