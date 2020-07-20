from TikTokApi import TikTokApi

import time


now = int(time.time()) 

# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)
print(now)

api = TikTokApi()

count = 1

tiktoks = api.byUsername('zeroair_official', count=count)

# holli_coleman
# for tiktok in tiktoks:
#     print(tiktok['createTime'])
recentTikTok = tiktoks[0]

recentTikTokTime = recentTikTok['createTime']

plusThirtyMin = recentTikTokTime + 1800

if plusThirtyMin >= now:
    print('this tik tok was posted less than 30 min ago')
elif plusThirtyMin < now:
    print('this tik tok was posted more than 30 min ago')

