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
ind = [0,64,109,166,203,264,300,len(temp)]
dose = np.zeros(6)

for i in range(7):
    if(i == 5):
        dose[i] = sum(temp[ind[i+1]:ind[i+2]])
        break;
    dose[i] = sum(temp[ind[i]:ind[i+1]])
    
dose = dose/max(dose)


##### Normalising
norm = dose/bactin
adjust = dose


print(bactin)
print(adjust)
normadjusted = adjust/bactin
#plt.plot(np.linspace(0,2.5,6),normadjusted,'--o', color="orange",label='Adjusted bactin')
plt.plot(np.linspace(0,2.5,6),norm,'o--')
plt.xlabel('Dose $[Gy]$',fontsize = 14)
plt.ylabel('chemiluminescence intensitet', fontsize = 14)
plt.title('Antall p53 proteiner ved gitt dose', fontsize = 16, fontweight="bold", y=1.08)
plt.show()

image = img/max(img.max(1))
plt.imshow(image)
plt.xlabel('x [Piksel]',fontsize = 14)
plt.ylabel('y [Piksel]',fontsize = 14)
plt.title('Chemiluminescence bildet fra detektor', fontsize = 16, fontweight="bold", y=1.08)
plt.colorbar()

plt.show()