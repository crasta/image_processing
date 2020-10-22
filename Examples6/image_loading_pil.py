from PIL import Image
import requests
from io import BytesIO


if __name__=="__main__":
	url0 = 'https://cdn.shopify.com/s/files/1/0229/8055/8912/products/HTB1NE0qQXXXXXXjXpXXq6xXFXXXk_1024x1024@2x.jpg?v=1571715992'
	response0 = requests.get(url0)
	image0 = Image.open(BytesIO(response0.content))

	# Output Images
	#image0.show()

	# prints format of image
	print(image0.format)
	# prints mode of image
	print(image0.mode)
	# Image size, in pixels. The size is given as a 2-tuple (width, height).
	print(image0.size) # Output: (1200, 776)
	# Colour palette table, if any.
	print(image0.palette) # Output: None

	resized_image0 = image0.resize((400, 400))
	#resized_image0.show('Resized image')

	box = (150, 150, 325, 300)
	cropped_image0 = resized_image0.crop(box)
	#cropped_image0.show(title="Cropped image")

	#image0.rotate(90).show()
	resized_image0.rotate(18, expand=True).show()

	greyscale_image0 = resized_image0.convert('L')
	greyscale_image0.show()
