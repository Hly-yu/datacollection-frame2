#!/bin/sh
echo "stop phantomjs"
user=`/usr/bin/whoami`
PIDS="`ps -ef|grep phantomjs|grep ${user}|grep -v grep|awk '{print $2}'`"
for pid in $PIDS
do
kill -9 $pid
done
echo "stop finish..."
