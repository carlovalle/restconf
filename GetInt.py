import requests
import sys
import os




#Allow self signed cert

requests.packages.urllib3.disable_warnings()

#credentials
user = "developer"
password = "C1sco12345"

# URL for get request

url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"

# set yang+json as the data formats

header = {"Content-Type":"application/yang-data+json",
          "Accept":"application/yang-data+json"}


# Run GET

response  = requests.get(url, auth=(user, password), headers = header, verify = False)

# create a file returning the result of GET

with open("getInterfaces.txt","w") as f:
    f.write(response.text)


print(response.text)