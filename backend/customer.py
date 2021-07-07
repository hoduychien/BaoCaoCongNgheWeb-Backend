import sqlite3

def connect_to_db():
    conn = sqlite3.connect('csdl.db')
    return conn


def get_customer():
    customers = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM khachhang")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            customer = {}
            customer["id"] = i["id"]
            customer["ten"] = i["ten"]
            customer["diachi"] = i["diachi"]
            customer["sdt"] = i["sdt"]

            customers.append(customer)

    except:
        customers = []

    return customers

def insert_customer(customer):
    inserted_customer = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO khachhang (ten, diachi, sdt) VALUES (?, ?, ?)",
                    (customer['ten'], customer['diachi'],customer['sdt']))
        conn.commit()
        inserted_customer = get_customer_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_customer

def update_customer(customer):
    updated_customer = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE khachhang SET ten = ?, diachi = ?, sdt = ? WHERE id =?",
                    (customer["ten"], customer["diachi"],customer["sdt"], customer["id"],))
        conn.commit()
        #return the user
        updated_customer = get_customer_by_id(customer["id"])

    except:
        conn.rollback()
        updated_customer = {}
    finally:
        conn.close()

    return updated_customer

def delete_customer(customer_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from khachhang WHERE id = ?", (customer_id,))
        conn.commit()
        message["status"] = "Customer deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete customer"
    finally:
        conn.close()

    return message

def get_customer_by_id(customer_id):
    customer = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM khachhang WHERE id = ?", (customer_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        customer["ten"] = row["ten"]
        customer["diachi"] = row["diachi"]
        customer["sdt"] = row["sdt"]
    except:
        customer = {}

    return customer
