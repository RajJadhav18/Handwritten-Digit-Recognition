from PIL import Image

# Load the image file
image = Image.open('rename.png')

# Loop 90 times and save each copy with a new filename
for i in range(5):
    # Create a new copy of the image
    copy = image.copy()
    # Save the copy with a new filename
    copy.save(f'{i}.jpg')
