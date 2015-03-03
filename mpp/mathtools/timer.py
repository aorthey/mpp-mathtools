from timeit import default_timer as timer
import numpy as np

class Timer:
        def __init__(self,name="program"):
                self.start = timer()
                self.end = -1.0
                self.time = 0.0
                self.name = name

        def getTime(self):
                return self.time

        def stopWithoutPrint(self):
                self.end = timer()
                self.time = self.end - self.start

        def stop(self,comment=None):
                self.end = timer()
                self.time = self.end - self.start
                self.ptime(self.time,comment)

        def ptime(self,time,comment=None):
                ts= np.around(time,2)
                tm= int(ts/60)
                tms = np.around(ts - tm*60,2)
                print "================================================================"
                print "Time elapsed for",self.name
                print "================="
                print tm,"m",tms,"s (",ts,"s)"
                if comment is not None:
                        print comment
                print "================================================================"


