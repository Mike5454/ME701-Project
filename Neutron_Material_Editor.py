import os
import re
from decimal import Decimal
import numpy as np


#This will extract the element data in the material text file
data = open('Element_Data.txt', 'r')
element = []
zaidp = []
zaidn = []
abun = []
mass = []
for i in data.readlines():
    clean_data = re.sub('\s+', '', i)
    data2 = clean_data.split('-')
    element.append(data2[0])
    zaidp.append(data2[1])
    data2[2] = data2[2][1:-1]
    zaidn.append(data2[2])
    data2[3] = data2[3][1:-1]
    abun.append(data2[3])
    mass.append(data2[4])
    
abunlist=['Natural_Abundance']
neuzaid=['Neutron_ZAID_Numbers']

for i in abun:
    if i != 'Natural_Abundance':
        a = map(float, i.split(','))
        b = []
        for k in a :
            newk = k/100
            b.append(newk)
        abunlist.append(b)
for j in zaidn:
    if j != 'Neutron_ZAID_Numbers':
        c = map(str, j.split(','))
        neuzaid.append(c)

#This makes the libraries containing element mass and element zaid number
k=0
elemdict = {}
phozaiddict = {}
neuzaiddict = {}
abundict = {}
for j in element :
    elemdict[j] = mass[k]
    phozaiddict[j] = zaidp[k]
    neuzaiddict[j] = neuzaid[k]
    abundict[j] = abunlist[k]
    k +=1

class matp(object):
    
    def __init__ (self, a, ap) :
        self.a = a
        self.ap = ap
        pattern1 = r'[a-z][A-Z]|[A-Z][A-Z]'
        pattern2 = '[A-Z][^A-Z0-9]*'
        pattern3 = r'\d+'
        b = re.sub(pattern1,'a1a', a)
        self.elea = re.findall(pattern2, a)
        self.numb = re.findall(pattern3, b)
        c = len(self.numb) + len(self.elea)
        if c %2 != 0 and len(self.numb) != 1 or len(self.numb) == 0:
            self.numb.insert(len(self.numb), 1)
        while len(self.elea) != len(self.numb):
            self.numb = self.numb +[1]
#        print self.elea
#        print self.numb
            
    def __str__ (self):
        return "c Material: " + self.a + "   Composition: " + str(self.ap)
        
def photon(num,den,*args):
    check = 0
    for i in args:
        check = round(check,10) + round(i.ap,10)
    if check != 1 :
        return str('Error: Fractions do not sum to unity')
    curdict = {}
    total_mass = 0
    for i in element:
        curdict[i] = 0
    for i in args:
        k = 0
        mass_mol = 0
        for j in i.elea:
            curdict[j]= curdict[j] + (float(elemdict[j])*float(i.numb[k])*i.ap)
            mass_mol = mass_mol + float(elemdict[j])*float(i.numb[k])
            k+=1
        total_mass = total_mass + mass_mol*i.ap
    results = []
    for l in element:
        curdict[l] = curdict[l]/total_mass
        if curdict[l] != 0:
            a = str(phozaiddict[l] + '    -' + str(curdict[l]))
            results.append(a)
    datafile = open('MCNP_Pho.i', 'r+')
    newfile = []
    for i in datafile.readlines():
        if 'den' in str(i):
            a = re.sub('den', '-' + str(den), str(i))
            newfile.append(str(a)) 
        elif 'M1' in str(i):
            newfile.append('M1     ' + results[0] + str('\n'))
            for j in range(1,len(results)):
                k = results[j]
                newfile.append('       ' + k + str('\n'))
        else:
            newfile.append(i)
    datafile.close()
    final = open('MCNP_Pho_'+ str(num) + '.i', 'w')
    for i in newfile:
        final.write(i)
    final.close()
    for i in results:
        print i

def neutron(num,den,*args):
    check = 0
    for i in args:
        check = round(check,10) + round(i.ap,10)
    if check != 1 :
        return str('Error: Fractions do not sum to unity')
    curdict = {}
    total_mass = 0
    for i in element:
        curdict[i] = 0
    for i in args:
        k = 0
        mass_mol = 0
        for j in i.elea:
            curdict[j]= curdict[j] + (float(elemdict[j])*float(i.numb[k])*i.ap)
            mass_mol = mass_mol + float(elemdict[j])*float(i.numb[k])
            k+=1
        total_mass = total_mass + mass_mol*i.ap
    nzaid = []
    iso_mass=[]
    for l in element:
        curdict[l] = curdict[l]/total_mass
        if curdict[l] != 0:
            for i in neuzaiddict[l]:
                nzaid.append(i)
            for i in abundict[l]:
                isotope_mass = i*curdict[l]
                iso_mass.append(isotope_mass)
    results = []
    for i in range(0, len(nzaid)):
        a = str(str(nzaid[i]) + '    -' + str(iso_mass[i]))
        results.append(a)    
    datafile = open('MCNP_Neu.i', 'r+')
    newfile = []
    for i in datafile.readlines():
        if 'den' in str(i):
            a = re.sub('den', '-' + str(den), str(i))
            newfile.append(str(a)) 
        elif 'M1' in str(i):
            newfile.append('M1     ' + results[0] + str('\n'))
            for j in range(1,len(results)):
                k = results[j]
                newfile.append('       ' + k + str('\n'))
        else:
            newfile.append(i)
    datafile.close()
    final = open('MCNP_Mars_Neu_'+ str(num) + '.i', 'w')
    for i in newfile:
        final.write(i)
    final.close()
    for i in results:
        print i
    
def MCNP_Run(directory):
    dr = directory
    filelist = os.listdir(dr)
    for i in filelist:
        if '.i' in str(i):
            os.system('C:/MY_MCNP/MCNP_CODE/bin/mcnp6 i=' + dr + str(i) + ' o=' + dr + str(i)[:-2] + '.o')

            
# *****************************************************************************
# ******************************INPUT DATA*************************************
# *****************************************************************************
# Enter Molecules and Molecular Percents
# "Wet" Molecular Weight Fraction
percent = np.linspace(0,1,21)
densitydry = 2.7
densitywet = 1.00
for i in percent:
# "Dry" Molecular Composition and Mass Percent
    n=(1-i)
    a = matp("SiO2", 0.553 *n)
    b = matp("Fe2O3", 0.10 *n)
    d = matp("Al2CaK2MgNa2O7", .347*n)
#    e = matp("O2", 0.0013*n)
#    f = matp("CO", 0.0008*n)
    
# "Wet" Molecular composition to be used
    c = matp('H2O',i)
    den = densitydry*(1-i) + densitywet*i
    print "\n c Material Table with " + c.a +  " Composition: " + str(i)
    neutron(i,den,a, b, c, d)
# *****************************************************************************
# *****************************************************************************  
    

        
    
    