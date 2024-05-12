from PIL import Image
cat_image = None
try:
    cat_image = Image.open("cat.png")
except:
    print("Could not display a cat picture.")
cat_image.show()