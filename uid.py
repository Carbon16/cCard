from mfrc522 import SimpleMFRC522
reader=SimpleMFRC522()
id=reader.read()
# extract only integers from the id
id = ''.join(filter(str.isdigit, id))