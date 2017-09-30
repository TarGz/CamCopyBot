
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("on_modified")

class CamCopyBot():
	def __init__(self):
		version = "0.0.1"
		self.path  = "/mnt/usbstorage/"
		print("CamCopyBot : "+version)

		self.event_handler = MyHandler()
		self.observer = Observer()

	

		# Listen to new files added to the folder			
		self.observer.schedule(self.event_handler, self.path , recursive=False)
		self.observer.start()


		try:
			while True:
				time.sleep(1)
				print("sleep..")
		except KeyboardInterrupt:
			self.observer.stop()
		self.observer.join()

watcher = CamCopyBot()
