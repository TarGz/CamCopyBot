# CamCopyBot
> Automatique extract video from cam using python on a raspberry


# Raspberry SETUP

Install python 3.5

```

```shell

sudo apt-get install python3-pip
sudo pip3 install watchdog
sudo pip3 install dropbox


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


YOUTUBE
TUTO : https://developers.google.com/youtube/v3/quickstart/python
https://console.developers.google.com/apis/credentials?project=numeric-nova-183515

sudo pip3 install --upgrade google-api-python-client
sudo pip3 install --upgrade google-auth google-auth-oauthlib google-auth-httplib2



 ```


https://www.raspberrypi.org/magpi/dropbox-raspberry-pi/





## Dropbox API

https://www.dropbox.com/developers-v1/core/start/python
http://dropbox-sdk-python.readthedocs.io/en/latest/


```
https://www.dropbox.com/developers/apps/info/cl3b8z52tee5atf
App key
cl3b8z52tee5atf
App secret
3501nuov1s9p3p7
```