import os

def static_dir_config():
   dirs = [ "css" , "js" , "images" , "pages" , "style" ]
   config = {}
   current_dir = os.path.abspath( "../content/webserver")
   for scd in dirs :
      key = os.path.join( "/", scd )
      config[key] = dict()
      config[key]["tools.staticdir.on"] = True
      config[key]["tools.staticdir.dir"] = os.path.join( current_dir , scd )
   print( config )
   
   return config

def host():
    server_ip = "127.0.0.1"
    server_port = 7002
    return { "server.socket_host":server_ip , "server.socket_port":server_port }
