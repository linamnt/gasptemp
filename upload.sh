#!/bin/bash
HOST='sites.utoronto.ca'
USER='gasp'
PASS='Banting2009'
TARGETFOLDER='/www-data/'
SOURCEFOLDER='/home/lina/Documents/Personal/GASP/uoftgasp/www-data/'

lftp -f "
set ftp:ssl-allow no;
open $HOST
user $USER $PASS
lcd $SOURCEFOLDER
mirror --reverse --verbose --only-newer --ignore-time $SOURCEFOLDER $TARGETFOLDER
bye
"
