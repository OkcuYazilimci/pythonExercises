import matplotlib.pyplot as plt
x = [0]
y = [0]
for i in range(0,500):
    stress = (700+900*((i/10000)**0.21))
    x.append(stress)
    i = i + 1
    if i == 500:
        stress = 1100
        x.append(stress)
print(x[100]) # K = 900

for i in range (0,500):
    strain = i/10000
    y.append(strain)
    i = i+1
    if i == 500:
        strain = 0.05001
        y.append(strain)

   # strain = (700/350000) + (700/900)**0.21

plt.plot(y,x)
print(strain)
plt.show()

#Stress = 700 * strain