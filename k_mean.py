import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('C:/Users/Vedant Deshmukh/Downloads/sample.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # OpenCV loads images in BGR, convert to RGB

# Flatten the image into a 2D array of pixels
pixels = image.reshape((-1, 3))

# Specify the number of clusters (K)
k = 4

# Perform K-means clustering
kmeans = KMeans(n_clusters=k)
kmeans.fit(pixels)

# Get cluster labels and reshape them back to the original image shape
labels = kmeans.labels_.reshape(image.shape[:2])

# Create segmented image using the cluster centroids as colors
segmented_image = np.zeros_like(image)
for i in range(k):
    segmented_image[labels == i] = kmeans.cluster_centers_[i]

# Display the original and segmented images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(segmented_image)
plt.title(f'Segmented Image (K={k})')
plt.axis('off')

plt.show()
