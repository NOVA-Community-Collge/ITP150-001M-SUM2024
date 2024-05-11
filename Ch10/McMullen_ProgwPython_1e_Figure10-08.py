from PIL import Image
cat_image = None
try:
    cat_image = Image.open("cat.png")
    cat_image.show()
except FileNotFoundError:
    print("Could not find the cat picture file.")
    