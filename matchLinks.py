import sys, VARS, urllib.request, json, os, subprocess

def getName(match):
    typ = match["comp_level"]
    if typ == 'qm':
        typ = 'Q'
    else:
        typ = typ.upper()
    return typ+str(match["match_number"])+".mp4"

req = urllib.request.Request("https://www.thebluealliance.com/api/v2/event/"+sys.argv[1]+"/matches", headers=VARS.headers)
data = json.load(urllib.request.urlopen(req))
teamMap = {}
for match in data:
    teams = match["alliances"]["red"]["teams"] + match["alliances"]["blue"]["teams"]
    name = getName(match)
    for team in teams:
        if not (team in teamMap):
            teamMap[team] = []
        teamMap[team].append(name)
for filename in os.listdir(VARS.teamDir):
    space = filename.find(" ")
    key = "frc"+filename[:space]
    if key in teamMap:
        for match in teamMap[key]:
            linkPath = VARS.teamDir+"/"+filename+"/"+match
            dest = "../../"+VARS.videoDir+"/"+match
            subprocess.Popen(["ln", "-sf", dest, linkPath])
