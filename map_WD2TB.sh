# Map network drive 

mkdir /home/pi/WD2TB

sudo mount -t cifs -o username=<>,password=<> //SERVER.local/WD2TB /home/pi/WD2TB
