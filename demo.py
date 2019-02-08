import requests
import pprint

x = requests.get("http://opencode-leaderboard.herokuapp.com/users/leaderboard")

pprint.pprint(x.text)