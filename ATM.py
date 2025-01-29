from mfrc522 import SimpleMFRC522
reader=SimpleMFRC522()
import mariadb
import sys
try:
    conn = mariadb.connect(
        user="sking",
        password="Tritium1769",
        host="localhost",
        database="poker"
)
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
# create database
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (name VARCHAR(255), uid INT, credit INT)")

# Get Cursor
cur = conn.cursor()

def read_uid():
    return reader.read_id()

def main():
    print("Select an option:\n1. Register\n2. Withdraw\n3. Deposit\n4. Check Balance")
    option = input("Enter option: ")

def register():
    name = input("Enter name: ")
    print("Present card")
    uid = read_uid()
    cur.execute("INSERT INTO users (name, uid) VALUES (?, ?)", (name, uid))
    conn.commit()
    print("User registered")

def withdraw():
    print("Present card")
    uid = read_uid()
    amount = input("Enter amount to withdraw: ")
    cur.execute("SELECT credit FROM users WHERE uid=?", (uid,))
    credit = cur.fetchone()[0]
    cur.execute("UPDATE users SET credit=? WHERE uid=?", (credit-int(amount), uid))
    conn.commit()
    print(amount + " withdrawn")

def deposit():
    print("Present card")
    uid = read_uid()
    amount = input("Enter amount to deposit: ")
    cur.execute("SELECT credit FROM users WHERE uid=?", (uid,))
    credit = cur.fetchone()[0]
    cur.execute("UPDATE users SET credit=? WHERE uid=?", (credit+int(amount), uid))
    conn.commit()
    print(amount + " deposited")

def check_balance():
    print("Present card")
    uid = read_uid()
    cur.execute("SELECT credit FROM users WHERE uid=?", (uid,))
    credit = cur.fetchone()[0]
    print("Balance: " + str(credit))