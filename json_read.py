#call library
# ./pox.py samples.pretty_log forwarding.l2_learning misc.mac_blocker tk < 作為範例。
# should work with the pox controller as a pox module 
# https://openflow.stanford.edu/display/ONL/POX+Wiki#POXWiki-DevelopingyourownComponents
import json
from pox.lib.addresses import IPAddr, EthAddr
from netaddr import *
from pox.lib.addresses import IPAddr, EthAddr
import socket

class get_json(object):
  
  
  def __init__(self, name):
    self.name = name
    
  def load_json(self):
    json_data = open(self.name)
    json_object = json.load(json_data) #type: dict. 
    return json_object
     
  def get_src_ip(self):
    json_ip = json_object['address']['src']['network_layer']['ip_address']
    #ip = json.dumps(json_ip, sort_keys=True, separators=(', ',': '))
    ip_list = []
    for key, value in json_ip.iteritems():
      # convert ipv4 to ipv6
      
      # test if they are valid IPV4 Addresses
      try:
        socket.inet_aton(str(value))
        ip_list.append(IPAddr(str(value)))
        # legal
      except socket.error:
        print(value + 'is no an valid IP Address')
        # Not legal
      
      
      
      if it is ip:
        
      else:
        
      
      
    for ipnet in ip:
       
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

