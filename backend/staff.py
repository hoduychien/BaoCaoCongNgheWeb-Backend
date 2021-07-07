import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

def connect_to_db():
    conn = sqlite3.connect('csdl.db')
    return conn

def get_staff():
    staffs = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM nhanvien")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            staff = {}
            staff["id"] = i["id"]
            staff["hotennv"] = i["hotennv"]
            staff["gioitinh"] = i["gioitinh"]
            staff["ngaysinh"] = i["ngaysinh"]
            staff["diachi"] = i["diachi"]
            staff["sdt_nhanvien"] = i["sdt_nhanvien"]
            staffs.append(staff)

    except:
        staffs = []

    return staffs

def insert_staff(staff):
    inserted_staff = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO nhanvien (hotennv, gioitinh, ngaysinh, diachi, sdt_nhanvien ) VALUES (?, ?, ?, ?, ?)",
                    (staff['hotennv'], staff['gioitinh'], staff['ngaysinh'], staff['diachi'], staff['sdt_nhanvien']))
        conn.commit()
        inserted_staff = get_staff_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_staff

def update_staff(staff):
    updated_staff = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE nhanvien SET hotennv = ?, gioitinh = ?, ngaysinh = ?, diachi = ?, sdt_nhanvien = ? "
                    "WHERE id =?",
                    (staff["hotennv"], staff["gioitinh"],staff["ngaysinh"], staff["diachi"], staff["sdt_nhanvien"],
                     staff["id"],))
        conn.commit()
        #return the user
        updated_staff = get_staff_by_id(staff["id"])

    except:
        conn.rollback()
        updated_staff = {}
    finally:
        conn.close()

    return updated_staff

def delete_staff(staff_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from nhanvien WHERE id = ?", (staff_id,))
        conn.commit()
        message["status"] = "Staff deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete staff"
    finally:
        conn.close()

    return message

def get_staff_by_id(staff_id):
    staff = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM nhanvien WHERE id = ?", (staff_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        staff["hotennv"] = row["hotennv"]
        staff["gioitinh"] = row["gioitinh"]
        staff["ngaysinh"] = row["ngaysinh"]
        staff["diachi"] = row["diachi"]
        staff["sdt_nhanvien"] = row["sdt_nhanvien"]
    except:
        staff = {}

    return staff