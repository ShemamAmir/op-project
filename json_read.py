#call library

import json
from pprint import pprint
from netaddr import *

json_data = open('example.json')
json_object = json.load(json_data)


# read transport_layer from object


# read network_layer from object
def get_src_ip(event):
  json_ip = json_object['address']['src']['network_layer']['ip_address']
  #ip = json.dumps(json_ip, sort_keys=True, separators=(', ',': '))
  for key, value in json_ip.iteritems():
    print(key,value)
  #check the format is ipv4, ipv6 or else
  #take out the ips that are ipv4
  #take out the ips taht are ipv6
  #emerge them into a new dict.
  #then the user can use get_src_ip(ipv4) to get ipv4
  #or get_src_ip(ipv6) to get ipv6
  
  
  
  return key, value


# read data_link_layer from object 


# read physical_layer from object 
