import requests


output =[]
for i in range(17):
    url = 'https://results.athlinks.com/event/1062874?eventCourseId=2407807&divisionId=&intervalId=&from='+str(1+50*i)+'&limit=100'
    
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        ats = data[0]["interval"]["intervalResults"]

        for a in ats:
            output.append([a["displayName"],a["pace"]["time"]["timeInMillis"]])


# print output to csv file
import csv
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(output)