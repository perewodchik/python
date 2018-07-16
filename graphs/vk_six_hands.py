#Теория шести рукопожатий
import requests #делать запросы
import time #делать задержки между двумя запросами
from tqdm import tqdm #progress bar
from collections import deque

HOST = 'https://api.vk.com/method/'
VERSION = '5.74'
access_token = 'f5b07d14abab4882b695f63557b2a8fb8d6f05c273481ea118e54b923ae07a365c5902b0e54a8f13b5cf3'

id_start =	169714598
id_end = 1770436

r = [requests.get(HOST + 'users.get', params={'user_ids': id_start, 'access_token': access_token, 'v': VERSION}),
	requests.get(HOST + 'users.get', params={'user_ids': id_end, 'access_token': access_token, 'v': VERSION})]

r_good_looking = [ r[0].json()['response'][0], r[1].json()['response'][0] ]

print("Ищем путь друзей между двумя пользователями")
print("Стартовый пользователь\n",r_good_looking[0])
print("Конечный пользователь\n",r_good_looking[1])


def get_friends_list(id_user):
	r = requests.get(HOST + 'friends.get', params={'user_id': id_user, 'access_token': access_token, 'v': VERSION})
	if 'response' in r.json():
		return r.json()['response']['items']
	return []

queue = deque(get_friends_list(id_start))

distances = {v: 1 for v in queue}
parents = {v: id_start for v in queue}

while id_end not in distances:
	current_user = queue.popleft()
	new_users = get_friends_list(current_user)
	time.sleep(0.2)
	for u in tqdm(new_users, total=len(new_users), ncols=70, desc='searching', postfix='finished, friends scanned:',  bar_format='{l_bar}{bar}{postfix}{total_fmt}'):
	#for u in new_users:
		if u not in distances:
			queue.append(u)
			distances[u] = distances[current_user] + 1
			parents[u] = current_user


path = [id_end]
parent = parents[id_end]
parents[id_start] = None
while parent is not None:
	path.append(parent)
	parent = parents[parent]
path[:] = (path[::-1])


for user in path:
	requested_user_unmodified = requests.get(HOST + 'users.get', params={'user_id': user, 'access_token': access_token, 'v': VERSION})
	if 'response' in requested_user_unmodified.json():
		requested_user = requested_user_unmodified.json()['response'][0]
		print('Name:', requested_user['first_name'] + " " + requested_user['last_name'], '- id:', requested_user['id'])
	else:
		print("Случилось какое-то говно. Скорее всего, VK API подлагал")
