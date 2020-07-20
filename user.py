from TikTokApi import TikTokApi
    
api = TikTokApi()

def getUserObject(self, username, language='en'):
    print(self.getUser(username, language)['userInfo']['user'])
