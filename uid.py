from mfrc522 import SimpleMFRC522
reader=SimpleMFRC522()
try:
    id = reader.read_id()
    # remove any leading/trailing whitespace
    id = id.strip()
    print(id)
finally:
    pass
