import json, urllib.request, VARS, sys

req = urllib.request.Request("https://www.thebluealliance.com/api/v2/event/"+sys.argv[1]+"/teams", headers={
    'X-TBA-App-Id': VARS.appID,
    'User-Agent': 'Not Chrome'
})
data = json.load(urllib.request.urlopen(req))
for team in data:
    name = str(team["team_number"]) + " " + str(team["nickname"])
    print(name)
