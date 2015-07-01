import json

class eventsource:
    id = 0
    def __init__(self, event=None, retry=None):
        self.data = []
        self.event = event
        self.retry = 1000


    def add(self, data):
        self.data.append( data )

    def __str__(self):
        res =""
        if self.retry:
            res+="retry: {0}".format( self.retry)+"\n"

        if self.event:
            res+="event: {0}".format(self.event)+"\n"

        res+= "id: {0}".format(eventsource.id)+"\n"

        res+= "\n".join( [ "data: {0}".format( json.dumps(d)) for d in self.data] )
        res+="\n"
        res+="\n"
        eventsource.id+= 1
        return res




#e = eventsource("test")
#e.add("test")
#e.add("master")

#str = str( e )
#print "<"+ str + ">"