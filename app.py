import email

from flask import Flask, render_template, request, redirect

import sqlite3

app = Flask(__name__)

connection= sqlite3.connect("mitambozfull.db", check_same_thread=False)
cursor=connection.cursor()
#cursor.execute('CREATE TABLE members (name VARCHAR(25), email VARCHAR(50) PRIMARY KEY, password VARCHAR (12) )')
#cursor.execute('INSERT INTO members(name,email,password) VALUES("saruni","mark@manenoz.com","babylulus")')
#cursor.execute('CREATE TABLE customers (fname VARCHAR(25), lname VARCHAR(25), cust_id VARCHAR(50) PRIMARY KEY, email VARCHAR(25), contact VARCHAR(25),address VARCHAR (25) )')
#cursor.execute('CREATE TABLE admin (admin_id VARCHAR(50) PRIMARY KEY,fname VARCHAR(25), lname VARCHAR(25),  email VARCHAR(25), contact VARCHAR(25),address VARCHAR (25) )')
#cursor.execute('INSERT INTO admin(admin_id,fname,lname,email,contact,address) VALUES("1","mark","saruni","mark@manenoz.com","0702328682","Kitengela")')
#cursor.execute('INSERT INTO admin(admin_id,fname,lname,email,contact,address) VALUES("2","shaleen","wanjiku","shaleen@manenoz.com","0702328682","Roysambu")')
#cursor.execute('CREATE TABLE products (prod_id VARCHAR(50) PRIMARY KEY,name VARCHAR(25), quantity VARCHAR(25),  price VARCHAR(25))')
#cursor.execute('CREATE TABLE orders (order_id VARCHAR(50) PRIMARY KEY,courcontact VARCHAR(25), amount VARCHAR (25) )')
#cursor.execute('CREATE TABLE sadmins (name VARCHAR(25), email VARCHAR(50) PRIMARY KEY, password VARCHAR (12) )')
#cursor.execute('INSERT INTO sadmins(name,email,password) VALUES("saruni","mark@mitamboz.com","babylulus")')
#cursor.execute('INSERT INTO sadmins(name,email,password) VALUES("oscar","oscar@mitamboz.com","babylulus")')
connection.commit()

@app.route("/")
def account():
    return render_template("login.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/customers")
def customers():
    cursor.execute('SELECT * FROM customers')
    customers = cursor.fetchall()
    return render_template("customers.html", customers=customers)

@app.route("/orders")
def orders():
    return render_template("orders.html")

@app.route("/inventory")
def inventory():
    return render_template("inventory.html")

@app.route("/staff")
def staff():
    cursor.execute('SELECT * FROM admin')
    admin = cursor.fetchall()
    return render_template("staff.html", admin=admin)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/register")
def register():
    return render_template("register.html")
@app.route("/dell")
def dell():
    return render_template("dell.html")
@app.route("/hp")
def hp():
    return render_template("hp.html")
@app.route("/asus")
def asus():
    return render_template("asus.html")
@app.route("/macbook")
def macbook():
    return render_template("macbook.html")
@app.route("/cart")
def cart():
    return render_template("cart.html")
@app.route("/panasonic")
def panasonic():
    return render_template("panasonic.html")
@app.route("/sonyalpha")
def sonyalpha():
    return render_template("sonyalpha.html")
@app.route("/nikon")
def nikon():
    return render_template("nikon.html")
@app.route("/canon")
def canon():
    return render_template("canon.html")
@app.route("/redmi")
def redmi():
    return render_template("redmi.html")
@app.route("/iphone")
def iphone():
    return render_template("iphone.html")
@app.route("/samsung")
def samsung():
    return render_template("samsung.html")
@app.route("/tcl")
def tcl():
    return render_template("tcl.html")

@app.route("/login_yesa",methods=["POST"])
def login_yesa():
    email=request.form.get("email")
    password=request.form.get("password")
    cursor.execute("""SELECT * FROM sadmins WHERE email LIKE '{}' AND password LIKE '{}' """.format(email, password))
    sadmins=cursor.fetchall()

    if len(sadmins)>0:

        return redirect('/dashboard')
    else:
        return render_template("admin.html")

@app.route("/login_yes",methods=["POST"])
def login_yes():
    email=request.form.get("email")
    password=request.form.get("password")
    cursor.execute("""SELECT * FROM members WHERE email LIKE '{}' AND password LIKE '{}' """.format(email, password))
    members=cursor.fetchall()

    if len(members)>0:

        return redirect('/home')
    else:
        return render_template("login.html")

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('signupname')
    email = request.form.get('signupemail')
    password = request.form.get('signuppassword')
    cursor.execute("""INSERT INTO members (name, email, password) VALUES ('{}','{}', '{}') """.format(name,email,password))
    connection.commit()
    return render_template('contact.html')


@app.route('/contact_yes', methods=['POST'])
def contact_yes():
    fname = request.form.get('firstname')
    lname = request.form.get('lastname')
    email = request.form.get('email')
    address = request.form.get('address')
    contact = request.form.get('contact')
    cursor.execute("""INSERT INTO customers (fname, lname, email, address, contact) VALUES ('{}','{}','{}','{}', '{}') """.format(fname,lname,email,address,contact))
    connection.commit()
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)