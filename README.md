# butterflies
OCR on butterfly catalogs using tesseract and python

Need to install tesseract. On Mac this worked by following these instructions using Mac ports

http://emop.tamu.edu/Installing-Tesseract-Mac

And setting this environment variable

export TESSDATA_PREFIX=/opt/local/share

Download and install pytesseract and test it in python
(also requires PIL)

import Image
from pytesseract import image_to_string
print image_to_string(Image.open('test.png'))

This code is copywrited by David Johnston of ThoughtWorks
the image data include is not under copywrite of David Johnston
