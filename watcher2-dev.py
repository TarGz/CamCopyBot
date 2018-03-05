
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from progress.spinner import Spinner
import time
import glob
import os.path
import paramiko
import pysftp
import sys
from pprint import pprint
# from pushover import Client


class CamCopyBot():
	def __init__(self):
		version = "0.0.3"
		# self.path  = "/mnt/usbstorage/DCIM/100MEDIA/" # PROD
		self.path  = "/Volumes/CNTR_ROAM3/DCIM/" 	# DEV
		print("CamCopyBot : "+version)

		self.host = "192.168.0.39"
		self.port = 22
		self.failetimeout = 300;
		self.username = "julienterraz"
		self.password = "Ticita71$01"
		self.poUSER_KEY = "INuXp5HFfmWVCICoRrhLlLmCRoyvJx"
		self.poTOKEN = "aw6mfguztvs6irod2k2o8yxqpuwkjx"
		# self.po = Client(self.poUSER_KEY, api_token=self.poTOKEN)
		# _self.po.send_message("upload done for the file " , title="Upload done:",sound="bike")
		
		self.checkForVideoInPath()



	def viewBar(_self,a,b):
	    # original version
	    res = a/int(b)*100
	    sys.stdout.write('\rComplete precent: %.2f %%' % (res))
	    sys.stdout.flush()

	def tqdmWrapViewBar(_self,*args, **kwargs):
	    try:
	        from tqdm import tqdm
	    except ImportError:
	        # tqdm not installed - construct and return dummy/basic versions
	        class Foo():
	            @classmethod
	            def close(*c):
	                pass
	        return viewBar, Foo
	    else:
	        pbar = tqdm(*args, **kwargs)  # make a progressbar
	        last = [0]  # last known iteration, start at 0
	        def viewBar2(a, b):
	            pbar.total = int(b)
	            pbar.update(int(a - last[0]))  # update pbar with increment
	            last[0] = a  # update last known iteration
	        return viewBar2, pbar  # return callback, tqdmInstance





	def uploadVideo(_self,source):

		dest = os.path.basename(source)
		print("source:"+source+"\n")
		print("dest:"+dest+"\n")

		spinner = Spinner("copying file: "+source+"\n")

		

		try:
			transport = paramiko.Transport((_self.host, _self.port))
			transport.connect(username = _self.username, password = _self.password)
			sftp = paramiko.SFTPClient.from_transport(transport)
			path = '/Users/julienterraz/Documents/_TarGz/DERUSH/TODO/' + dest 
			localpath = source
			cbk, pbar = _self.tqdmWrapViewBar(ascii=True, unit='b', unit_scale=True)
			sftp.put(localpath, path,callback=cbk)
			sftp.close()
			transport.close()
			pbar.close()
			print ("upload done: "+path+"\n")

			print ("removing source : "+source+"\n")
			

			os.remove(source)

			filename, file_extension = os.path.splitext(source)
			print ("file_extension: " + file_extension + "\n")

			if(file_extension == ".MP4"):
				_self.po.send_message("upload done for the file " + dest, title="Upload done:"+dest,sound="bike")
			
		except:
			e = sys.exc_info()
			print ("unable to upload: "+source+"\n")
			print(e)
			print ("waiting: "+str(_self.failetimeout)+" seconds\n")


	def checkForVideoInPath(self):
		spinner = Spinner('Waiting camera... ')
		while True:
			self.MP4 = glob.glob(self.path+"*.*")
			spinner.next()
			time.sleep(1)

			if(len(self.MP4) > 0):
				
				for entry in self.MP4:
					print('found file'+entry+"\n")
					self.uploadVideo(entry)
				# break



watcher = CamCopyBot()
# watcher.checkForVideoInPath()




