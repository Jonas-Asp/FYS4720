import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('2017-Gr1.jpg')

print(np.shape(img))

### Cut image in half
ba = img[110:160,150:450]
s = img[280:400,140:500]



#### image beta actin
plt.imshow(ba)
plt.plot([60,60],[0,50])
plt.plot([108,108],[0,50])
plt.plot([151,151],[0,50])
plt.plot([200,200],[0,50])
plt.plot([250,250],[0,50])
plt.show()

temp = ba.sum(axis=0)
ind = [0,60,108,151,200,250,len(temp)]
bactin = np.zeros(6)

for i in range(6):
    bactin[i] = sum(temp[ind[i]:ind[i+1]])

bactin = bactin/max(bactin)



#### image Dose
plt.imshow(s)
plt.plot([64,64],[0,100])
plt.plot([109,109],[0,100])
plt.plot([166,166],[0,100])
plt.plot([203,203],[0,100])
plt.plot([264,264],[0,100])
plt.plot([300,300],[0,100])
plt.show()

temp = s.sum(axis=0)
ind = [0,64,109,166,203,300,len(temp)]
dose = np.zeros(6)

for i in range(6):
    dose[i] = sum(temp[ind[i]:ind[i+1]])
    
dose = dose/max(dose)


##### Normalising
norm = dose/bactin
adjust = bactin
adjust[4] = 1.1
normadjusted = dose/adjust
plt.plot(np.linspace(0,2.5,6),normadjusted,'--o', color="orange",label='Adjusted bactin')
plt.plot(np.linspace(0,2.5,6),norm,'o-',label='Original plot')
plt.xlabel('Dose [Gy]')
plt.ylabel('Antall p53 proteiner [arb.unit]')
plt.legend()
plt.title('Antall p53 proteiner ved gitt dose')
plt.show()
