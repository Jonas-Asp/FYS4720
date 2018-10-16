import matplotlib.pyplot as plt
import numpy as np



img = plt.imread('2017-Gr1.jpg')

print(np.shape(img))

### Cut image in half
ba = img[110:160,150:450]
s = img[280:400,140:500]

bactin = ba.max(0)
sample = s.max(0)


##### Finding peaks
peak = np.zeros(6)
peakindex = np.zeros(6)
pcount = 0
leap = 0
threshold = 20
tcount = 0
index = [0,0]
for i in range(len(bactin)):
    if(bactin[i] < threshold):
        #print(i)
        if(tcount == 1):
            tcount = 0
            pcount += 1
    elif(bactin[i] > peak[pcount]):
        peak[pcount] = bactin[i]
        peakindex[pcount] = i
        if(tcount == 0):
            tcount = 1
    if(pcount == 6):
       break; 




peak = peak/peak.max()
bactin = bactin/bactin.max()


#### image beta actin
x = np.linspace(1,len(bactin),len(bactin))
plt.imshow(ba)
plt.show()
plt.plot(x,bactin)
plt.plot(peakindex,peak,'o-')
plt.xlabel('Piksel indeks')
plt.ylabel('Normalisert intensitet')
plt.show()





##### Finding peaks
peak2 = np.zeros(6)
peakindex2 = np.zeros(6)
pcount = 0
leap = 0
tcount = 0
ind = [0,60,108,151,200,250,len(sample)]
for j in range(len(ind)-1):
    for i in range(ind[j+1]-ind[j]):
        if(sample[ind[j]+i] > peak2[j]):
            peak2[j] = sample[ind[j]+i]
            peakindex2[j] = ind[j]+i


peak2 = peak2/peak2.max()
sample = sample/sample.max()
###### Sample plotting
x2 = np.linspace(1,len(sample),len(sample))
plt.imshow(s)
plt.show()
plt.plot(x2,sample)
plt.plot(peakindex2,peak2,'o-')
plt.xlabel('Piksel indeks')
plt.ylabel('Normalisert intensitet')
plt.show()

##### Normalising
norm = peak2/peak
adjust = peak
adjust[4] = 0.82
normadjusted = peak2/adjust
plt.plot(np.linspace(0,2.5,6),normadjusted,'--o', color="orange", label='Adjusted $beta$-actin')
plt.plot(np.linspace(0,2.5,6),norm,'o-', label='Original plot')
plt.xlabel('Dose [Gy]')
plt.ylabel('Antall p53 proteiner [arb.unit]')
plt.legend()
plt.title('Antall p53 proteiner ved gitt dose')
plt.show()