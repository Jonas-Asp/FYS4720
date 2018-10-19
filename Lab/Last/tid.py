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
ind = [0,53,104,151,201,253,len(temp)]
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
ind = [0,53,104,153,205,253,300]
dose = np.zeros(6)

for i in range(6):
    dose[i] = sum(temp[ind[i]:ind[i+1]])
    
dose = dose/max(dose)


##### Normalising
print(dose)
print(bactin)
norm = dose/bactin
adjust = bactin
adjust[4] = 1.5
normadjusted = dose/adjust
#plt.plot(np.linspace(0,2.5,6),normadjusted,'--o', color="orange",label='Adjusted bactin')
plt.plot(np.linspace(0,2.5,6),norm,'o--')
plt.xlabel('Tid $[Timer]$',fontsize = 14)
plt.ylabel('chemiluminescence intensitet', fontsize = 14)
#plt.legend()
plt.title('Antall p53 proteiner 2 Gy okende inkuberingstid', fontsize = 16, fontweight="bold", y=1.08)
plt.show()

image = img/max(img.max(1))
plt.imshow(image)
plt.xlabel('x [Piksel]',fontsize = 14)
plt.ylabel('y [Piksel]',fontsize = 14)
plt.title('Chemiluminescence bildet fra detektor', fontsize = 16, fontweight="bold", y=1.08)
plt.colorbar()

plt.show()