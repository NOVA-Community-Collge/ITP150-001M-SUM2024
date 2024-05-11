from PIL import Image, UnidentifiedImageError
cat_image = None
try:
    cat_image = Image.open("cat.png")
    cat_image.show()
except FileNotFoundError:
    print("Could not find the cat picture file.")
except UnidentifiedImageError:
    print("Could not identify the picture format.")