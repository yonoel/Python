import pytesseract

class Handler:
    def __init__(self,img):
        self.img = img

    def recognize(self):
        return pytesseract.image_to_string(self.img)