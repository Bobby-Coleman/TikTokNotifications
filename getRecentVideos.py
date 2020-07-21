from TikTokApi import TikTokApi
import notifications

import time


now = int(time.time()) 

api = TikTokApi()

count = 1

usernames = ['chefcuso', 'planetcarlita', 'holli_coleman']

def check_recent_video(user): 
    tiktoks = api.byUsername(user, count=count)

    recentTikTok = tiktoks[0]

    recentTikTokTime = recentTikTok['createTime']

    plusThirtyMin = recentTikTokTime + 1800

    if plusThirtyMin >= now:
        notifications.email_alert(f'New Tik Tok from {user}', 'lol', "6266167250@tmomail.net")
    elif plusThirtyMin < now:
        print(f'no recent vid for {user}')

for user in usernames:
    check_recent_video(user)

