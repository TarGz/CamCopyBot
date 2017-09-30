# CamCopyBot
> Automatique extract video from cam using python on a raspberry


# Raspberry SETUP

Install python 3.5

```

```shell

sudo apt-get install python3-pip
sudo pip3 install watchdog
# You may have to wait a long time before it start instaling, be patient.


```shell

# [https://www.htpcguides.com/properly-mount-usb-storage-raspberry-pi/](https://www.htpcguides.com/properly-mount-usb-storage-raspberry-pi/) 

# List USB
sudo blkid

# mount
sudo mount -o uid=pi,gid=pi /dev/sda1 /mnt/usbstorage

# Auto mount
# UUID="8765-4321"
# UUID=8765-4321 /mnt/usbstorage exfat nofail,uid=pi,gid=pi 0 0



 ```


https://www.raspberrypi.org/magpi/dropbox-raspberry-pi/