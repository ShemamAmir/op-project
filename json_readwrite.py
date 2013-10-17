import json 
test = json.dumps({
    "flow_id": 123,
    "time": "2012-07-01T13:01:00Z",
    "results": [
        {
            "destination_ip": "131.187.127.16",
            "destination_port": 17240,
            "source_ip": "131.187.118.27",
            "source_port": 49832,
            "bytes": 342,
            "packets": 8
        }
    ]
})
test = json.loads(test)

for i in test['results']:
    i['destination_ip'] = 10000
print test
