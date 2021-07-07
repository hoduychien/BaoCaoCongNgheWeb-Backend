from flask import Flask, request, jsonify
from flask_cors import CORS
import staff as st
import product as prod
import customer as cus
import bill as Bills


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


# PRODUCT
@app.route('/api/product', methods=['GET'])
def api_get_products():
    return jsonify(prod.get_product())

@app.route('/api/product/<product_id>', methods=['GET'])
def api_get_product(product_id):
    return jsonify(prod.get_product_by_id(product_id))

@app.route('/api/product/add',  methods = ['POST'])
def api_add_product():
    product = request.get_json()
    return jsonify(prod.insert_product(product))

@app.route('/api/product/update',  methods = ['POST'])
def api_update_product():
    product = request.get_json()
    return jsonify(prod.update_product(product))

@app.route('/api/product/delete/<product_id>',  methods = ['DELETE'])
def api_delete_product(product_id):
    return jsonify(prod.delete_product(product_id))



# STAFF
@app.route('/api/staff', methods=['GET'])
def api_get_staffs():
    return jsonify(st.get_staff())
@app.route('/api/staff/<staff_id>', methods=['GET'])
def api_get_staff(staff_id):
    return jsonify(st.get_staff_by_id(staff_id))

@app.route('/api/staff/add',  methods = ['POST'])
def api_add_staff():
    staff = request.get_json()
    return jsonify(st.insert_staff(staff))

@app.route('/api/staff/update',  methods = ['PUT'])
def api_update_staff():
    staff = request.get_json()
    return jsonify(st.update_staff(staff))

@app.route('/api/staff/delete/<staff_id>',  methods = ['DELETE'])
def api_delete_staff(staff_id):
    return jsonify(st.delete_staff(staff_id))


# CUSTOMER
@app.route('/api/customer', methods=['GET'])
def api_get_customers():
    return jsonify(cus.get_customer())

@app.route('/api/customer/<customer_id>', methods=['GET'])
def api_get_customer(customer_id):
    return jsonify(cus.get_customer_by_id(customer_id))

@app.route('/api/customer/add',  methods = ['POST'])
def api_add_customer():
    customer = request.get_json()
    return jsonify(cus.insert_customer(customer))

@app.route('/api/customer/update',  methods = ['PUT'])
def api_update_customer():
    customer = request.get_json()
    return jsonify(cus.update_customer(customer))

@app.route('/api/customer/delete/<customer_id>',  methods = ['DELETE'])
def api_delete_customer(customer_id):
    return jsonify(cus.delete_customer(customer_id))

# BILL
@app.route('/api/bill', methods=['GET'])
def api_get_bills():
    return jsonify(Bills.get_bill())

@app.route('/api/bill/<bill_id>', methods=['GET'])
def api_get_bill(bill_id):
    return jsonify(Bills.get_bill_by_id(bill_id))

@app.route('/api/bill/add',  methods = ['POST'])
def api_add_bill():
    bill = request.get_json()
    return jsonify(Bills.insert_bill(bill))

@app.route('/api/bill/update',  methods = ['PUT'])
def api_update_bill():
    bill = request.get_json()
    return jsonify(Bills.update_bill(bill))

@app.route('/api/bill/delete/<bill_id>',  methods = ['DELETE'])
def api_delete_bill(bill_id):
    return jsonify(Bills.delete_bill(bill_id))


if __name__ == "__main__":
    app.run()