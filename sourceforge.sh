#!/bin/bash

FILE=${1?Error: what to put}

expect -c " 
spawn sftp $SFUSER@frs.sourceforge.net
expect \"yes/no\"
send \"yes\r\"
expect \"Password\"        
send \"$SFPASS\r\"
expect \"sftp> \"
send \"cd $SFDIR\r\"
set timeout -1
send \"put $FILE\r\"
expect \"Uploading\"
expect \"100%\"
expect \"sftp>\"
interact"

rm -rf .ssh/known_hosts
