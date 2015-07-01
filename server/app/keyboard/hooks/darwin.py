from AppKit import NSApplication, NSObject, NSApp
from Cocoa import NSEvent, NSKeyDownMask
from PyObjCTools import AppHelper
import Quartz

def handler( event ) :
    try :
        unicode_tuple = Quartz.CGEventKeyboardGetUnicodeString( event.CGEvent() , 2 , None , None )
        letter = unicode_tuple[1]
        
        if letter == "\r" :
            keypress = "enter"
        elif letter == " " :
            keypress = "space"
        elif letter == u'\x1b' :  # escape
            keypress = "espace"
        elif letter == u'\x08' :  # backspace
            keypress = "backspace"
        else :
            keypress = letter
                
        #post_keypress( keypress )
        
    except KeyboardInterrupt:
        AppHelper.stopEventLoop()
    
class Delegate( NSObject ) :
    def applicationDidFinishLaunching_( self , notification ) :
        mask = NSKeyDownMask
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_( mask , handler )

def StartMainloop( post_keypress ) :
    app = NSApplication.sharedApplication()
    delegate = Delegate.alloc().init()
    NSApp().setDelegate_( delegate )
    AppHelper.runEventLoop()
