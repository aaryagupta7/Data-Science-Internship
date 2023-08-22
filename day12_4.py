from PIL import Image, ImageFilter

#Open an image using pillow
image_path = "panda.jpg"
original_image = Image.open(image_path)

#Display some information about the image 
print("Original Image Format:", original_image.format)
print("Original Image Size:", original_image.size)

#Apply a Gaussian Blur filter
blurred_image = original_image.filter(ImageFilter.GaussianBlur(radius=2))

#Save the modified image 
output_path = "panda.jpg"
blurred_image.save(output_path)

#Display a message
print("Image is processed and saved to:",output_path)