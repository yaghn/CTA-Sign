from CTA import CTA
from sign import Sign
import time
import math
import logging
import sys



RT = '74'
STOP = '1317'

class CTASign(object):
    def __init__(self,logger=None):
        self.busTime = CTA()
        self.matrix = Sign()
        self.pages=0
        self.buses=[]
        if logger:
           self.logger = logger
        else:
             self.logger = logging

    def run(self):
        while():
            self.updateBuses()
            
            if self.pages == 1:
                self.updateDisplay(self.buses)
                time.sleep(60)
            elif self.pages == 2:
                self.updateDisplay(self.buses[:2])
                time.sleep(30)
                self.updateDisplay(self.buses[2:])
                time.sleep(30)
            else:
                time.sleep(60)
                self.display()
    
    def updateBuses(self):
        self.logger.info('Updating Buses')
        resp = self.busTime.getPredictions(RT,STOP,'4')
        print resp
        if u'error' in resp[u'bustime-response']:
            self.logger.info('No Busses Running')
        else:
            self.buses = resp[u'bustime-response'][u'prd']
            self.pages = int(math.ceil(len(self.buses)/2.))
            self.logger.info('got {} buses'.format(str(len(self.buses))))


    def updateDisplay(self,buses):
        if len(buses) == 1:
            self.matrix.makeBus(buses[0],None)
        elif len(buses) == 2:
            self.matrix.makeBus(buses[0],buses[1])
        else:
            self.matrix.makeBus(None,None)
        self.matrix.display()

if __name__ == '__main__':
    print 'Running Matrix'
    ledSign = CTASign()
    try:
        ledSign.run()
    except KeyboardInterrupt:
        sys.exit(0)







