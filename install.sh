#! /bin/bash
sudo chmod +x remove.sh alarm.py
sudo mkdir /opt/alarm-manager
sudo cp remove.sh alarm.py gui.py /opt/alarm-manager
sudo ln -s /opt/alarm-manager/alarm.py /usr/bin/alarm
sudo ln -s /opt/alarm-manager/remove.sh /usr/bin/alarm-uninstall
