from mfrc522 import SimpleMFRC522
reader=SimpleMFRC522()
try:
    id = reader.read_id()
    print(id)
finally:
    pass
