import requests as request

data= {
    "allowed_mentions":{
        "parse":["users","everyone","roles"]
    },
    "content":"/buy",
    "username":"EEEEE",
 #   "avatar_url":""


}
webhook_url = 'https://discord.com/api/webhooks/1370946492533313661/YCsiMn-BxeEFeZHQp1z-a6CSmclBsYsTd5Ct6UREvZjpUNyMz64Si20mdRRrydvRqPHq'

request.post(webhook_url,json=data)
