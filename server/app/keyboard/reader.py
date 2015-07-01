from AppKit import NSApplication, NSObject, NSApp
from Cocoa import NSEvent, NSKeyDownMask
from PyObjCTools import AppHelper
import requests
import json
import Quartz
import logging
import argparse
import signal
import psutil
import sys
from pid.decorator import pidfile
import pid
import os
import time

import subprocess
import platform

def post_keypress( key ) :
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    payload = json.dumps({'keypress':key})
    port = 7001
    url = "127.0.0.1"
    
    try:
        r = requests.post("http://{0}:{1}/keypress".format(url, port), data=payload, headers=headers)
    except requests.exceptions.ConnectionError :
        print( "post to ip {0} port {1} failed".format( url , port ) )
     

def darwin( ):
    import hooks
    hooks.darwin.StartMainloop( post_keypress )

def linux():
    pass

def windows():
    pass
        
@pidfile( pidname = ".keybaord_reader_lock" , piddir = "." )
def runApp():
    
    system = platform.system()

    if system  == "Darwin" :
        darwin()
        
    elif system == "Linux" :
        pass
    
    elif system == "windows" :
        pass

    
if __name__ == "__main__":
    try:
        runApp()
    except pid.PidFileError :
        pid=int( open(".keybaord_reader_lock.pid").read() )
        p=psutil.Process(pid)
        p.kill()
        time.sleep(0.2) 
        runApp()
        
def startreader(ip, port):
    cmd = ["python3", "keyboard/reader.py", "--ip", ip, "--port", str(port)]
    process = subprocess.Popen(cmd)
    return process

