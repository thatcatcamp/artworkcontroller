#!/bin/bash
aplay ~/storage.wav
if ! mount | grep butts ; then
	echo "butt file system not mounted - recover"
	exit 1
fi
echo "models are mounted"
aplay ~/services
cd /butts
. venv/bin/activate
sudo python buttons.py &
python stream.py &
python randomimage.py &
python guiserver.py &
cd gui
ng serve &
aplay ~/modem.wav
echo "Waiting..."
while ! nc -z localhost 4200; do
  sleep 0.1
done
firefox -kiosk http://localhost:4200 &

