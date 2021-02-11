import time

class TimeInterval:
    def __init__(self, startOnInit=False):
        self.startTime = time.time()
        self.stopTime = time.time()
        self.running = startOnInit

    # Restart only if not already running
    def start(self):
        if not self.running:
            self.restart()

    # Set the start time and start running
    def restart(self):
        self.startTime = time.time()
        self.running = True

    # If still running, set the end time and stop running
    def stop(self):
        if self.running:
            self.stopTime = time.time()
            self.running = False

    # Read the current time in the interval
    def read(self):
        # If still running, read time since start
        if self.running:
            return time.time() - self.startTime
        # If stopped, read time between end and start
        else:
            return self.stopTime - self.startTime

    def is_running(self):
        return self.running
