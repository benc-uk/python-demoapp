from flask import url_for, redirect, render_template, flash, g, session
from app import app
#import socket
import cpuinfo
import psutil
import platform

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/info')
def info():
   osinfo = {}
   #osinfo['hostname'] = socket.gethostname()
   osinfo['plat'] = platform
   osinfo['cpu'] = cpuinfo.get_cpu_info()
   osinfo['mem'] = psutil.virtual_memory()
   osinfo['net'] = psutil.net_if_addrs()

   return render_template('info.html', info = osinfo)