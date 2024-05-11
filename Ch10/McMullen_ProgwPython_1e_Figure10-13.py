try:
    # Code that might raise
    # exceptions somewhere...
except RuntimeError:
    print("A runtime error happened.")
except AttributeError:
    print("An attribute error happened.")
except:
    print("Any other exception ends up here.")
