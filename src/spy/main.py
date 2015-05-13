#!/usr/bin/python3
from vkapi import get_users
try:
    import db
except:
    print('DBshit')
    pass

import datetime

def GetUserIds():
    user_ids = []
    with open('id.list', 'r') as f:
        for line in f:
            user_ids.append(line)
    return user_ids



def RunSpy():
    user_ids = GetUserIds()
    user_online = {}


    response = get_users(user_ids, 'online')

    now = datetime.datetime.now()
    now_fmttd = now.strftime('%Y-%m-%d %H:%M:%S')
    for user in response:
        if not user['id'] in user_online or user['online'] != user_online[user['id']]:
            user_online[user['id']] = user['online']
            print(now_fmttd)
            # add event to database
            db.add_online_status(user['id'], user['online'], now_fmttd)


    print(user_online)


if __name__ == '__main__':
    RunSpy()


