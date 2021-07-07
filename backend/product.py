import sqlite3

def connect_to_db():
    conn = sqlite3.connect('csdl.db')
    return conn


def get_product():
    products = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM sanpham")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            product = {}
            product["id"] = i["id"]
            product["tensp"] = i["tensp"]
            product["dongia"] = i["dongia"]

            products.append(product)

    except:
        products = []

    return products

def insert_product(product):
    inserted_product = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO sanpham (tensp, dongia) VALUES (?, ?)",
                    (product['tensp'], product['dongia']))
        conn.commit()
        inserted_product = get_product_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_product

def update_product(product):
    updated_product = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE sanpham SET tensp = ?, dongia = ? WHERE id =?",
                    (product["tensp"], product["dongia"],product["id"],))
        conn.commit()
        #return the user
        updated_product = get_product_by_id(product["id"])

    except:
        conn.rollback()
        updated_product = {}
    finally:
        conn.close()

    return updated_product

def delete_product(product_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from sanpham WHERE id = ?", (product_id,))
        conn.commit()
        message["status"] = "Product deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete product"
    finally:
        conn.close()

    return message

def get_product_by_id(product_id):
    product = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM sanpham WHERE sanpham.id = ?", (product_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        product["tensp"] = row["tensp"]
        product["dongia"] = row["dongia"]
    except:
        product = {}

    return product
