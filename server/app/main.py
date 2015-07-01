import queue
import keyboard
import webserver
import wordpredictor

from pid.decorator import pidfile
@pidfile( pidname = "buchstabieren_lock" , piddir = "." )
def runApp():
    event_queue = queue.Queue()
    result_queue = queue.Queue()
    #keyboardReaderProess = keyboard.reader.startreader( "0.0.0.0" , 9001 )
    webserver.setup_webserver( event_queue , result_queue )
    webserver.start_webserver()
    wp = wordpredictor.predictorloop.PredictorLoop( event_queue , result_queue )
    wp.run()
    webserver.stop_webserver()
    keyboardReaderProess.kill()
      
    
if __name__ == "__main__":
    runApp()
    


  
      
      