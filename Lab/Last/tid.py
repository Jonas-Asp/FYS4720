import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('2017-Gr2.jpg')

print(np.shape(img))

### Cut image in half
ba = img[60:130,185:490]
s = img[300:360,185:500]


ind = [0,53,104,151,201,253,490-185]
#### image beta actin
plt.imshow(ba)
plt.plot([ind[1],ind[1]],[0,50])
plt.plot([ind[2],ind[2]],[0,50])
plt.plot([ind[3],ind[3]],[0,50])
plt.plot([ind[4],ind[4]],[0,50])
plt.plot([ind[5],ind[5]],[0,50])
plt.show()

temp = ba.sum(axis=0)

bactin = np.zeros(6)

for i in range(6):
    bactin[i] = sum(temp[ind[i]:ind[i+1]])

bactin = bactin/max(bactin)


ind = [0,53,104,153,205,253,500-185]
#### image Dose
plt.imshow(s)
plt.plot([ind[1],ind[1]],[0,50])
plt.plot([ind[2],ind[2]],[0,50])
plt.plot([ind[3],ind[3]],[0,50])
plt.plot([ind[4],ind[4]],[0,50])
plt.plot([ind[5],ind[5]],[0,50])
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
adjust[4] = 1.5
normadjusted = dose/adjust
plt.plot(np.linspace(0,2.5,6),normadjusted,'--o', color="orange",label='Adjusted bactin')
plt.plot(np.linspace(0,2.5,6),norm,'o-',label='Original plot')
plt.xlabel('Tid [timer]')
plt.ylabel('Antall p53 proteiner [arb.unit]')
plt.legend()
plt.title('Antall p53 proteiner ved gitt dose')
plt.show()
