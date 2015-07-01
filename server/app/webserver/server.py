import os
import queue
import cherrypy
import webbrowser
import random    
from . import eventsource
from . import config

def setup_webserver( event, result):
    port = 7001
    cherrypy.server.socket_port = port
    cherrypy.tree.mount(  Server( event, result ) , "/" , config.static_dir_config() ) 
    cherrypy.engine.signals.subscribe()

def start_webserver():
    cherrypy.engine.start()
    ip = "127.0.0.01"
    port =  cherrypy.server.socket_port
    url = "index"
    urlOfBackend = "http://{0}:{1}/{2}".format( ip , port , url )
    open_webbroswer( urlOfBackend ) 

def stop_webserver() :
    cherrypy.engine.exit()

def open_webbroswer( url ) :
    webbrowser.open( url )
    print( "webserver is now running" )
    

stop_pump = set([ cherrypy.engine.states.STOPPING ,cherrypy.engine.states.EXITING ])

def pump_response_messages(result_queue):
    while True:
        try:

            event = result_queue.get( timeout = 0.1 )
            es = eventsource.eventsource( "wordListUpdate" , 10000 )
            es.add( event )
            yield str( es )        
                    
        except queue.Empty:
            pass

        if cherrypy.engine.state in stop_pump :
            break

    yield str("")
    return

class Server(object):
    def __init__(self, event_queue, result_queue):
        self.result_queue = result_queue
        self.event_queue = event_queue

    @cherrypy.expose
    def index( self ) :
        with open( os.path.join( ".." , "content" , "webserver"  , "pages" , "index.html" ) ) as f:
            return f.read()
            
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def keypress(self):
        keypress = cherrypy.request.json
        self.event_queue.put( keypress )

    @cherrypy.expose
    def result_list(self):
        cherrypy.response.headers["Content-Type"] = "text/event-stream"
        cherrypy.response.headers["Cache-Control"] = "no-cache"
        return pump_response_messages(self.result_queue)
    result_list._cp_config = {'response.stream': True, 'tools.encode.encoding':'utf-8'}