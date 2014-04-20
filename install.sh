#!/bin/bash

sudo chmod 777 *
sudo mkdir /opt/alarm-manager
sudo cp remove.sh alarm.py gui.py script.sh alarm.jpg alarm.mp3 /opt/alarm-manager/
sudo ln -s /opt/alarm-manager/alarm.py /usr/bin/alarm
sudo ln -s /opt/alarm-manager/remove.sh /usr/bin/alarm-uninstall
