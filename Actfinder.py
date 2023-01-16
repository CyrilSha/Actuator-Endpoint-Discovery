import requests
import sys
import art

Logo=text2art("Actuator Discovery")
print(Logo)

print("Enter command :")
CliInput = input()
print(CliInput)

url = input("Please enter a URL: ")
response = requests.get('http://' + url)

if response.status_code == 200:
    endpoints = response.json()['_links']
    for endpoint in endpoints:
        endpoint_url = endpoints[endpoint]['href']
        endpoint_response = requests.get(endpoint_url)
        if endpoint_response.status_code == 200:
            print(f'{endpoint_url} is up')
        else:
            print(f'{endpoint_url} is down')
else:
    print('Error: Unable to fetch actuator endpoints')