#!/bin/bash

# install virtualenv
sudo apt install  python3-venv

# setup virtualenv
python3 -m venv python
pwd=`basename $PWD`;
sed -i "s/(python)/($pwd)/" ./python/bin/activate

# add /opt/iot to python sys.path
site_packages_dir=$(/opt/iot/python/bin/python -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')
ln -svf $(readlink -f ./settings/iot.pth) $site_packages_dir


# for python_miio:
sudo apt install python3-dev

# install requirements:
./python/bin/pip install -r requirements.txt

cp settings/dreamevacuum_miot.py.pathched ./python/lib/python3.12/site-packages/miio/integrations/vacuum/dreame/dreamevacuum_miot.py

# secrets:
./get-secrets.sh

sudo cp etc/iot_supervisor.service /etc/systemd/system/
sudo sed -i "s/username/$(whoami)/" /etc/systemd/system/iot_supervisor.service 
sudo chown root:root /etc/systemd/system/iot_supervisor.service 
sudo chmod 644 /etc/systemd/system/iot_supervisor.service 
sudo systemctl daemon-reload
sudo systemctl enable iot_supervisor.service
sudo systemctl start iot_supervisor.service

mkdir log
