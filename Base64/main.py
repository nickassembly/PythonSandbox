# 1 byte = 8 bits
# 10011011 = 8 bits = 1 byte
# 10110110 01100011 00001100 = 3*8 bits = 3 bytes
# Base 64 encodes binary data and turns it into text data

import base64

my_text = "Hello World"

my_text = my_text.encode("ascii")
my_text_b64 = base64.b64encode(my_text)

# print(my_text_b64)

# print(base64.b64decode(my_text_b64))

# Base 64 is not encryption, it is encoding

with open("image.jpg", "rb") as f:
    data = f.read()

print(base64.b64encode(data))

data = base64.b64encode(data)  # encode

data = base64.b64decode(data)  # decode

with open("copy_of_image.jpg", "wb") as f:
    f.write(data)
