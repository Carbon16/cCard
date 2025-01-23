from mfrc522 import MFRC522

reader = MFRC522()
status =  None
(status, uid) = reader.Anticoll()
if status == reader.MI_OK:
	print(uid)