import requests
from cloudant.client import Cloudant

url='http://api.icndb.com/jokes/random'
PORT_NUMBER = 8080
cred = {
  "username": "13119a46-72cc-4f66-ad4d-239cdb813e0c-bluemix",
  "password": "f992a4aa0b014e94f3029101c8c7923af6691343fabce39fc851b6c3c69cf943",
  "host": "13119a46-72cc-4f66-ad4d-239cdb813e0c-bluemix.cloudant.com",
  "port": 443,
  "url": "https://13119a46-72cc-4f66-ad4d-239cdb813e0c-bluemix:f992a4aa0b014e94f3029101c8c7923af6691343fabce39fc851b6c3c69cf943@13119a46-72cc-4f66-ad4d-239cdb813e0c-bluemix.cloudant.com"
}
client = Cloudant(cred['username'], cred['password'], url=cred['url'], account=cred['username'])
client.connect()
my_database = client['mydb']

for i in range(20):
	joke = requests.get(url).json()['value']['joke']
	my_database.create_document({'joke': joke})
