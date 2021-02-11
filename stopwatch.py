from timeinterval import TimeInterval
import time

# A stopwatch with all the typical functions of a stopwatch
# Start and stop the stopwatch, reset it, restart it
class Stopwatch:
    def __init__(self, startOnInit=False):
        self.times = []

        # If we are starting the stopwatch, add the first time interval
        if startOnInit:
            self.times.append(TimeInterval(True))

    # Start the stopwatch if it is not running
    def start(self):
        if not self.is_running():
            # Add a running time interval to the list of time intervals
            self.times.append(TimeInterval(True))

    # Stop the stopwatch if it is currently running
    def stop(self):
        if self.is_running():
            # Stop the last time interval in the list
            self.times[-1].stop()

    # Start the stopwatch if it is stopped, or stop it if it is still running
    def start_or_stop(self):
        if self.is_running():
            self.stop()
        else:
            self.start()

    # Reset the stopwatch by clearing the list of all time intervals
    def reset(self):
        self.times = []

    # Reset the stopwatch and then start it
    def restart(self):
        self.reset()
        self.start()

    # Return the times of all time intervals added together
    def read(self):
        total = 0
        for interval in self.times:
            total += interval.read()
        return total

    # Return true if the stopwatch is running and false if it is stopped
    def is_running(self):
        # If there are time intervals in the times, the stopwatch is running if the most recent one is running
        if len(self.times) > 0:
            return self.times[-1].is_running()
        # If there are no time intervals, the stopwatch is not running
        else:
            return False


if __name__ == "__main__":
    print("Stopwatch started")
    stopwatch = Stopwatch(True)
    time.sleep(5)

    print("Stopwatch stopped")
    stopwatch.stop()
    print(f"Stopwatch time: {stopwatch.read()}")

    print("Stopwatch restarting")
    stopwatch.restart()
    time.sleep(7)

    print("Stopwatch stopped")
    stopwatch.stop()
    print(f"Stopwatch time: {stopwatch.read()}")

