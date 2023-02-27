import this
import time
from threading import Thread


class Methronome:
    def __init__(self):
        self.weak_beat = None
        self.bpm = 60
        self.sleep_time = 60 / self.bpm

    def high_pulse(self):
        print('1')

    def low_pulse(self):
        print('0')

    def high_pulse_with_threading(self):
        self.high_pulse()
        time.sleep(self.sleep_time)

    def low_pulse_with_thread(self):
        time_with_weak_time = self.sleep_time / (self.weak_beat + 1)
        time.sleep(time_with_weak_time)
        for x in range(0, self.weak_beat):
            self.low_pulse()
            time.sleep(time_with_weak_time)


    def start(self):
        pass

    def pulse(self):
        while True:
            if not self.weak_beat:
                t1 = Thread(target=self.high_pulse_with_threading)
                t1.start()
                t1.join(1)
            else:
                t1 = Thread(target=self.high_pulse_with_threading)
                t2 = Thread(target=self.low_pulse_with_thread)
                t1.start()
                t2.start()
                t1.join()
                t2.join()

    def set_config(self, config: dict):
        if config['bpm']:
            self.bpm = config['bpm']

        if config['weak_beat']:
            self.weak_beat = config['weak_beat']
