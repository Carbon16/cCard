from mfrc522 import SimpleMFRC522
reader=SimpleMFRC522()
id=reader.read()
print(id)