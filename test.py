import json, os


data = {}
data['guilds'] = []


# Add new guild into Json
def new_guild(guild):
    with open('test.json', 'r') as f:
        data = json.load(f)

        data['guilds'].append({
            'id': guild,
            'prefix': None,
            'channel': None,
            'allowed_roles': None
        })

    with open('test.json', 'w') as f:
        json.dump(data, f, indent=2)


# Edit channel guild into Json
def json_channel(id, channel):
    with open('test.json', 'r') as f:
        data = json.load(f)

        for guild in data['guilds']:
            if guild['id'] == id:
                print(id)
                guild['channel'] = channel
                print(guild['channel'])
                break

    with open('test.json', 'w') as f:
        json.dump(data, f, indent=2)


# Edit prefix guild into Json
def json_edit(id, key, value):
    with open('test.json', 'r') as f:
        data = json.load(f)

        for guild in j['guilds']:
            if guild[key] == value:
                #print(guild['prefix'])
                guild[key] = value
                break


    with open('test.json', 'w') as f:
        json.dump(json.dump(data, f, indent=2), f)

#new_guild('06')
#json_channel('04', 'CHA04')
json_edit('04', 'prefix', '!')
