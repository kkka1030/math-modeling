import matplotlib.pyplot as plt  
  
# Initialize lists to store steps, losses and accuracies  
steps = []  
losses = []  
accuracies = []  
  
# Open and read the file  
with open('result.txt', 'r') as file:  
    for line in file:  
        # Split the line into components  
        components = line.split('\t')  
          
        # Append the step, loss, and accuracy to the respective lists  
        steps.append(int(components[0].split()[1]))  
        losses.append(float(components[1].split(':')[1]))  
        accuracies.append(float(components[2].split(':')[1]))  
  
# Create a new figure for the plots  
plt.figure(figsize=(12, 6))  
  
# Plot the average loss per step  
plt.subplot(1, 2, 1)  
plt.plot(steps, losses, label='Average Loss')  
plt.xlabel('Step')  
plt.ylabel('Average Loss')  
plt.title('Average Loss per Step')  
plt.grid(True)  
  
# Plot the accuracy per step  
plt.subplot(1, 2, 2)  
plt.plot(steps, accuracies, label='Accuracy', color='orange')  
plt.xlabel('Step')  
plt.ylabel('Accuracy')  
plt.title('Accuracy per Step')  
plt.grid(True)  
  
# Show the plots  
plt.tight_layout()  
plt.show()  