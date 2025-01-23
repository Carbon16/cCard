from mfrc522 import SimpleMFRC522
reader=SimpleMFRC522()
id=reader.read()
# extract the id from the tuple
print(id[0])