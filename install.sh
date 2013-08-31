#! /bin/bash
sudo apt-get install python-qt4
sudo chmod +x remove.sh alarm.py script.sh
sudo mkdir /opt/alarm-manager
sudo cp remove.sh alarm.py gui.py script.sh /opt/alarm-manager
sudo ln -s /opt/alarm-manager/alarm.py /usr/bin/alarm
sudo ln -s /opt/alarm-manager/remove.sh /usr/bin/alarm-uninstall
