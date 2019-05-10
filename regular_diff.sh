#!/bin/bash

DB_HOST=""
DATABASE=""
USERNAME=""
PASSWORD=""


LAST=""
CURRENT=""
DIFF="xxx-diff-$(date '+%Y%m%d%H%M%S')"

mv $CURRENT $LAST

/usr/bin/mysqldump --opt --skip-extended-insert -u$USERNAME -p$PASSWORD -h $DB_HOST $DATABASE > $CURRENT

diff -u $LAST $CURRENT > $DIFF
