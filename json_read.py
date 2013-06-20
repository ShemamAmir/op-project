#call library
# ./pox.py samples.pretty_log forwarding.l2_learning misc.mac_blocker tk < 作為範例。
# should work with the pox controller as a pox module 
# https://openflow.stanford.edu/display/ONL/POX+Wiki#POXWiki-DevelopingyourownComponents
import json
from pox.lib.addresses import IPAddr, EthAddr
from netaddr import *
from pox.lib.addresses import IPAddr, EthAddr

def load_json(name):
  json_data = open(name)
  json_object = json.load(json_data) #type: dict. 
  return json_object, json_data


# read transport_layer from object


# read network_layer from object
def get_src_ip(event):
  json_ip = json_object['address']['src']['network_layer']['ip_address']
  #ip = json.dumps(json_ip, sort_keys=True, separators=(', ',': '))
  for key, value in json_ip.iteritems():
    #key = key # todo: find a way to link key, but is key needed?
    ip = IPAddr(value)
    return ip
  for ipnet in ip:
    parts = ipnet.split("/")
    ip = parts[0]
    bits = int(parts[1]) if len(parts)>1 else 32
    # set the IP address
    setattr(m, attr, ipnet)

    # gets converted to just the ip address during query
    self.assertEqual(getattr(m, attr), ip)

    # the get_#{attr} method gives a tuple of (ip, cidr-bits)
    self.assertEqual( getattr(m, "get_"+attr)(), (ip, bits))

    # the appropriate bits in the wildcard should be set
    self.assertEqual( (m.wildcards & bitmask) >> shift, 32-bits)

    # reset to 0.0.0.0/0 results in full wildcard
  setattr(m, attr, "0.0.0.0/0")
  self.assertEquals(getattr(m, "get_"+attr)(), (None, 0), "get_%s for unset %s should return (None,0)" % (attr, attr))
  self.assertTrue( ((m.wildcards & bitmask) >> shift) >= 32)
    
  #check the format is ipv4, ipv6 or else
  #take out the ips that are ipv4
  #take out the ips taht are ipv6
  #emerge them into a new dict.
  #then the user can use get_src_ip(ipv4) to get ipv4
  #or get_src_ip(ipv6) to get ipv6
  
  
  


# read data_link_layer from object 


# read physical_layer from object 



def launch( allow_unknown = True ):
  core.RegisterNew(class_name_tbd, class(input)) #core.Register(object_name, class(input)) register  object and core. RegisterNew(class_name, input) pass a class

