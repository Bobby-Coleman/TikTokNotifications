from TikTokApi import TikTokApi
import notifications

import time


now = int(time.time()) 

# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)
# print(now)

api = TikTokApi()

count = 1

usernames = ['chefcuso', 'charlidemelio', 'holli_coleman']
counter = 0
username = usernames[counter]

tiktoks = api.byUsername(username, count=count)

# holli_coleman
# for tiktok in tiktoks:
#     print(tiktok['createTime'])
recentTikTok = tiktoks[0]

recentTikTokTime = recentTikTok['createTime']


plusThirtyMin = recentTikTokTime + 1800

if plusThirtyMin >= now:
    # print('this tik tok was posted less than 30 min ago')
    notifications.email_alert(f'New Tik Tok from {usernames}', 'lol', "6266167250@tmomail.net")
elif plusThirtyMin < now:
    # print('this tik tok was posted more than 30 min ago')
    # notifications.email_alert('No tik tok', 'sorry', "6266167250@tmomail.net")
    pass

counter = counter + 1 
