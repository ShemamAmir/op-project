#call library
# ./pox.py samples.pretty_log forwarding.l2_learning misc.mac_blocker tk < 作為範例。
# should work with the pox controller as a pox module 
# https://openflow.stanford.edu/display/ONL/POX+Wiki#POXWiki-DevelopingyourownComponents
import json
from pox.lib.addresses import IPAddr, EthAddr
from netaddr import *
import pox.lib.packet as pkt

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
    ipv4_src = []
    ipv4_dst = []
    ipv6_src = []
    ipv6_dst = []
    # we can use http://boubakr92.wordpress.com/2012/12/20/convert-cidr-into-ip-range-with-python/ or netaddr lib
    for key, value in json_src_ip.iteritems():  
      ip_cidr = IPNetwork(str(value))
      ip = ip_cidr.ip,
      ip_network = ip_cidr.network
      ip_broadcast = ip_cidr.broadcast
      ip_netmask = ip_cidr.netmask
      ip_hostmask = ip_cidr.hostmask
      ip_size = ip_cidr.size
      
      ipv4_src.append(ip_cidr.ipv4())
      ipv6_src.append(ip_cidr.ipv6())
     
    
    for key, value in json_dst_ip.iteritems():  
      ip_addr = IPAddress(str(value))
      ip = ip_cidr.ip,
      ip_network = ip_cidr.network
      ip_broadcast = ip_cidr.broadcast
      ip_netmask = ip_cidr.netmask
      ip_hostmask = ip_cidr.hostmask
      ip_size = ip_cidr.size
      ipv4_dst.append(ip_addr.ipv4())
      ipv6_dst.append(ip_addr.ipv6())    
    

  def get_tcp(self):
    json_src_tcp = self.load_json()['address']['src']['transport_layer']['tcp_address']
    json_dst_tcp = self.load_json()['address']['dst']['transport_layer']['tcp_address']
    tcp_src = []
    tcp_dst = []
      #http://en.wikipedia.org/wiki/Transmission_Control_Protocol
      #TODO? SRC_PORT, DST_PORT, SEQ, ACK= ?
    for key, value in json_src_tcp():
      tcp_src.append(str(json_src_tcp))        
    for key, value in json_dst_tcp():
      tcp_src.append(str(json_dst_tcp))      
      #http://ciscoiseasy.blogspot.com/2010/08/lesson-6-example-of-tcpip-traffic-flow.html
    return tcp_src, tcp_dst
      
  def get_mac(self):
    json_src_mac = self.load_json()['address']['src']['data_link_layer']['mac_address']
    json_dst_mac = self.load_json()['address']['dst']['data_link_layer']['mac_address']
    mac_src = []
    mac_dst = []
    for key, value in json_src_mac():
      mac_src.append(str(json_src_tcp))        
    for key, value in json_dst_mac():
      mac_src.append(str(json_dst_tcp))    
    return mac_src, mac_dst
      
  def get_port(self):
    json_src_port = self.load_json()['address']['src']['physical_layer']['switch_dpid']
    json_dst_port = self.load_json()['address']['dst']['physical_layer']['switch_dpid']
    port_src = []
    port_dst = []      
    for key, value in json_src_port():
      port_src.append(str(json_src_port))        
    for key, value in json_dst_mac():
      port_src.append(str(json_dst_port))  
    return port_src, port_dst_list
    

  def check_unknown(self):
    #check the flow table 
    if self.load_json()['flow_control']['unkown'] = True:
      self.load_json()['flow_control']['allow'] = json.dumps(False)
    else:
      self.load_json()['flow_control']['allow'] = json.dumps(True)
          

  def check_many(self):
    if len(ipv4_src) > 1 or len(ipv6_src) > 1 or len(mac_src) > 1 or len(port_src) > 1 or len(tcp_src) > 1 :
      many_to_point = True
      self.load_json()['flow_control']['many_to_point'] = json.dumps(True)
    else:
      many_to_point = False
      self.load_json()['flow_control']['many_to_point'] = json.dumps(False)      

      
#When the flag: many_to_point = True

class route_scheme(object,many_to_point = True):
  
  def __init__(self, name):
    self.name = name
        
  def low_ult(self):
  #utilization % = (data bits x 100) / (bandwidth x interval)
    
    
  def low_rtt(self):
  #lowest ping time
  #make srcs ping with random order and set the rule by the ping time, dynamic rule
    
  def low_priority(self):
  #define priority
    
    
    
    
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
  core.RegisterNew(get_json)
  #core.Register(object_name, class(input)) register  object and core. RegisterNew(class_name, input) pass a class

