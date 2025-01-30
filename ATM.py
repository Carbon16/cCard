from mfrc522 import SimpleMFRC522
reader=SimpleMFRC522()
import mariadb
import sys
from time import sleep
from RPLCD.i2c import CharLCD
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()
#replace "print" with "lcd.write_string" to display on LCD.


try:
    conn = mariadb.connect(
        user="sking",
        password="Tritium1769",
        host="localhost",
        database="poker"
)
except mariadb.Error as e:
    lcd.write_string(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
# create database
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (name VARCHAR(255), uid INT, credit INT)")

# Get Cursor
cur = conn.cursor()

def read_uid():
    return reader.read_id()

def main():
    lcd.clear()
    lcd.write_string("1:Reg | 2:Wit | 3:Dep | 4:Bal")
    option = input("Enter option: ")
    if option == "1":
        register()
    elif option == "2":
        withdraw()
    elif option == "3":
        deposit()
    elif option == "4":
        check_balance()
    else:
        lcd.write_string("Invalid option")

def register():
    lcd.clear()
    lcd.write_string("Enter name")
    name = input("Enter name: ")
    lcd.clear()
    lcd.write_string("Present card")
    uid = read_uid()
    print(uid)
    cur.execute("INSERT INTO users (name, uid, credit) VALUES (?, ?, ?)", (name, uid, 350))
    conn.commit()
    lcd.clear()
    lcd.write_string(name + " registered")
    sleep(3)

def withdraw():
    lcd.clear()
    lcd.write_string("Present card")
    uid = read_uid()
    amount = input("Enter amount to withdraw: ")
    cur.execute("SELECT credit FROM users WHERE uid=?", (uid,))
    credit = cur.fetchone()[0]
    cur.execute("UPDATE users SET credit=? WHERE uid=?", (credit-int(amount), uid))
    conn.commit()
    lcd.write_string(amount + " withdrawn")
    sleep(3)

def deposit():
    lcd.clear()
    lcd.write_string("Present card")
    uid = read_uid()
    amount = input("Enter amount to deposit: ")
    cur.execute("SELECT credit FROM users WHERE uid=?", (uid,))
    credit = cur.fetchone()[0]
    cur.execute("UPDATE users SET credit=? WHERE uid=?", (credit+int(amount), uid))
    conn.commit()
    lcd.clear()
    lcd.write_string(amount + " deposited")
    sleep(3)

def check_balance():
    lcd.clear()
    lcd.write_string("Present card")
    uid = read_uid()
    cur.execute("SELECT credit FROM users WHERE uid=?", (uid,))
    credit = cur.fetchone()[0]
    lcd.clear()
    lcd.write_string("Balance: " + str(credit))
    sleep(3)

while True:
    main()