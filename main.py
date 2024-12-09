import vk_api
import json

print("Enter phone:")
phone = input()

print("Enter token:")
token = input()

vk_session = vk_api.VkApi(login=phone, token=token)

tools = vk_api.VkTools(vk_session)

print("Enter wall:")
owner = input()

wall = tools.get_all('wall.get', 100, {'owner_id': owner})

print(f"Retrieved posts: {wall['count']}")

with open(f"dumps/{owner}_dump.json", "w") as f:
    f.write(json.dumps(wall))

with open(f"dumps/{owner}_posts.txt", "w") as f:
    for index, item in enumerate(wall['items']):
        f.write(str(index) + "\n")
        f.write(item['text'] + "\n")
