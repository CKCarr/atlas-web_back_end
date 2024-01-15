import base64

def encode_base64(input_string):
    print('Given this string:\n', input_string)
    input_bytes = input_string.encode('utf-8')  # Convert string to bytes
    print('We encode with utf-8 and receive\n', input_bytes)
    base64_bytes = base64.b64encode(input_bytes)  # Encode bytes to Base64
    print('Following that we have now added the layer of encoding with b64 and now receive\n', base64_bytes)
    print('Now we have encoded our sting twice with utf-8 and b64. We can now decode the utf-8 and receive\n', base64_bytes.decode('utf-8'))
    return base64_bytes.decode('utf-8')  # Convert bytes back to string


encoded_string = encode_base64('Hello World')
print(encoded_string)
