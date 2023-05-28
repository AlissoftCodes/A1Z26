# A1Z26
This is a simple Python module to encode or decode messages using the A1Z26 cipher.

# Usage:
from a1z26 import *

message = 'Hello, world!'
encoded_message = text_to_a1z26(message)
print(encoded_message)

[output]
>>>8-5-12-12-15, 23-15-18-12-4!

hidden_message = '8-5-12-12-15, 23-15-18-12-4!'
decoded_message = a1z26_to_text(hidden_message)
print(decoded_message)

[output]
>>>HELLO, WORLD!
