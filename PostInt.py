import requests
import sys
import os
import json




#Allow self signed cert

requests.packages.urllib3.disable_warnings()

#credentials
user = "developer"
password = "C1sco12345"

# URL for get request

url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"



# Body
body= '''{
      "ietf-interfaces:interface": {
          "name": "Loopback101",
          "description": "Added with RESTCONF",
          "type": "iana-if-type:softwareLoopback",
          "enabled": true,
          "ietf-ip:ipv4": {
              "address": [
                  {
                      "ip": "172.16.100.2",
                      "netmask": "255.255.255.0"
                  }
              ]
          }
      }
  }'''

# set yang+json as the data formats

header = {
    "Accept":"application/yang-data+json",
    "Content-Type":"application/yang-data+json"
          }

# Run POST

response  = requests.post(url, auth=(user,password),data = body,headers = header, verify = False )

print(response)