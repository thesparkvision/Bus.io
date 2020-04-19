import pyttsx3 
engine = pyttsx3.init()  
def get_drive_time(apiKey, origin, destination):
    """
    Returns the driving time between using the Google Maps Distance Matrix API. 
    API: https://developers.google.com/maps/documentation/distance-matrix/start


    # INPUT -------------------------------------------------------------------
    apiKey                  [str]
    origin                  [str]
    destination             [str]

    # RETURN ------------------------------------------------------------------
    drive_tim               [float] (minutes)
    """
    import requests
    url = ('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={}&destinations={}&key={}'
           .format(origin.replace(' ','+'),
                   destination.replace(' ','+'),
                   apiKey
                  )
          )
    try:
        response = requests.get(url)
        resp_json_payload = response.json()
        drive_time = resp_json_payload['rows'][0]['elements'][0]['duration']['value']/60
    except:
        print('ERROR: {}, {}'.format(origin, destination))
        drive_time = 0
    return drive_time


def short_dist(ori,des):
    # get key
    fname = 'Key.txt'
    file  = open(fname, 'r')
    apiKey = file.read()

    # get coordinates 
    origin = ori
    destination = des
    drive_time = get_drive_time(apiKey, origin, destination)
    ori="The distance from" ,origin ,"to ", " is ",destination
    if drive_time == 1:
        des = "you can go by magic"
    elif drive_time > 1:
        des = " you should take lift "
    engine.say(ori)
    engine.say(des)
    engine.runAndWait() 

    #print('Origin:      {}\nDestination: {}\nDrive Time:  {} hr'.format(origin, destination, drive_time/60))
    return str(drive_time/60)
