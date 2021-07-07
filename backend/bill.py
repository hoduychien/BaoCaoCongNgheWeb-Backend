import sqlite3

def connect_to_db():
    conn = sqlite3.connect('csdl.db')
    return conn


def get_bill():
    bills = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM hoadon INNER JOIN nhanvien ON hoadon.id_nhanvien=nhanvien.id "
                    "INNER JOIN sanpham ON sanpham.id=hoadon.id_sanpham "
                    "INNER JOIN khachhang ON khachhang.id=hoadon.id_khachhang")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            bill = {}
            bill["id"] = i["id"]
            bill["ngaylap"] = i["ngaylap"]
            bill["ngaynhan"] = i["ngaynhan"]
            bill["soluong"] = i["soluong"]
            bill["hotennv"] = i["hotennv"]
            bill["tensp"] = i["tensp"]
            bill["ten_khachhang"] = i["ten"]
            bills.append(bill)

    except:
        bills = []

    return bills

def insert_bill(bill):
    inserted_bill = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO hoadon (id_khachhang,id_sanpham, id_nhanvien, ngaylap, ngaynhan,soluong) VALUES (?, ?, ?, ?, ?, ?)",
                    (bill['id_khachhang'], bill['id_sanpham'], bill['id_nhanvien'],bill['ngaylap'],bill['ngaynhan'],bill['soluong']))
        conn.commit()
        inserted_bill = get_bill_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_bill

def update_bill(bill):
    updated_bill = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE hoadon SET id_khachhang = ?, id_sanpham = ?, id_nhanvien = ?, ngaylap = ?, ngaynhan = ?, soluong = ? WHERE id =?",
                   (bill["id_khachhang"], bill["id_sanpham"], bill["id_nhanvien"], bill["ngaylap"], bill["ngaynhan"],bill["soluong"], bill["id"],))
        conn.commit()
        #return the user
        updated_bill = get_bill_by_id(bill["id"])

    except:
        conn.rollback()
        updated_bill = {}
    finally:
        conn.close()

    return updated_bill

def delete_bill(bill_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from hoadon WHERE id = ?", (bill_id,))
        conn.commit()
        message["status"] = "Bill deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete bill"
    finally:
        conn.close()

    return message

def get_bill_by_id(bill_id):
    bill = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM hoadon INNER JOIN nhanvien ON hoadon.id_nhanvien=nhanvien.id"
                    " INNER JOIN sanpham ON sanpham.id=hoadon.id_sanpham "
                    "INNER JOIN khachhang ON khachhang.id=hoadon.id_khachhang WHERE hoadon.id = ?", (bill_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        bill["ngaylap"] = row["ngaylap"]
        bill["ngaynhan"] = row["ngaynhan"]
        bill["soluong"] = row["soluong"]
        bill["hotennv"] = row["hotennv"]
        bill["tensp"] = row["tensp"]
        bill["ten_khachhang"] = row["ten"]
    except:
        bill = {}

    return bill
