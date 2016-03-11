import os
from obspy.core import UTCDateTime, read

from msnoise.api import connect, is_next_job, get_next_job, \
    get_data_availability, get_config, update_job

def main():
    db = connect()
    while is_next_job(db, jobtype='AMAZ1'):
        jobs = get_next_job(db, jobtype='AMAZ1')
        for job in jobs:
            net, sta = job.pair.split('.')
            gd = UTCDateTime(job.day).datetime
            print("Processing %s.%s for day %s"%(net,sta, job.day))
            files = get_data_availability(
                    db, net=net, sta=sta, starttime=gd, endtime=gd,
                    comp="Z")
            for file in files:
                fn = os.path.join(file.path, file.file)
                st = read(fn, starttime=UTCDateTime(job.day), endtime=UTCDateTime(job.day)+86400)
                print st