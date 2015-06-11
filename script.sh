#!/bin/bash

hour=$1
minutes=$2
if [ $minutes -lt 10 ]
then
	minutes="0$minutes"
fi
shift
shift
message=$*

flag=1
while [ $flag != 0 ]
do
	min=`date +%M`
	hr=`date +%H`
	if [ $hr == $hour -a $min == $minutes ]
	then
		notify-send -t 5000 "ALARM       " "$message" -i /opt/alarm-manager/alarm.jpg
		mplayer /opt/alarm-manager/alarm.mp3
		flag=0
	fi
done
