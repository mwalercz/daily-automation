import datetime
import shlex
from time import sleep

import subprocess

start_playing_time = datetime.datetime(
    year=2017,
    month=9,
    day=6,
    hour=00,
    minute=51
)
time_to_record = 60 * 50  # in seconds
command = 'curl --output audycja.mp3 "http://193.0.98.66:8005/"'
time_to_sleep = 5


def fire_subprocess_wait_for_it_and_kill():
    args = shlex.split(command)
    process = subprocess.Popen(args)
    stop_playing_time = datetime.datetime.now() + datetime.timedelta(seconds=time_to_record)
    while True:
        now = datetime.datetime.now()
        if now >= stop_playing_time:
            print 'recording finished'
            process.terminate()
            break
        else:
            print str(now) + ' recording...'
            sleep(time_to_sleep)


def wait_and_record():
    while True:
        now = datetime.datetime.now()
        if now >= start_playing_time:
            fire_subprocess_wait_for_it_and_kill()
            break
        else:
            print str(now) + ' sleeping'
            sleep(time_to_sleep)

wait_and_record()
