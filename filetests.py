import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class Watcher:
    DIRECTORY_TO_WATCH = "/Users/James/Desktop/myFolder"
    DIR_TO_CHANGE = "/Users/James/Desktop/myNewFolder"
    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):

        for filename in os.listdir(Watcher.DIRECTORY_TO_WATCH):
            src = Watcher.DIRECTORY_TO_WATCH + "/" + filename
            new_destination = Watcher.DIR_TO_CHANGE + "/" + filename
            os.rename(src, new_destination)
            

        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - {}".format(event.src_path))

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print("Received modified event - {}".format(event.src_path))

        elif event.event_type == 'moved':
            # Taken any action here when a file is moved
            print("Received moved event - {}".format(event.src_path))

if __name__ == '__main__':
    w = Watcher()
    w.run()

