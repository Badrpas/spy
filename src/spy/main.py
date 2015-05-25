#!/usr/bin/python3
from vkapi import get_users, ResponseError
# try:
#     import db
# except:
#     print('DBshit')
#     pass
import db

import time
import datetime


def GetUserIds():
    user_ids = []
    with open('id.list', 'r') as f:
        for line in f:
            user_ids.append(line)
    return user_ids



def RunSpy():
    user_ids = GetUserIds() # Из файла

    db.init()
    users_online = db.get_users() #getting last user status from DB



    start = time.time()
    try:
        print(datetime.datetime.now().strftime('%H:%M:%S'), 'Getting response. ')
        response = get_users(user_ids, 'online', timeout=3)
    except ResponseError as e:
        print(e)
        return

    end = time.time()
    print(datetime.datetime.now().strftime('%H:%M:%S'), 'Response came in {0:04.2f} sec'.format(end - start) )

    now = datetime.datetime.now()
    now_fmttd = now.strftime('%Y-%m-%d %H:%M:%S')
    for user in response:
        if not user['id'] in users_online or user['online'] != users_online[user['id']]:
            users_online[user['id']] = user['online']
            # add event to database
            db.add_online_status(user['id'], user['online'], now_fmttd)

    now = datetime.datetime.now()
    sleep_value = 10
    print(now.strftime('%H:%M:%S'), 'Now waiting for {0} sec'.format(sleep_value))
    time.sleep(sleep_value)


if __name__ == '__main__':
    RunSpy()


