
import time

def delhi_channel_update():
    import requests
    import datetime
    
    
    theday = datetime.date.today()
    start = theday - datetime.timedelta(days=0)
    dates = [start + datetime.timedelta(days=d) for d in range(7)]
    
    print("...",theday)


print('...starting execution...')
while True:
    print('Delhi Update Started')
    delhi_channel_update()
    time.sleep(10)
