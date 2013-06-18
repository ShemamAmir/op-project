#call library

import json
import pprint
from netaddr import *

json_data = open('object.json')
json_object = json.load(json_data)


# read transport_layer from object 


# read network_layer from object 

json_object_network = json_object["address"]["src"]["network_layer"]["ip_address"]

print(json_object_network)

  #define it is ipv4 or ipv6



# read data_link_layer from object 


# read physical_layer from object 
