#call library
# ./pox.py samples.pretty_log forwarding.l2_learning misc.mac_blocker tk < 作為範例。
# should work with the pox controller as a pox module 
# https://openflow.stanford.edu/display/ONL/POX+Wiki#POXWiki-DevelopingyourownComponents
import json
from pox.lib.addresses import IPAddr, EthAddr
from netaddr import *
import socket

class get_json(object):
  
  
  def __init__(self, name):
    self.name = name
    
  def load_json(self):
    json_data = open(self.name)
    json_object = json.load(json_data) #type: dict. 
    return json_object
     
          
  def get_ip(self):
    json_src_ip = self.load_json()['address']['src']['network_layer']['ip_address']
    json_dst_ip = self.load_json()['address']['dst']['network_layer']['ip_address']
    #ip = json.dumps(json_ip, sort_keys=True, separators=(', ',': '))
    ip_src_list = []
    ip_dst_list = []
    for key, value in json_src_ip.iteritems():
    #test validation for src ip address
      try:
        socket.inet_aton(str(value))
        ip_src_list.append(IPAddr(str(value)))
        # legal
      except socket.error:
        print(value + 'it is not an valid IP Address')
        # Not legal
        
    #test validation for dst ip address    
    try:
        socket.inet_aton(str(json_dst_ip))
        ip_src_list.append(IPAddr(str(json_dst_ip))
        # legal
      except socket.error:
        print(value + 'it is not an valid IP Address')
        # Not legal    
    
    def get_tcp(self):
      json_src_tcp = self.load_json()['address']['src']['transport_layer']['tcp_address']
      json_dst_tcp = self.load_json()['address']['dst']['transport_layer']['tcp_address']
      tcp_src_list = []
      tcp_dst_list = []
      #http://en.wikipedia.org/wiki/Transmission_Control_Protocol
      #TODO? SRC_PORT, DST_PORT, SEQ, ACK= ?
      for key, value in json_src_tcp():
        tcp_src_list.append(str(json_src_tcp))        
      for key, value in json_dst_tcp():
        tcp_src_list.append(str(json_dst_tcp))      
      #http://ciscoiseasy.blogspot.com/2010/08/lesson-6-example-of-tcpip-traffic-flow.html
      
    def get_mac(self):
      json_src_mac = self.load_json()['address']['src']['data_link_layer']['mac_address']
      json_dst_mac = self.load_json()['address']['dst']['data_link_layer']['mac_address']
      mac_src_list = []
      mac_dst_list = []
      for key, value in json_src_mac():
        mac_src_list.append(str(json_src_tcp))        
      for key, value in json_dst_mac():
        mac_src_list.append(str(json_dst_tcp))    
        
    def get_port(self):
      json_src_port = self.load_json()['address']['src']['physical_layer']['switch_dpid']
      json_dst_port = self.load_json()['address']['dst']['physical_layer']['switch_dpid']
      port_src_list = []
      port_dst_list = []      
      for key, value in json_src_port():
        port_src_list.append(str(json_src_port))        
      for key, value in json_dst_mac():
        port_src_list.append(str(json_dst_port))       
    
  #def get_dst_ip(self)
  #def get_src_
      
      
    
       
    #check the format is ipv4, ipv6 or else
    #take out the ips that are ipv4
    #take out the ips taht are ipv6
    #emerge them into a new dict.
    #then the user can use get_src_ip(ipv4) to get ipv4
    #or get_src_ip(ipv6) to get ipv6
    #json.dump to import to the json file
    
    
    
  
  
  # read data_link_layer from object 
  

# read physical_layer from object 



def launch( allow_unknown = True ):
  core.RegisterNew(class_name_tbd, class(input)) #core.Register(object_name, class(input)) register  object and core. RegisterNew(class_name, input) pass a class

