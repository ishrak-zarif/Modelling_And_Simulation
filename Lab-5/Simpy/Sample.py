from SimPy.Simulation import *
from SimPy.SimPlot import *


class Source(Process):
    def generate(self,noOfCustomers):
        for i in range(noOfCustomers):
            c = Customer(name="Customer%d"%i)
            activate(c,c.visit())
            yield hold,self,2
        
        
    
class Customer(Process):
    def visit(self):
       at = now()
       print at,self.name, "Arrived"
       yield request,self,k
       wait = now() - at
       wm.observe(wait)
       print self.name, "Waited for ", wait
       yield hold,self,5
       yield release,self,k
       print now(),self.name, "Leaving"
       

initialize()
s = Source()
k = Resource(monitored=True)
wm = Monitor()
activate(s,s.generate(5),at=0)
simulate(until=100)

print wm.count(),wm.mean()

print k.waitMon
plt = SimPlot()
plt.plotBars(k.waitMon)
plt.mainloop()
