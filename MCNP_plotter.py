import numpy as np
import matplotlib.pyplot as plt
import re

#from read import periodOutput

class process(object):
    '''
    This class reads the MCNP output, extracts necessary information (k_eff & kinetics paramters)
    '''
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.results = []
        self.readMCNPOutput()
        #self.computerModelRho()
        
        #self.period = period
        #self.periodU = periodU

        
        #self.computeRho()
        
    
    def readMCNPOutput(self):
        #results = []
        F = open('MCNP_{}_Neu_{}.o'.format(self.name,self.number), 'r').readlines()
        # Iterate over the output file
        for i, line in enumerate(F):
            # Find the line beginning the precursor groups
            if 'this tally' in line:
                # Begin iterating through the rest of the file
                for j, _ in enumerate(F[i:]):
                    if 'surface ' in _:
                        self.results.append(F[j+i+1])
                        return self.results

if __name__ == "__main__":
    names = ['Mars','Earth']
    a = []
    for name in names:
        x = np.arange(0,1.05,0.05)
        for i in x:
            p=process(name,i)
            a.append(p.results)
            
            
MCNP_control = 2.42092E+14            
data=[]
for i in a:
    i = str(i)
    i = i[:-11]
    i = i[-12:]
    data.append(float(i))
Mars = []
Earth = []
for i in range(0,21):
    a = (data[i] - MCNP_control)/MCNP_control
    Mars.append(a)
for i in range(21,42):
    b = (data[i] - MCNP_control)/MCNP_control
    Earth.append(b)
    
# Now we have the collided over uncollided dose ratio       
#print Mars
#print Earth   
#print x           
            
plt.Figure
plt.figure(figsize = (7,5))
plt.xlabel("Percent Water Composition", fontsize=18)
plt.ylabel("Collided/Un-collided Dose", fontsize=14)
plt.title ("Test of Particle Albedo",fontsize=18)
plt.xlim(0, 1)
plt.ylim(0, 1)

p1 = plt.plot(x, Mars, 'k-', label = 'Mars')
p2 = plt.plot(x, Earth, 'r-', label = 'Earth')
plt.legend()
plt.show()
