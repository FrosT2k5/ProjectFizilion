#!/bin/bash

FILE=${1?Error: what to put}
TEST=${FILE:0:10}
if [ $TEST == "/Fizilion/" ]; then
    MFILE=$FILE
else
    MFILE="/Fizilion/"
    MFILE+="${FILE}"
fi
expect -c "
spawn sftp $SFUSER@frs.sourceforge.net
#expect \"yes/no\"
#send \"yes\r\"
expect \"Password:\"
send \"$SFPASS\r\"
expect \"sftp> \"
send \"cd $SFDIR\r\"
set timeout -1
send \"put $MFILE\r\"
expect \"Uploading\"
expect \"100%\"
expect \"sftp>\"
interact"

rm -rf .ssh/known_hosts
