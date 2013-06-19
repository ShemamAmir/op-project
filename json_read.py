#call library

import json
import pprint
from netaddr import *

json_data = open('example.json')
json_object = json.load(json_data)


# read transport_layer from object


# read network_layer from object
#def get_ip():
json_ip = json_object["address"]["src"]["network_layer"]["ip_address"]
ip = json.dumps(json_ip, separators=(', ',': '))
for key, value in json_ip.iteritems():
  print(key, value)


  #define it is ipv4 or ipv6



# read data_link_layer from object 


# read physical_layer from object 
