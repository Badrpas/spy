import requests
import datetime

class ResponseError(Exception):
    def __init__(self, value):
        self.value = value
        self.code = value['error_code']
    def __str__(self):
        return repr(self.value)
    
def get_response(apiname, params, timeout=10):
    # if get_response.last_call:
    #     dt = time.perf_counter() - get_response.last_call
    #     get_response.last_call = time.perf_counter()
    #     if dt < 0.34:
    #         time.sleep(0.34-dt)
    # else:
    #     get_response.last_call = time.perf_counter()

    params['v'] = 5.29
    try:
        r = requests.post('https://api.vk.com/method/'+apiname, params=params, timeout=timeout)
        if r.status_code == requests.codes.ok:
            json = r.json()
            if 'error' in json:
                # print('There is error[{}]:'.format(json['error']['error_code']), json['error']['error_msg'])
                raise ResponseError(json['error'])
            return json['response']
        else:
            print(datetime.datetime.now().strftime('%H:%M:%S'), 'FAIL code:', r.status_code)
            return
    except requests.exceptions.RequestException as e:
        print(e)

get_response.last_call = None



def get_users(users, fields='', timeout=3):
    """
    :param users:
     list of user_id's
    :param fields:
     string containing desired fields separated by comma
    :return:
    """
    users_str = ', '.join(str(user) for user in users)
    params = {
        'user_ids': users_str,
        'fields': fields,
    }

    r = get_response('users.get', params, timeout=timeout)
    # print(r)
    return r

def get_photos(owner_id, album_id='profile', rev=1):
    params = {
        'owner_id': owner_id,
        'album_id': album_id,
        'rev': rev
    }
    r = get_response('photos.get', params)
    return r

def get_likes(owner_id, item_id, type, count=1000, filter='likes', extended=0):
    params = {
        'owner_id': owner_id,
        'item_id': item_id,
        'type': type,
        'count': count,
        'filter': filter,
        'extended': extended
    }
    r = get_response('likes.getList', params)
    return r

