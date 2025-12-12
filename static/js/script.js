// Function to duplicate an image
function duplicateImage(imageId) {
    const originalImage = document.getElementById(imageId);
    if (originalImage) {
        const clonedImage = originalImage.cloneNode(true);
        clonedImage.id = imageId + '-copy'; // Assign a new ID to the cloned image
        originalImage.parentNode.appendChild(clonedImage); // Append the cloned image to the same parent
    } else {
        console.error('Image not found');
    }
}

// Example usage: Call this function with the ID of the image you want to duplicate
duplicateImage('apple'); // Replace 'myImageId' with the actual ID of your image