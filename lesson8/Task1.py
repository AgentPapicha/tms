original_bite_string = b'r\xc3\xa9sum\xc3\xa9'
print('Original bite string: ', original_bite_string)
decoded_string = original_bite_string.decode("utf-8")
print('Decoded string: ', decoded_string)
encoded_string = decoded_string.encode("Latin1")
print('Encoded to Latin1 string: ', encoded_string)
decoded_latin__string = encoded_string.decode("Latin1")
print('Decoded from Latin1 string: ', decoded_latin__string)
