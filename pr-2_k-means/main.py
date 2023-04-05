fig = plt.figure(figsize=(10, 7))
axis = fig.add_subplot()
for i in range(len(mass_elbow_value)):
    axis.scatter(mass_elbow_value[i], i + 1)
plt.axis([1, 10, 0, mass_elbow_value[0]])
axis.grid()
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], mass_elbow_value)
plt.show()
print(mass_elbow_value)
