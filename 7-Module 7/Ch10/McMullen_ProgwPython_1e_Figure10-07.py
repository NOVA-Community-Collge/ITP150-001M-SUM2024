from PIL import Image
cat_image = None
try:
    cat_image = Image.open("cat.png")
    cat_image.show()
except:
    print("Could not display a cat picture.")
    