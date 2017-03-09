import sys

appID = "frc2122:automatic-umbrella:1"
headers = {
    'X-TBA-App-Id': appID,
    'User-Agent': 'Not Chrome'
}
teamDir = "Teams"
videoDir = "Videos"

if len(sys.argv) > 1:
    if sys.argv[1] == "teamDir":
        print(teamDir)
    elif sys.argv[1] == "videoDir":
        print(videoDir)
