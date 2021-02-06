# Import Things
import base64

# Selctor
val = input("Would you like to encode(1) or decode(2) to or from base64:  ")

# Main code here
if (val == "1"):
    message = input("Insert your text here to encode to base64:  ")
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    print(base64_message)
    print("Above is your base 64 string.")
    input("")
elif (val == "2"):
    base64_message = input("Type in your base64 string:  ")
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')

    print(message)
    print("The message has been decoded successfully!")
    input("")
else:
    print("There are only 2 options, 1 or 2")
    input("")