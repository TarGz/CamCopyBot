
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from progress.spinner import Spinner
import time
import glob
import os.path
import paramiko
import sys
from pprint import pprint


class CamCopyBot():
	def __init__(self):
		version = "0.0.1"
		self.path  = "/mnt/usbstorage/DCIM/100MEDIA/"
		print("CamCopyBot : "+version)

		self.host = "192.168.0.39"                    #hard-coded
		self.port = 22
		self.transport = paramiko.Transport((host, port))
		self.password = "julienterraz"                #hard-coded
		self.username = "Ticita71$01"                #hard-coded
		self.transport.connect(username = username, password = password)

				



		# self.dbx = dropbox.Dropbox('X-ZcIun6I8QAAAAAAAUhbEdNuWv-pVIko6L2wSsx6fd_yDRSmThQ-xpofCPVBVdT')
		# self.dbx.users_get_current_account()
		# print("?")
		# pprint(self.dbx)
		# for entry in self.dbx.files_list_folder('Applications').entries:
  #  			print("entry:"+entry.name)
						# finename = os.path.basename(vid)
				# spinner = Spinner('Desrushing '+finename)
				# spinner.next()

		self.connectDropBox()
		self.checkForVideoInPath()

	def connectDropBox(_self):
		print("Conencting to DropBox")
		_self.dbx = dropbox.Dropbox('X-ZcIun6I8QAAAAAAAUhbEdNuWv-pVIko6L2wSsx6fd_yDRSmThQ-xpofCPVBVdT')
		print ("linked account: ", _self.dbx)
		pprint (_self.dbx)
		for entry in _self.dbx.files_list_folder('/Applications/CamCopyBot').entries:
  			print("entry:"+entry.name)

	def copyVideos(_self,source):

		dest = os.path.basename(source)
		print("dest:"+dest)

		#dbx.files_upload("Potential headline: Game 5 a nail-biter as Warriors inch out Cavs", '/cavs vs warriors/game 5/story.txt')

		spinner = Spinner("copying file"+source)
		# while True:
		# 	spinner.next()
			# _self.dbx.files_upload(source,'/Applications/CamCopyBot'+source)
		with open(source, "rb") as f:
			spinner.next()
			_self.dbx.files_upload(f.read(), '/Applications/CamCopyBot'+dest, mute = False)



	def checkForVideoInPath(self):	
		spinner = Spinner('Waiting camera... ')
		while True:
			self.MP4 = glob.glob(self.path+"*.MP4")
			spinner.next()
			time.sleep(1)

			if(len(self.MP4) > 0):
				
				for entry in self.MP4:
					spinner = Spinner('found file'+entry)
					spinner.next()
					self.copyVideos(entry)
				# break

				

			




watcher = CamCopyBot()
# watcher.checkForVideoInPath()




