from Simpy.Simulation import*
from Simpy.Simplot import*



class Source(Process):
    def generate(self,noOfCustomers):
        for i in range(noOfCustomers):
            c  = Customer(name="Customer%d"%i)
            activate(c,c.visit())
            yield hold,self,2


class Customer(Process):
    def visit(self):
        at = now()
        print at , self.name,"Arrived"
        yield request,self,k
        wait = now()-at
        wm.observe(wait)
        yield hold ,self,5
        print self.name,"Waited for ",wait
        yield hold,self,5
        yield release,self,k
        print now(),self.name,"Leaving"


initialize()
s =  source()
k = Resource(monitored = True)
activate(s,s.generate(5),at=0)
cl = Customer(name = "mrX")
activate(cl,c1.visit(),at=5)
c2 = Customer(name = "mrY")
activate(c2,c2.visit(),at=2)

simulate(until = 100)
print wm.count(),wm.mean()
print k.waitMon
plt = Simplot()
plt.plotBars(k.waitMon)
plt.mainloop()

