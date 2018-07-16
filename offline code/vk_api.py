import requests
from tqdm import tqdm

HOST = 'https://api.vk.com/method/'
VERSION = '5.74'
access_token = 'f5b07d14abab4882b695f63557b2a8fb8d6f05c273481ea118e54b923ae07a365c5902b0e54a8f13b5cf3'


popushennost_list = [57846937,51812607,128033123,97753059,860937,30602036]

class User:
    """User class using VK API"""

    def __init__(self, user_id):
        self.id = user_id
        self.object = requests.get(HOST + 'users.get', params={'user_ids': self.id, 'fields': 'sex,bdate', 'access_token': access_token, 'v': VERSION}).json()["response"][0]
        self.first_name = self.object['first_name']
        self.last_name = self.object['last_name']
        self.sex = self.get_user_sex()
        self.birthday = self.object['bdate'] if 'bdate' in self.object else "и умер (не указал дату рождения)"
        self.friends = self.get_user_friends()['items']
        self.groups = self.get_user_subscriptions()['groups']['items']
        self.wall_count = requests.get(HOST + 'wall.get', params={'owner_id': self.id, 'count': 100,  'access_token': access_token, 'v': VERSION}).json()["response"]["count"]

    def get_user_sex(self):
        sex_number = self.object['sex']
        if sex_number == 1:
            return 'женский'
        elif sex_number == 2:
            return 'мужской'
        else:
            return 'гендерфлюидный'


    def get_user_friends(self):
        return requests.get(HOST + 'friends.get', params={'user_id': self.id, 'access_token': access_token, 'v': VERSION}).json()["response"]

    def get_user_subscriptions(self):
        return requests.get(HOST + 'users.getSubscriptions', params={'user_id': self.id, 'access_token': access_token, 'v': VERSION}).json()["response"]

    def isOnline(self):
        if requests.get(HOST + 'users.get', params={'user_id': self.id, 'fields': 'online', 'access_token': access_token, 'v': VERSION}).json()["response"][0]['online'] == 1:
            return True;
        return False

    def get_wall_stats(self):
        likes = 0
        reposts = 0
        views = 0
        copypasted = 0
        posts_analyzed = 0
        print()
        for shift in tqdm(range(self.wall_count // 100 + 1), desc="scanning posts"):
            posts_100 = requests.get(HOST + 'wall.get', params={'owner_id': self.id, 'count': 100, 'offset': shift*100,  'access_token': access_token, 'v': VERSION}).json()["response"]['items']
            for post in posts_100:
                posts_analyzed += 1
                likes += post['likes']['count']
                reposts += post['reposts']['count']
                if 'views' in post:
                    views += post['views']['count']
                if 'copy_history' in post:
                    copypasted += 1
        return {"likes": likes, "reposts": reposts, "views": views, "copypasted": copypasted}

    def popushennost_test(self):
        groups = []
        for zashkvar in popushennost_list:
            if zashkvar in user.groups:
                groups.append(zashkvar)

        if groups:
            print("О нет! Пользователь попущен")
            print("Он состоит в следующих пабликах:")
            for public in groups:
                print(requests.get(HOST + 'groups.getById', params={'group_id': public, 'access_token': access_token, 'v': VERSION}).json()["response"][0]["name"], "id =", public)
        else:
            print("Хвала летающему макаронному монстру! Пользователь не попущен!!!")

    def print_user_info(self):
        wall_info = self.get_wall_stats()

        print(
f"""
    Пользователь {user.first_name} {user.last_name}
    Пол: {user.sex}
    Родился {user.birthday}
    Насчитывает {user.wall_count} постов
    Получил {wall_info['likes']} лайков, {wall_info['reposts']} репостов, {wall_info['views']} просмотров
    Скопипастил {wall_info['copypasted']} постов
"""
        )
        self.popushennost_test()


if __name__ == '__main__':
    user = User(73303295)

    user.print_user_info()
