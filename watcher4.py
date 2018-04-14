
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
from pushover import Client
import shutil
import sys
from termcolor import colored, cprint
import ntpath


class CamCopyBot():
	def __init__(self):
		cprint("   _____ ____  _______     ______   ____ _______  ",'magenta',attrs=['bold'])
		cprint("  / ____/ __ \|  __ \ \   / /  _ \ / __ \__   __| ",'magenta',attrs=['bold'])
		cprint(" | |   | |  | | |__) \ \_/ /| |_) | |  | | | |    ",'magenta',attrs=['bold'])
		cprint(" | |   | |  | |  ___/ \   / |  _ <| |  | | | |    ",'magenta',attrs=['bold'])
		cprint(" | |___| |__| | |      | |  | |_) | |__| | | |    ",'magenta',attrs=['bold'])
		cprint("  \_____\____/|_|      |_|  |____/ \____/  |_|    	",'magenta',attrs=['bold'])
		cprint("                                                   ",'magenta',attrs=['bold'])
		version = "0.0.3"

		if(sys.argv[1] == "debug"):
			self.camera_path  = "/Volumes/CNTR_ROAM3/DCIM/100MEDIA/" # DEV
			self.storage_path  = "/Users/julienterraz/Documents/_TarGz/DERUSH/USBSTORAGE/" # DEV
		else:
			self.camera_path  = "/mnt/usbstorage/DCIM/100MEDIA/" # PROD
			self.storage_path  = "/home/pi/CamCopyBot/RUSH/" # PROD


		print("CamCopyBot 	: " + colored(version, 'magenta'))
		print("Camera path 	: " + colored(self.camera_path, 'magenta'))
		print("Storage path 	: " + colored(self.storage_path, 'magenta'))
	

		

		self.host = "homebook.local"
		self.port = 22
		self.failetimeout = 300;
		self.username = "julienterraz"
		self.password = "Ticita71$01"
		self.poUSER_KEY = "gtwbip1rrtuduivghs14gw1s93ezee"
		self.poTOKEN = "aw6mfguztvs6irod2k2o8yxqpuwkjx"
		self.po = Client(self.poUSER_KEY, api_token=self.poTOKEN)

		try:
			self.checkForVideoInPath()
		except KeyboardInterrupt:
			print(colored("\nExiting by user request.", 'magenta'))
			sys.exit(0)



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



	def backupVideo(_self,source):

		dest = os.path.basename(source)
		print("\nCopying file :	" + colored(source, 'white',  'on_yellow'))
		try:
			filename, file_extension = os.path.splitext(source)
			shutil.move(source,_self.storage_path)

		except:
			e = sys.exc_info()
			print("unable to backup :	" + colored(source, 'white',  'on_red'))
			print(colored(e, 'white',  'on_red'))
			print("waiting:	" + colored(str(_self.failetimeout)+" seconds\n", 'magenta'))
			_self.po.send_message(e, title="unable to backup :	"+source,sound="bike")
			quit()


	def uploadVideo(_self,source):

		dest = os.path.basename(source)
		# print("source:"+source+"\n")
		# print("dest:"+dest+"\n")
		# cprint("\nuploading file: "+source,'green',attrs=['bold'])
		print("\nUploading file : " + colored(source, 'white',  'on_blue'))
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
			# print("upload done  : " + colored(path, 'white',  'on_green'))
			# print ("removing source : "+source+"\n")
			

			os.remove(source)

			# filename, file_extension = os.path.splitext(source)
			# print ("file_extension: " + file_extension + "\n")

			# if(file_extension == ".MP4"):
			_self.po.send_message("upload done: " + dest, title="Upload done:"+dest,sound="bike")
			
		except:
			e = sys.exc_info()
			print("unable to backup :	" + colored(source, 'white',  'on_red'))
			print(colored(e, 'white',  'on_red'))
			print("waiting:	" + colored(str(_self.failetimeout)+" seconds\n", 'magenta'))
			_self.po.send_message(e, title="unable to upload :	"+source,sound="bike")
			quit()


	def checkForVideoInPath(self):
		# spinner = Spinner('running... ')
		while True:
			# Preview crap
			self.camera_preview = glob.glob(self.camera_path+"*.THM")
			if(len(self.camera_preview) > 0):
				for entry in self.camera_preview:
					os.remove(entry)
			# Files to copy
			self.camera_files = glob.glob(self.camera_path+"*.MP4")
			# Files to upload
			self.storage_files = glob.glob(self.storage_path+"*.MP4")
			if(len(self.camera_files) > 0):
				if 'spinner' in locals():
					del spinner

				### PUSHOVER LIST OF FILE
				file_list = ""
				for entry in self.camera_files:
					head = os.path.basename(entry)
					file_list += head+ "\n"

				print(file_list);
				self.po.send_message(file_list, title="Backuping batch",sound="bike")

				### BACKUPING FILES
				for entry in self.camera_files:
					self.backupVideo(entry)
					
			elif(len(self.storage_files) > 0):
				if 'spinner' in locals():
					del spinner
				for entry in self.storage_files:
					self.uploadVideo(entry)
				self.po.send_message(file_list, title="Backuping done",sound="bike")
			else:
				try:
					spinner
				except NameError:
					spinner = Spinner('\nwaiting for camera ')
				spinner.next()
			time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')
watcher = CamCopyBot()
# watcher.checkForVideoInPath()




