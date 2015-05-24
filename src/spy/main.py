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
    user_ids = GetUserIds()

    db.init()
    user_online = db.get_users() #getting last user status


    start = time.time()
    try:
        print(start, 'Getting response. ')
        response = get_users(user_ids, 'online', timeout=3)
    except ResponseError as e:
        print(e)
        return

    end = time.time()
    print('Time elapsed on response:', end - start)

    now = datetime.datetime.now()
    now_fmttd = now.strftime('%Y-%m-%d %H:%M:%S')
    for user in response:
        if not user['id'] in user_online or user['online'] != user_online[user['id']]:
            user_online[user['id']] = user['online']
            # add event to database
            db.add_online_status(user['id'], user['online'], now_fmttd)
    print(now_fmttd, ':', user_online)
    print(datetime.datetime.now().strftime('%H:%M:%S'), 'Now waiting')
    time.sleep(10)


if __name__ == '__main__':
    RunSpy()


