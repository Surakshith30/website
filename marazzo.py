from flask import Flask, render_template, request, url_for, redirect, flash
from flask import *  
from flask import session
# from flask_sqlalchemy import SQLAlchemy
from forms import BillingForm, ShippingForm , PaymentForm
# from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user
# import update
import sqlite3
from datetime import datetime

import os
import psycopg2
import secrets

app = Flask(__name__)
app.secret_key = "wkfw"  
# app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"
# db = SQLAlchemy(app)
# login_manager = LoginManager(app)


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# class Billing(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     bfname = db.Column(db.String(20),  nullable=False)
#     blname = db.Column(db.String(20),  nullable=False)
#     billing_address = db.Column(db.String(50),  nullable=False)
#     bstate = db.Column(db.String(20), nullable=False)
#     bcity = db.Column(db.String(20), nullable=False)
#     bpincode = db.Column(db.Integer, nullable=False)
#     #carts = db.relationship('Cart', backref='shopper_cart',lazy = True)
#     def __repr__(self):
#         return f"Billing('{self.bfname}','{self.blname}')"

# class Shipping(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     sfname = db.Column(db.String(20),  nullable=False)
#     slname = db.Column(db.String(20),  nullable=False)
#     shipping_address = db.Column(db.String(50),  nullable=False)
#     fstate = db.Column(db.String(20), nullable=False)
#     fcity = db.Column(db.String(20), nullable=False)
#     fpincode = db.Column(db.Integer, nullable=False)
#     #carts = db.relationship('Cart', backref='shopper_cart',lazy = True)
#     def __repr__(self):
#         return f"Billing('{self.sfname}','{self.slname}')"

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     product_name=db.Column(db.String(30),nullable = False)
#     product_cost = db.Column(db.Integer, nullable = False)
#     product_quantity=db.Column(db.Integer, nullable = False)
#     #carts = db.relationship('Cart', backref='product_cart', lazy=True)
#     def __repr__(self):
#         return f"Product('{self.id}','{self.product_name}','{self.product_cost}','{self.product_quantity}')"

# class Cart(db.Model):
#    id = db.Column(db.Integer, primary_key = True)
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable = False)
# def __repr__(self):
#        return f"Cart('{self.id}','{self.user_id}','{self.product_id}')"


# add_to_cart = {1:3, #product_id : product_quantity
#         2:5}
# cart_details={'total_amt':0,
#               'products':0}
# temp_list = []

@app.route("/checkout", methods=['GET','POST'])
def checkout():
    form = BillingForm()
    # for key in add_to_cart.keys():
    #     result =db.session.query(Product).filter(Product.id==key)
    #     for r in result:
    #         temp = {'id': r.id, 'product_name': r.product_name, 'product_cost': r.product_cost,
    #                 'product_quantity': r.product_quantity, }
    #         temp_list.append(temp)
    # cart_details['products']=temp_list

    # print(cart_details['products'])
    # if form.validate_on_submit():
    #     bill = Billing(bfname = form.bfname.data, blname = form.blname.data, billing_address = form.billing_address.data,
    #                    bstate=form.bstate.data, bcity = form.bcity.data, bpincode = form.bpincode.data )
    #     db.session.add(bill)
    #     db.session.commit()
        # flash('success', 'success')
        # print("done")
    # return redirect(url_for('checkout'))
    # print(form.errors)
    return render_template("checkout.html" , form =form)


#@app.route("/checkout-shipping", methods=['GET','POST'])
#def shipping():
 #   form = ShippingForm()
  #  print(form.errors)
   # if form.validate_on_submit():
    #    flash('success', 'success')
     #   print("done")
      #  return redirect(url_for('payment'))
    #print(form.errors)
    #return render_template("checkout2.html", form=form)


#@app.route("/checkout-payment", methods=['GET','POST'])
#def payment():
 #   form = PaymentForm()
  #  print(form.errors)
   # if form.validate_on_submit():
    #    flash('success', 'success')
     #   print("done")
      #  return redirect(url_for('checkout'))
    #print(form.errors)
    #return render_template("checkout3.html", form=form)


# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('home'))

# def get_db_connection():
#     with sqlite3.connect('dbms.db') as conn:
#         cur = conn.cursor()
#     return conn
    
    
# @app.before_request
# def before_request_func():
#     print("before_request executing!")

#CSP PROCESS CHECKING FOR ADOBE
# Replace 'EDGE-DOMAIN' with your configured first-party domain or '*.adobedc.net'
# EDGE_DOMAIN = '*.adobedc.net'

# @app.after_request
# def add_csp(response):
#     csp_header = f"default-src 'self'; connect-src 'self' {EDGE_DOMAIN} *.demdex.net; script-src 'self' assets.adobedtm.com; "

#     # Add the CSP nonce if it exists in the response context
#     nonce = getattr(response, '_csp_nonce', None)
#     if nonce:
#         csp_header += f" script-src 'nonce-{nonce}'"

#     response.headers["Content-Security-Policy"] = csp_header
#     return response

# import random
# import string

# def generate_nonce(length=32):
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/')
# def index():
#     nonce = generate_nonce()
#     return render_template('home.html', nonce=nonce)

@app.route("/home")
def home():
    return render_template("home.html")

# @app.route('/home.html', methods=['POST'])
# def index():
#     if 'email' in session:
#         return redirect(url_for('logout'))
#     return redirect(url_for('login'))

@app.route("/sign-in.html")
def signin():
    return render_template("sign-in.html")

# @app.route("/login", methods=['POST'])
# def get_email():
#     return isp_query
@app.route("/login", methods=['GET','POST'])
def login():
    print("=======================================================================================")
    with sqlite3.connect('new_db.db') as conn:
        cur = conn.cursor()
        email_id= request.form["email_id"]
    #     em_id=email_id
        session['email_id']=email_id.lower()
        pwd = request.form["pwd"]
#         conn = get_db_connection()
        cur_in=conn.cursor()
        cur_pwd=conn.cursor()
#         cur = conn.cursor()
        cur_name=conn.cursor()
        cur_date=conn.cursor()
        cur_details=conn.cursor()
        cur_email=conn.cursor()
        cur_get_all=conn.cursor()
        current_email=conn.cursor()
        email_id=email_id.lower()
    #         global  params
        params = [email_id]
        pswd=[pwd]
        em_id=str(session['email_id'])

        # cursor return affected rows
        cur.execute('select count(email_id) from signup where email_id=?', params)# prevent SqlInject
#         print(count)
        cur_pwd.execute('select password from signup where email_id=?',params)
        cur_name.execute('select name from signup where email_id=?',params)
        cur_details.execute('select id from signup where email_id=?',params)
        cur_email.execute('select email_id from signup where email_id=?',params)
        cur_date.execute("SELECT datetime('now','localtime') as timestamps;")
#         date_time=cur_date.fetchone()
        date_time=cur_date.fetchone()
        datetime_object = datetime.strptime(date_time[0], '%Y-%m-%d %H:%M:%S')
        date_time=datetime_object.strftime("%Y-%m-%d, %H:%M:%S")
        get_id=cur_details.fetchone()
        get_email=cur_email.fetchone()
        name_get=cur_name.fetchone()
        print(get_id)
        count_pwd=cur_pwd.fetchone()
        count=cur.fetchone()
#         print(count[0])
    # if count[0] > 0 and count_pwd[0] == pwd:
    #     # Connect to the database
    #     with sqlite3.connect('new_db.db') as conn:
    #         cur = conn.cursor()
    #         cur.execute('SELECT product_id, price FROM add_to_cart WHERE email_id=?', params)
    #         rows = cur.fetchall()
            
    #         # Create a dictionary to store the items
    #         items = {}
    #         for row in rows:
    #             items[row[0]] = row[1]
                
    #         # Convert the dictionary to a JSON string
    #         items_json = json.dumps(items)

        if count[0] < 0:
            # count 0 email 
    #         redirect(url_for('addperson'))
            return redirect(url_for('signin'))
        elif count[0] < 0 or count_pwd[0]!=pwd:
            conn.commit()
            cur.close()
            #conn.close()
            return redirect(url_for('signin'))
        else:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            current_email.execute('select count(email_id) from signup where email_id=?',params)
            count_email_id=current_email.fetchone()

    with sqlite3.connect('new_db.db') as conn:
            cur = conn.cursor()
            current_email = session['email_id']
            if current_email:
                cur.execute('SELECT product_id, price, product_name, product_qty, product_image FROM add_to_cart WHERE email_id=?', [current_email])
                rows = cur.fetchall()
            
            # Create a dictionary to store the items
            items = {}
            for row in rows:
                items[row[0]] = {'product_id':row[0], 'product_name': row[2], 'product_image':row[4],'product_price':str(row[1]) , 'product_quantity': row[3]}
                
            # Store the items in a session variable
            session['cart'] = items

            if count_email_id[0]<1:
                cur_get_all.execute('insert into signin (id,email_id,last_visited,logout_time)'
                           'values(?,?,?,?)',(get_id[0],em_id,date_time,date_time))
                conn.commit()
                cur_get_all = conn.cursor()
                products = cur_get_all.fetchall()
    
#                 cur_get_all.close()
                #conn.close()
            else:
                cur_get_all.execute("update signin set last_visited='{0}' where email_id='{1}'".format(date_time,em_id))
                conn.commit()
#                 cur_get_all.close()
                #conn.close()
    #         logout_entry()
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    #         cur_in.execute('insert into signin (id,email_id,last_visited,logout_time)'
    #                    'values(%s,%s,%s,%s)',(get_id,get_email,date_time,date_time))
#             flash('Welcome'+" "+name_get[0].capitalize())
            flash(name_get[0],'category1')
            flash('Welcome'+" "+session['email_id'],'category2')
            return render_template('home.html',response=session['email_id'], clear_storage=True) # redirect(url_for('home'))
# @app.after_request
@app.route("/get_session")
def get_session():
    return jsonify({"email_id": session.get("email_id")})


@app.route("/cart", methods=['GET'])
def get_cart_data():
    # Retrieve the cart data from the session
    cart = session.get('cart', {})
    # Convert the cart data to a JSON object and return it
    return jsonify({'cart':cart})

def logout_entry():
#     if 'email_id' not in session:
#         return redirect(url_for('login'))
#         email_id =request.args.get("email_id")
#     global em_id
#     print(type(session['email_id']))
#     print('sdknkdnsds')
#     em_id=session.get('email_id')
#     print(email_id)
    with sqlite3.connect('new_db.db') as conn:
        cur = conn.cursor()
#         cur=conn.cursor()
        cur_date=conn.cursor()
        cur_details=conn.cursor()
        cur_email=conn.cursor()
        print(session['email_id'])
        em_id=str(session['email_id'])
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")    
    #     cur_details.execute('select id from signup where email_id={s}',em_id)
    #     cur_email.execute('select email_id from signup where email_id=%s',em_id)
    #     cur_date.execute("SELECT (current_timestamp AT TIME ZONE 'UTC'+'05:30') as timestamps;")
    #     date_time=cur_date.fetchone()
    #     get_id=cur_details.fetchone()
    #     get_email=cur_email.fetchone()
    #     cur.execute('update signin set logout_time=%s where email_id=%s',[date_time,em_id])
        cur_details.execute("select id from signup where email_id='{0}'".format(em_id))
        cur_email.execute("select email_id from signup where email_id='{0}'".format(em_id))
        cur_date.execute("SELECT datetime('now','localtime') as timestamps")
        date_time=cur_date.fetchone()
        get_id=cur_details.fetchone()
        get_email=cur_email.fetchone()
        datetime_object = datetime.strptime(date_time[0], '%Y-%m-%d %H:%M:%S')
        date_time=datetime_object.strftime("%Y-%m-%d, %H:%M:%S")
        cur.execute("update signin set logout_time='{0}'where email_id='{1}'".format(date_time,em_id))
        conn.commit()
        #conn.close()

#     return response

@app.route('/logout',methods=['GET','POST'])
def logout():
#     conn = get_db_connection()
#     cur=conn.cursor()
#     cur_date=conn.cursor()
#     cur_details=conn.cursor()
#     cur_email=conn.cursor()
#     if 'email_id' not in session:
#         return redirect(url_for('login'))
#         email_id =request.args.get("email_id")
#     global em_id
#     print(type(session['email_id']))
    
#     em_id=session.get('email_id')
#     print(em_id)
#     cur_details.execute('select id from signup where email_id=%s',em_id)
#     cur_email.execute('select email_id from signup where email_id=%s',em_id)
#     cur_date.execute("SELECT (current_timestamp AT TIME ZONE 'UTC'+'05:30') as timestamps;")
#     date_time=cur_date.fetchone()
#     get_id=cur_details.fetchone()
#     get_email=cur_email.fetchone()
#     cur.execute('update signin set logout_time=%s where email_id=%s',[date_time,q])
    print("*****************************************************************************")
    logout_entry()
    session.pop('email_id',None)
    return redirect(url_for('home'))

   
# @app.route('/home.html', methods=['POST'])
# def index():
#     login=False
#     if 'email' in session:
#         login=True
#         return render_template('home.html',login=login)

# @app.route("/addToCart")
# def addToCart():
#     if 'email_id' not in session:
#         return redirect(url_for('signin'))
#     else:
#         productId = int(request.args.get('productId'))
# #         with sqlite3.connect('dbms.db') as conn:
# #             cur = conn.cursor()
#             cur.execute("SELECT id FROM signin WHERE email_id = ?", (session['email_id'], ))
#             userId = cur.fetchone()[0]
#             try:
#                 cur.execute("INSERT INTO customer_cart (id,email_id,product_id) VALUES (?, ?)", (userId,email_id,productId))
#                 conn.commit()
#                 msg = "Added successfully"
#             except:
#                 conn.rollback()
#                 msg = "Error occured"
#         #conn.close()
#         return redirect(url_for('home'))
    
# @app.route("/shopping-cart.html")
# def cart():
#     #  email = "pratiksha@gmail.com"
#     # #  cur = conn.cursor()
#     #  params=[email]
#     #  cur.execute("SELECT email_id FROM signin WHERE email_id = %s",params)
#     #  email_Id = cur.fetchone()[0]
#     #  cur.execute("SELECT product_id,product_type,category,sub_category,product_name,price,label,rating,image,description = %s",email_Id)
#     #  products = cur.fetchall()
#     #  totalPrice = 0
#     #  for row in products:
#         #  totalPrice += row[2]
#      return render_template("shopping-cart.html")


@app.route("/create_account/", methods=['GET','POST'])
def create_account():
    with sqlite3.connect('new_db.db') as conn:
        cur = conn.cursor()
        email_id = request.form["email_id"]
        Name = request.form["Name"]
        Phone = request.form["Phone"]
        pwd = request.form["pwd"]
        cpwd = request.form["cpwd"]
#         conn = get_db_connection()
#         cur = conn.cursor()
        cur_date=conn.cursor()
        count_row=conn.cursor()
        params = [email_id]
        # cursor return affected rows
        count_row.execute('select count(*) from signup')
        cur.execute('select count(email_id) from signup where email_id=?', params)  # prevent SqlInject
    #     print(count)
        cur_date.execute("SELECT datetime('now','localtime') as timestamps;")
        ids=count_row.fetchone()
        ids=ids[0]+1
        # ids1=ids1[0]+1
        print(ids)
        date_time=cur_date.fetchone()
        datetime_object = datetime.strptime(date_time[0], '%Y-%m-%d %H:%M:%S')
        date_time=datetime_object.strftime("%Y-%m-%d, %H:%M:%S")
        count=cur.fetchone()
    #     print(count[0])
        if count[0] > 0:
            # count 0 email
            return redirect(url_for('signin'))
        else:
    #         cur.execute('select email_id from signin ')
            cur.execute('INSERT INTO signup (Id,email_id, name,phone_number,password,confirm_password,created_at,modified_at)'
                        'VALUES (?,?,?,?,?,?,?,?)',
                        (ids,email_id, Name,Phone,pwd,cpwd,date_time,date_time))

            # cur.execute(
            #     'INSERT INTO signin (email_id, last_visited, logout_time)'
            #     'VALUES (?, ?, ?)',
            #     (email_id, cur_date, cur_date)
            # )

            conn.commit()
            cur.close()
            #conn.close()
    return redirect(url_for('signin'))

# from flask import Flask, render_template, request, url_for, redirect, flash
# from flask import *  
# from flask_sqlalchemy import SQLAlchemy #HAQ needs to clarify
# from flask import session
# # #below updated by HAQ
# from forms import BillingForm, ShippingForm , PaymentForm
# from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user
# #Above updated by HAQ
# import os
# import psycopg2
# #Below updated by pratiksha
# import sqlite3
# from datetime import datetime

# # app = Flask(__name__)
# # app.secret_key = "abc"  

# # def get_db_connection():
# #     conn = psycopg2.connect(user="postgres",
# #                               password="password",
# #                               host="127.0.0.1",
# #                               port="5432",
# #                               database="marrazo")
# #     return conn
# app = Flask(__name__)
# app.secret_key = "wkfw"  
# app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///dbms.db"
# db = SQLAlchemy(app)
# login_manager = LoginManager(app)


# #BELOW CODE UPDATED BY HAQ Nizar Mohammed

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# class Billing(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     bfname = db.Column(db.String(20),  nullable=False)
#     blname = db.Column(db.String(20),  nullable=False)
#     billing_address = db.Column(db.String(50),  nullable=False)
#     bstate = db.Column(db.String(20), nullable=False)
#     bcity = db.Column(db.String(20), nullable=False)
#     bpincode = db.Column(db.Integer, nullable=False)
#     #carts = db.relationship('Cart', backref='shopper_cart',lazy = True)
#     def __repr__(self):
#         return f"Billing('{self.bfname}','{self.blname}')"

# class Shipping(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     sfname = db.Column(db.String(20),  nullable=False)
#     slname = db.Column(db.String(20),  nullable=False)
#     shipping_address = db.Column(db.String(50),  nullable=False)
#     fstate = db.Column(db.String(20), nullable=False)
#     fcity = db.Column(db.String(20), nullable=False)
#     fpincode = db.Column(db.Integer, nullable=False)
#     #carts = db.relationship('Cart', backref='shopper_cart',lazy = True)
#     def __repr__(self):
#         return f"Billing('{self.sfname}','{self.slname}')"

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     product_name=db.Column(db.String(30),nullable = False)
#     product_cost = db.Column(db.Integer, nullable = False)
#     product_quantity=db.Column(db.Integer, nullable = False)
#     #carts = db.relationship('Cart', backref='product_cart', lazy=True)
#     def __repr__(self):
#         return f"Product('{self.id}','{self.product_name}','{self.product_cost}','{self.product_quantity}')"

# class Cart(db.Model):
#    id = db.Column(db.Integer, primary_key = True)
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable = False)
# def __repr__(self):
#        return f"Cart('{self.id}','{self.user_id}','{self.product_id}')"

# add_to_cart = {1:3, #product_id : product_quantity
#         2:5}
# cart_details={'total_amt':0,
#               'products':0}
# temp_list = []

# @app.route("/checkout", methods=['GET','POST'])
# def checkout(add_to_cart=add_to_cart):
#     form = BillingForm()
#     for key in add_to_cart.keys():
#         result =db.session.query(Product).filter(Product.id==key)
#         for r in result:
#             temp = {'id': r.id, 'product_name': r.product_name, 'product_cost': r.product_cost,
#                     'product_quantity': r.product_quantity, }
#             temp_list.append(temp)
#     cart_details['products']=temp_list

#     print(cart_details['products'])
#     if form.validate_on_submit():
#         bill = Billing(bfname = form.bfname.data, blname = form.blname.data, billing_address = form.billing_address.data,
#                        bstate=form.bstate.data, bcity = form.bcity.data, bpincode = form.bpincode.data )
#         db.session.add(bill)
#         db.session.commit()
#         flash('success', 'success')
#         print("done")
#         return redirect(url_for('checkout'))
#     print(form.errors)
#     return render_template("checkout.html", form=form, cart_details= cart_details)
    

# #ABOVE CODE UPDATED BY HAQ Nizar Mohammed

# # @app.route('/logout')
# # def logout():
# #     logout_user()
# #     return redirect(url_for('home'))

# @app.route("/")

# @app.route("/home.html")
# def home():
#     return render_template("home.html")

# # @app.route('/home.html', methods=['POST'])
# # def index():
#     # if 'email' in session:
#         # return redirect(url_for('logout'))
#     # return redirect(url_for('login'))

# #BELOW CODE UPDATED FROM PRATIKSHA

# @app.route("/sign-in.html")
# def signin():
#     return render_template("sign-in.html")

# @app.route("/login", methods=['GET','POST'])
# def login():
#     print("=======================================================================================")
#     with sqlite3.connect('dbms.db') as conn:
#         cur = conn.cursor()
#         email_id= request.form["email_id"]
#     #     em_id=email_id
#         session['email_id']=email_id.lower()
#         pwd = request.form["pwd"]
# #         conn = get_db_connection()
#         cur_in=conn.cursor()
#         cur_pwd=conn.cursor()
# #         cur = conn.cursor()
#         cur_name=conn.cursor()
#         cur_date=conn.cursor()
#         cur_details=conn.cursor()
#         cur_email=conn.cursor()
#         cur_get_all=conn.cursor()
#         current_email=conn.cursor()
#         email_id=email_id.lower()
#     #         global  params
#         params = [email_id]
#         pswd=[pwd]
#         em_id=str(session['email_id'])

#         # cursor return affected rows
#         cur.execute('select count(email_id) from signup where email_id=?', params)# prevent SqlInject
# #         print(count)
#         cur_pwd.execute('select password from signup where email_id=?',params)
#         cur_name.execute('select name from signup where email_id=?',params)
#         cur_details.execute('select id from signup where email_id=?',params)
#         cur_email.execute('select email_id from signup where email_id=?',params)
#         cur_date.execute("SELECT datetime('now','localtime') as timestamps;")
# #         date_time=cur_date.fetchone()
#         date_time=cur_date.fetchone()
#         datetime_object = datetime.strptime(date_time[0], '%Y-%m-%d %H:%M:%S')
#         date_time=datetime_object.strftime("%Y-%m-%d, %H:%M:%S")
#         get_id=cur_details.fetchone()
#         get_email=cur_email.fetchone()
#         name_get=cur_name.fetchone()
#         print(get_id)
#         count_pwd=cur_pwd.fetchone()
#         count=cur.fetchone()
# #         print(count[0])
#         if count[0] < 0:
#             # count 0 email 
#     #         redirect(url_for('addperson'))
#             return redirect(url_for('signin'))
#         elif count[0] < 0 or count_pwd[0]!=pwd:
#             conn.commit()
#             cur.close()
#             #conn.close()
#             return redirect(url_for('signin'))
#         else:
#             print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#             current_email.execute('select count(email_id) from signin where email_id=?',params)
#             count_email_id=current_email.fetchone()
#             if count_email_id[0]<1:
#                 cur_get_all.execute('insert into signin (id,email_id,last_visited,logout_time)'
#                            'values(?,?,?,?)',(get_id[0],em_id,date_time,date_time))
#                 conn.commit()
# #                 cur_get_all.close()
#                 #conn.close()
#             else:
#                 cur_get_all.execute("update signin set last_visited='{0}' where email_id='{1}'".format(date_time,em_id))
#                 conn.commit()
# #                 cur_get_all.close()
#                 #conn.close()
#     #         logout_entry()
#             print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#     #         cur_in.execute('insert into signin (id,email_id,last_visited,logout_time)'
#     #                    'values(%s,%s,%s,%s)',(get_id,get_email,date_time,date_time))
# #             flash('Welcome'+" "+name_get[0].capitalize())
#             flash(name_get[0],'category1')
#             flash('Welcome'+" "+session['email_id'],'category2')
#         return render_template('home.html',response=session['email_id']) # redirect(url_for('home'))
    
# # @app.after_request

# def logout_entry():
# #     if 'email_id' not in session:
# #         return redirect(url_for('login'))
# #         email_id =request.args.get("email_id")
# #     global em_id
# #     print(type(session['email_id']))
# #     print('sdknkdnsds')
# #     em_id=session.get('email_id')
# #     print(email_id)
#     with sqlite3.connect('dbms.db') as conn:
#         cur = conn.cursor()
# #         cur=conn.cursor()
#         cur_date=conn.cursor()
#         cur_details=conn.cursor()
#         cur_email=conn.cursor()
#         print(session['email_id'])
#         em_id=str(session['email_id'])
#         print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")    
#     #     cur_details.execute('select id from signup where email_id={s}',em_id)
#     #     cur_email.execute('select email_id from signup where email_id=%s',em_id)
#     #     cur_date.execute("SELECT (current_timestamp AT TIME ZONE 'UTC'+'05:30') as timestamps;")
#     #     date_time=cur_date.fetchone()
#     #     get_id=cur_details.fetchone()
#     #     get_email=cur_email.fetchone()
#     #     cur.execute('update signin set logout_time=%s where email_id=%s',[date_time,em_id])
#         cur_details.execute("select id from signup where email_id='{0}'".format(em_id))
#         cur_email.execute("select email_id from signup where email_id='{0}'".format(em_id))
#         cur_date.execute("SELECT datetime('now','localtime') as timestamps")
#         date_time=cur_date.fetchone()
#         get_id=cur_details.fetchone()
#         get_email=cur_email.fetchone()
#         datetime_object = datetime.strptime(date_time[0], '%Y-%m-%d %H:%M:%S')
#         date_time=datetime_object.strftime("%Y-%m-%d, %H:%M:%S")
#         cur.execute("update signin set logout_time='{0}'where email_id='{1}'".format(date_time,em_id))
#         conn.commit()
#         #conn.close()

# #     return response

# @app.route('/logout',methods=['GET','POST'])
# def logout():
# #     conn = get_db_connection()
# #     cur=conn.cursor()
# #     cur_date=conn.cursor()
# #     cur_details=conn.cursor()
# #     cur_email=conn.cursor()
# #     if 'email_id' not in session:
# #         return redirect(url_for('login'))
# #         email_id =request.args.get("email_id")
# #     global em_id
# #     print(type(session['email_id']))
    
# #     em_id=session.get('email_id')
# #     print(em_id)
# #     cur_details.execute('select id from signup where email_id=%s',em_id)
# #     cur_email.execute('select email_id from signup where email_id=%s',em_id)
# #     cur_date.execute("SELECT (current_timestamp AT TIME ZONE 'UTC'+'05:30') as timestamps;")
# #     date_time=cur_date.fetchone()
# #     get_id=cur_details.fetchone()
# #     get_email=cur_email.fetchone()
# #     cur.execute('update signin set logout_time=%s where email_id=%s',[date_time,q])
#     print("*****************************************************************************")
#     logout_entry()
#     session.pop('email_id',None)
#     return redirect(url_for('home'))

   
# # @app.route('/home.html', methods=['POST'])
# # def index():
# #     login=False
# #     if 'email' in session:
# #         login=True
# #         return render_template('home.html',login=login)

# # @app.route("/addToCart")
# # def addToCart():
# #     if 'email_id' not in session:
# #         return redirect(url_for('signin'))
# #     else:
# #         productId = int(request.args.get('productId'))
# # #         with sqlite3.connect('dbms.db') as conn:
# # #             cur = conn.cursor()
# #             cur.execute("SELECT id FROM signin WHERE email_id = ?", (session['email_id'], ))
# #             userId = cur.fetchone()[0]
# #             try:
# #                 cur.execute("INSERT INTO customer_cart (id,email_id,product_id) VALUES (?, ?)", (userId,email_id,productId))
# #                 conn.commit()
# #                 msg = "Added successfully"
# #             except:
# #                 conn.rollback()
# #                 msg = "Error occured"
# #         #conn.close()
# #         return redirect(url_for('home'))
    
# # @app.route("/shopping-cart.html")
# # def cart():
# #     email = session['email_id']
# #     cur = conn.cursor()
# #     params=[email]
# #     cur.execute("SELECT email_id FROM signin WHERE email_id = %s",params)
# #     email_Id = cur.fetchone()[0]
# #     cur.execute("SELECT product_id,product_type,category,sub_category,product_name,price,label,rating,image,description = %s",email_Id)
# #     products = cur.fetchall()
# #     totalPrice = 0
# #     for row in products:
# #         totalPrice += row[2]
# #     return render_template("shopping-cart.html")


# @app.route("/create_account/", methods=['GET','POST'])
# def create_account():
#     with sqlite3.connect('dbms.db') as conn:
#         cur = conn.cursor()
#         email_id = request.form["email_id"]
#         Name = request.form["Name"]
#         Phone = request.form["Phone"]
#         pwd = request.form["pwd"]
#         cpwd = request.form["cpwd"]
# #         conn = get_db_connection()
# #         cur = conn.cursor()
#         cur_date=conn.cursor()
#         count_row=conn.cursor()
#         params = [email_id]
#         # cursor return affected rows
#         count_row.execute('select count(*) from signup')
#         cur.execute('select count(email_id) from signup where email_id=?', params)  # prevent SqlInject
#     #     print(count)
#         cur_date.execute("SELECT datetime('now','localtime') as timestamps;")
#         ids=count_row.fetchone()
#         ids=ids[0]+1
#         print(ids)
#         date_time=cur_date.fetchone()
#         datetime_object = datetime.strptime(date_time[0], '%Y-%m-%d %H:%M:%S')
#         date_time=datetime_object.strftime("%Y-%m-%d, %H:%M:%S")
#         count=cur.fetchone()
#     #     print(count[0])
#         if count[0] > 0:
#             # count 0 email
#             return redirect(url_for('signin'))
#         else:
#     #         cur.execute('select email_id from signin ')
#             cur.execute('INSERT INTO signup (Id,email_id, name,phone_number,password,confirm_password,created_at,modified_at)'
#                         'VALUES (?,?,?,?,?,?,?,?)',
#                         (ids,email_id, Name,Phone,pwd,cpwd,date_time,date_time))
#             conn.commit()
#             cur.close()
#             #conn.close()
#     return redirect(url_for('signin'))

# ABOVE CODE UPDATED FROM PRATIKSHA
# @app.route("/home.html")
# def home():
#     return render_template("home.html")
@app.route("/header.html")
def header():
    return render_template("header.html") 
    
@app.route("/shirts.html")
def shirts():
    return render_template("shirts.html") 
    
@app.route("/mens_shirt1-0001.html")
def mens_shirt1():
    return render_template("mens_shirt1-0001.html")      
    # return render_template("shopping-cart.html") 
         
@app.route("/mens_shirt2-0002.html")
def mens_shirt2():
    return render_template("mens_shirt2-0002.html")
    # return render_template("shopping-cart.html")  

@app.route("/mens_shirt3-0003.html")
def mens_shirt3():
    return render_template("mens_shirt3-0003.html")    

@app.route("/mens_shirt4-0004.html")
def mens_shirt4():
    return render_template("mens_shirt4-0004.html")    

@app.route("/mens_shirt5-0005.html")
def mens_shirt5():
    return render_template("mens_shirt5-0005.html")  

@app.route("/mens_shirt6-0006.html")
def mens_shirt6():
    return render_template("mens_shirt6-0006.html")

@app.route("/mens_shirt7-0007.html")
def mens_shirt7():
    return render_template("mens_shirt7-0007.html") 
    
@app.route("/mens_shirt8-0008.html")
def mens_shirt8():
    return render_template("mens_shirt8-0008.html") 

@app.route("/mens_shirt9-0009.html")
def mens_shirt9():
    return render_template("mens_shirt9-0009.html") 


@app.route("/mens_shirt10-0010.html")
def mens_shirt10():
    return render_template("mens_shirt10-0010.html")       
  
@app.route("/mens_shirt11-0011.html")
def mens_shirt11():
    return render_template("mens_shirt11-0011.html")
    
@app.route("/mens_shirt12-0012.html")
def mens_shirt12():
    return render_template("mens_shirt12-0012.html")
    
@app.route("/mens_shirt13-0013.html")
def mens_shirt13():
    return render_template("mens_shirt13-0013.html")

@app.route("/mens_shirt14-0014.html")
def mens_shirt14():
    return render_template("mens_shirt14-0014.html")  

@app.route("/mens_shirt15-0015.html")
def mens_shirt15():
    return render_template("mens_shirt15-0015.html")
    
@app.route("/mens_shirt16-0016.html")
def mens_shirt16():
    return render_template("mens_shirt16-0016.html")
    
  
@app.route("/shopping-cart.html")
def cart():
    #  with sqlite3.connect('new_db.db') as conn:
    #     cur_name=conn.cursor()
    #     params=[session['email_id'].lower()]
    #     em_id=str(session['email_id'])
    #     cur_name.execute("select name from signup where email_id='{0}'".format(em_id))
    #     name_get=cur_name.fetchone()
    #     flash(session['email_id'],'category1')
    #     flash(('Welcome'+" "+ name_get[0]),'category2')
        return render_template("shopping-cart.html")
@app.route("/orderConfirm",methods=['POST'])
def orderConfirm():
    with sqlite3.connect('new_db.db') as conn:
        ins_data = conn.cursor()
        confirm_order = conn.cursor()
        em_id=str(session['email_id'])
       
        billing_data = json.loads(request.json['Billing'])
        bfname =billing_data['first_name']
        blname =billing_data['last_name']
        baddress = billing_data['address']
        bcity = billing_data['city']
        bstate = billing_data['state']
        bpincode = billing_data['pincode']
        
        shipping_data = json.loads(request.json['Shipping'])
        sfname =shipping_data['first_name']
        slname =shipping_data['last_name']
        saddress = shipping_data['address']
        scity = shipping_data['city']
        sstate = shipping_data['state']
        spincode = shipping_data['pincode']


        payment_data = json.loads(request.json['Payment'])
        cardname = payment_data['name_card']
        cardno = payment_data['card_number']
        cvv = payment_data['CVV']
        date = payment_data['date']

        added_products = request.json['added_products']
        finalcart = added_products
        
        em_id=str(session['email_id'])
        totalPrice = request.json['total_price']
        
        ins_data.execute('INSERT INTO order_confirmation(email_id,cart,total_price,bfname,blname,billing_address,bcity,bstate,bpincode,sfname,slname,shipping_address,scity,sstate,spincode,card_number,card_name,cvv,expiry_date)'
        'values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', 
        (em_id,finalcart,totalPrice,bfname,blname,baddress,bcity,bstate,bpincode,sfname,slname,saddress,scity,sstate,spincode,cardno,cardname,cvv,date))

        conn.commit()

        cur = conn.cursor()
        cur.execute("select * from add_to_cart where email_id='{0}'".format(em_id))
        cart_items = cur.fetchall()
        if cart_items:
                # Perform the checkout process here
                # ...
                
                # Delete the products from the cart
                cur.execute("delete from add_to_cart where email_id='{0}'".format(em_id))
                conn.commit()
                
                return jsonify({'status': 'ok', 'message': "products checked out and removed from the cart"})
        else:
                return jsonify({'status': 'false', 'message': "No products in the cart"}) 


@app.route("/addProductToCart", methods=['POST'])
def addtoCart():
    with sqlite3.connect('new_db.db') as conn:
        cur = conn.cursor()
        ins_data=conn.cursor()
        check_id_if_exists=conn.cursor()
        update_cart=conn.cursor()
        
        if request.method == 'POST':
            added_products = request.values.get('added_products', False)
            if added_products:
                if isinstance(added_products, str):
                    added_products = json.loads(added_products)
                added_products = list(added_products.items())

                em_id=str(session['email_id'])
                cur.execute("select id from signup where email_id='{0}'".format(em_id))
                get_cust_id=cur.fetchone()
                
                # Add new products to cart or update existing ones
                for i in range(len(added_products)):
                    get_data=added_products[i][1]
                    prd_id=get_data['product_id']
                    prd_name=get_data['product_name']
                    prd_price=get_data['product_price']
                    prd_qty=get_data['product_quantity']
                    prd_img = get_data['product_image']
                    check_prd_id=conn.cursor()
                    check_prd_id.execute("select count(product_id) from add_to_cart where email_id='{0}' and product_id='{1}'".format(em_id, prd_id))
                    check_prd_id_count=check_prd_id.fetchone()
                    if check_prd_id_count[0]==0:
                        ins_data.execute('INSERT INTO add_to_cart(id,email_id,product_image,product_name,product_id,product_qty,price)'
                                'values(?,?,?,?,?,?,?)',
                                (get_cust_id[0],em_id,prd_img,prd_name,prd_id,prd_qty,prd_price))
                        conn.commit()
                    else:
                        update_cart.execute("update add_to_cart set product_qty='{0}',price=cast('{1}' as float) where email_id='{2}' and product_id='{3}' and product_image='{4}'  and product_name='{5}' ;".format(prd_qty,prd_price,em_id,prd_id,prd_img,prd_name))
                        conn.commit()
                
                # Remove products from cart if not present in new fetch
                cur.execute("select product_id from add_to_cart where email_id='{0}'".format(em_id))
                products_in_cart = cur.fetchall()
                products_in_cart = [p[0] for p in products_in_cart]
                for prd_id in products_in_cart:
                    if prd_id not in [prod[1]['product_id'] for prod in added_products]:
                        cur.execute("delete from add_to_cart where email_id='{0}' and product_id='{1}'".format(em_id, prd_id))
                        conn.commit()
                        
                return jsonify({'status': 'ok', 'message': "products added to the cart"})
            else:
                cur.execute("select count(*) from add_to_cart where email_id='{0}'".format(em_id))
                check_cart_count=cur.fetchone()
                if check_cart_count[0]==0:
                    return jsonify({'status': 'false', 'message': "No products in the cart"})
                else:
                    cur.execute("delete from add_to_cart where email_id='{0}'".format(em_id))
                    conn.commit()
                    return jsonify({'status': 'ok', 'message': "products removed from the cart"})
        return redirect(url_for('carts'))

@app.route("/confirmOrder", methods=['POST'])
def confirmOrder():
    with sqlite3.connect('new_db.db') as conn:
        cur = conn.cursor()

        if request.method == 'POST':
            em_id=str(session['email_id'])
            cur.execute("delete from add_to_cart where email_id='{0}'".format(em_id))
            conn.commit()

            return jsonify({'status': 'ok', 'message': "Order confirmed and items removed from the cart"})
        else:
            return jsonify({'status': 'false', 'message': "Failed to confirm order"})


    
  
  

@app.route("/Mens_shose.html")
def Mshose():
    return render_template("Mens_shose.html") 
    
    
@app.route("/woman_handbags.html")
def whandbags():
    return render_template("woman_handbags.html") 
 
@app.route("/toys.html")
def toys():
    return render_template("toys.html") 

@app.route("/toy1.html")
def toy1():
    return render_template("toy1.html")

@app.route("/mens_Shoes-0017.html")
def shose1():
    return render_template("mens_Shoes-0017.html")

@app.route("/mens_Shoes-0018.html")
def shose2():
    return render_template("mens_Shoes-0018.html")
    
@app.route("/mens_Shoes-0019.html")
def shose3():
    return render_template("mens_Shoes-0019.html")

@app.route("/mens_Shoes-0020.html")
def shose4():
    return render_template("mens_Shoes-0020.html")

@app.route("/mens_Shoes-0021.html")
def shose5():
    return render_template("mens_Shoes-0021.html")

@app.route("/mens_Shoes-0022.html")
def shose6():
    return render_template("mens_Shoes-0022.html")

@app.route("/mens_Shoes-0023.html")
def shose7():
    return render_template("mens_Shoes-0023.html")
    
@app.route("/mens_Shoes-0024.html")
def shose8():
    return render_template("mens_Shoes-0024.html")    
    
@app.route("/mens_Shoes-0025.html")
def shose9():
    return render_template("mens_Shoes-0025.html")
    
@app.route("/mens_Shoes-0026.html")
def shose10():
    return render_template("mens_Shoes-0026.html")
    
@app.route("/mens_Shoes-0027.html")
def shose11():
    return render_template("mens_Shoes-0027.html")
 
@app.route("/mens_Shoes-0028.html")
def shose12():
    return render_template("mens_Shoes-0028.html")
    
@app.route("/mens_Shoes-0029.html")
def shose13():
    return render_template("mens_Shoes-0029.html")
    
@app.route("/mens_Shoes-0030.html")
def shose14():
    return render_template("mens_Shoes-0030.html")
    
@app.route("/mens_Shoes-0031.html")
def shose15():
    return render_template("mens_Shoes-0031.html")

@app.route("/mens_Shoes-0032.html")
def shose16():
    return render_template("mens_Shoes-0032.html")
    
@app.route("/toys.html")
def toy():
    return render_template("toys.html")
    
@app.route("/toys1-0129.html")
def toys1():
    return render_template("toys1-0129.html")
    
@app.route("/toys2-0130.html")
def toys2():
    return render_template("toys2-0130.html")

@app.route("/thank-you.html")
def thankyou():
    return render_template("thank-you.html")
  
@app.route("/toys3-0131.html")
def toys3():
    return render_template("toys3-0131.html")
    
@app.route("/toys4-0132.html")
def toys4():
    return render_template("toys4-0132.html")
   
@app.route("/toys5-0133.html")
def toys5():
    return render_template("toys5-0133.html")
    
@app.route("/toys6-0134.html")
def toys6():
    return render_template("toys6-0134.html")
@app.route("/toys7-0135.html")

def toys7():
    return render_template("toys7-0135.html")
    
@app.route("/toys8-0136.html")
def toys8():
    return render_template("toys8-0136.html")
    
@app.route("/toys9-0137.html")
def toys9():
    return render_template("toys9-0137.html")
    
@app.route("/toys10-0138.html")
def toys10():
    return render_template("toys10-0138.html")
    
@app.route("/toys11-0139.html")
def toys11():
    return render_template("toys11-0139.html")
       
@app.route("/toys12-0140.html")
def toys12():
    return render_template("toys12-0140.html")
    
@app.route("/toys13-0141.html")
def toys13():
    return render_template("toys13-0141.html")
    
@app.route("/toys14-0142.html")
def toys14():
    return render_template("toys14-0142.html")   
       
@app.route("/toys15-0143.html")
def toys15():
    return render_template("toys15-0143.html")  
       
@app.route("/toys16-0144.html")
def toys16():
    return render_template("toys16-0144.html")
    
@app.route("/woman_handbags.html")
def whandbag():
    return render_template("woman_handbags.html") 

@app.route("/handbag1-0081.html")
def handbag1():
    return render_template("handbag1-0081.html") 

@app.route("/handbag2-0082.html")
def handbag2():
    return render_template("handbag2-0082.html")

@app.route("/handbag3-0083.html")
def handbag3():
    return render_template("handbag3-0083.html")

@app.route("/handbag4-0084.html")
def handbag4():
    return render_template("handbag4-0084.html")

@app.route("/handbag5-0085.html")
def handbag5():
    return render_template("handbag5-0085.html") 

@app.route("/handbag6-0086.html")
def handbag6():
    return render_template("handbag6-0086.html") 

@app.route("/handbag7-0087.html")
def handbag7():
    return render_template("handbag7-0087.html")

@app.route("/handbag8-0088.html")
def handbag8():
    return render_template("handbag8-0088.html")         

@app.route("/handbag9-0089.html")
def handbag9():
    return render_template("handbag9-0089.html") 

@app.route("/handbag10-0090.html")
def handbag10():
    return render_template("handbag10-0090.html")     

@app.route("/handbag11-0091.html")
def handbag11():
    return render_template("handbag11-0091.html")      

@app.route("/handbag12-0092.html")
def handbag12():
    return render_template("handbag12-0092.html")  

@app.route("/handbag13-0093.html")
def handbag13():
    return render_template("handbag13-0093.html")  

@app.route("/handbag14-0094.html")
def handbag14():
    return render_template("handbag14-0094.html")   

@app.route("/handbag15-0095.html")
def handbag15():
    return render_template("handbag15-0095.html")

@app.route("/handbag16-0096.html")
def handbag16():
    return render_template("handbag16-0096.html")
@app.route("/mens_jacket.html")
def mens_jacket():
    return render_template("mens_jacket.html")
@app.route("/mens_jacket1-0033.html")
def mens_jacket1():
    return render_template("mens_jacket1-0033.html")
@app.route("/mens_jacket2-0034.html")
def mens_jacket2():
    return render_template("mens_jacket2-0034.html")
@app.route("/mens_jacket3-0035.html")
def mens_jacket3():
    return render_template("mens_jacket3-0035.html")
@app.route("/mens_jacket4-0036.html")
def mens_jacket4():
    return render_template("mens_jacket4-0036.html")
@app.route("/mens_jacket5-0037.html")
def mens_jacket5():
    return render_template("mens_jacket5-0037.html")
@app.route("/mens_jacket6-0038.html")
def mens_jacket6():
    return render_template("mens_jacket6-0038.html")
@app.route("/mens_jacket7-0039.html")
def mens_jacket7():
    return render_template("mens_jacket7-0039.html")
@app.route("/mens_jacket8-0040.html")
def mens_jacket8():
    return render_template("mens_jacket8-0040.html")
@app.route("/mens_jacket9-0041.html")
def mens_jacket9():
    return render_template("mens_jacket9-0041.html")
@app.route("/mens_jacket10-0042.html")
def mens_jacket10():
    return render_template("mens_jacket10-0042.html")
@app.route("/mens_jacket11-0043.html")
def mens_jacket11():
    return render_template("mens_jacket11-0043.html")
@app.route("/mens_jacket12-0044.html")
def mens_jacket12():
    return render_template("mens_jacket12-0044.html")
@app.route("/mens_jacket13-0045.html")
def mens_jacket13():
    return render_template("mens_jacket13-0045.html")
@app.route("/mens_jacket14-0046.html")
def mens_jacket14():
    return render_template("mens_jacket14-0046.html")
@app.route("/mens_jacket15-0047.html")
def mens_jacket15():
    return render_template("mens_jacket15-0047.html")
@app.route("/mens_jacket16-0048.html")
def mens_jacket16():
    return render_template("mens_jacket16-0048.html")


@app.route("/womens_top.html")
def wtop():
    return render_template("womens_top.html")  

@app.route("/top1-0065.html")
def wtop1():
    # with sqlite3.connect('new_db.db') as conn:
    #     cur_name=conn.cursor()
    #     params=[session['email_id'].lower()]
    #     em_id=str(session['email_id'])
    #     cur_name.execute("select name from signup where email_id='{0}'".format(em_id))
    #     name_get=cur_name.fetchone()
    #     flash(session['email_id'],'category1')
    #     flash(('Welcome'+" "+ name_get[0]),'category2')
        return render_template("top1-0065.html")
    # return render_template("top1-0065.html", response=session['email_id'])

@app.route("/top2-0066.html")
def wtop2():
    return render_template("top2-0066.html")

@app.route("/top3-0067.html")
def wtop3():
    return render_template("top3-0067.html")
   
@app.route("/top4-0068.html")
def wtop4():
    return render_template("top4-0068.html")
     
@app.route("/top5-0069.html")
def wtop5():
    return render_template("top5-0069.html")

@app.route("/top6-0070.html")
def wtop6():
    return render_template("top6-0070.html")    

@app.route("/top7-0071.html")
def wtop7():
    return render_template("top7-0071.html")

@app.route("/top8-0072.html")
def wtop8():
    return render_template("top8-0072.html")

@app.route("/top9-0073.html")
def wtop9():
    return render_template("top9-0073.html")     

@app.route("/top10-0074.html")
def wtop10():
    return render_template("top10-0074.html") 

@app.route("/top11-0075.html")
def wtop11():
    return render_template("top11-0075.html") 

@app.route("/top12-0076.html")
def wtop12():
    return render_template("top12-0076.html")

@app.route("/top13-0077.html")
def wtop13():
    return render_template("top13-0077.html")

@app.route("/top14-0078.html")
def wtop14():
    return render_template("top14-0078.html")

@app.route("/top15-0079.html")
def wtop15():
    return render_template("top15-0079.html")

@app.route("/top16-0080.html")
def wtop16():
    return render_template("top16-0080.html")

@app.route("/bags.html")
def bags():
    return render_template("bags.html")  
   
@app.route("/bags1-0171.html")
def bags1():
    return render_template("bags1-0171.html")  
       
@app.route("/bags2-0172.html")
def bags2():
    return render_template("bags2-0172.html")   
@app.route("/bags3-0173.html")
def bags3():
    return render_template("bags3-0173.html") 
    
@app.route("/bags4-0174.html")
def bags4():
    return render_template("bags4-0174.html")   
@app.route("/bags5-0175.html")
def bags5():
    return render_template("bags5-0175.html")     
 
@app.route("/bags6-0176.html")
def bags6():
    return render_template("bags6-0176.html")
@app.route("/bags7-0177.html")
def bags7():
    return render_template("bags7-0177.html")
@app.route("/bags8-0178.html")
def bags8():
    return render_template("bags8-0178.html")  
@app.route("/bags9-0179.html")
def bags9():
    return render_template("bags9-0179.html")  
@app.route("/bags10-0180.html")
def bags10():
    return render_template("bags10-0180.html")  
@app.route("/bags11-0181.html")
def bags11():
    return render_template("bags11-0181.html")  
@app.route("/bags12-0182.html")
def bags12():
    return render_template("bags12-0182.html")   
@app.route("/bags13-0183.html")
def bags13():
    return render_template("bags13-0183.html")
@app.route("/bags14-0184.html")
def bags14():
    return render_template("bags14-0184.html")
@app.route("/bags15-0185.html")
def bags15():
    return render_template("bags15-0185.html")
@app.route("/bags16-0186.html")
def bags16():
    return render_template("bags16-0186.html")  
@app.route("/womens_shoes.html")
def wshoes():
    return render_template("womens_shoes.html")  

@app.route("/w-shoes-0113.html")
def wshoes1():
    return render_template("w-shoes-0113.html")

@app.route("/w-shoes-0114.html")
def wshoes2():
    return render_template("w-shoes-0114.html")

@app.route("/w-shoes-0115.html")
def wshoes3():
    return render_template("w-shoes-0115.html")

@app.route("/w-shoes-0116.html")
def wshoes4():
    return render_template("w-shoes-0116.html")

@app.route("/w-shoes-0117.html")
def wshoes5():
    return render_template("w-shoes-0117.html")

@app.route("/w-shoes-0118.html")
def wshoes6():
    return render_template("w-shoes-0118.html")

@app.route("/w-shoes-0119.html")
def wshoes7():
    return render_template("w-shoes-0119.html")                           

@app.route("/w-shoes-0120.html")
def wshoes8():
    return render_template("w-shoes-0120.html")

@app.route("/w-shoes-0121.html")
def wshoes9():
    return render_template("w-shoes-0121.html")

@app.route("/w-shoes-0122.html")
def wshoes10():
    return render_template("w-shoes-0122.html")

@app.route("/w-shoes-0123.html")
def wshoes11():
    return render_template("w-shoes-0123.html")

@app.route("/w-shoes-0124.html")
def wshoes12():
    return render_template("w-shoes-0124.html")

@app.route("/w-shoes-0125.html")
def wshoes13():
    return render_template("w-shoes-0125.html")

@app.route("/w-shoes-0126.html")
def wshoes14():
    return render_template("w-shoes-0126.html")

@app.route("/w-shoes-0127.html")
def wshoes15():
    return render_template("w-shoes-0127.html")

@app.route("/w-shoes-0128.html")
def wshoes16():
    return render_template("w-shoes-0128.html") 

@app.route("/jeans.html")
def jeans():
    return render_template("jeans.html")
@app.route("/jeans1-0145.html")
def jeans1():
    return render_template("jeans1-0145.html") 
@app.route("/jeans2-0146.html")
def jeans2():
    return render_template("jeans2-0146.html")  
@app.route("/jeans3-0147.html")
def jeans3():
    return render_template("jeans3-0147.html")  
@app.route("/jeans4-0148.html")
def jeans4():
    return render_template("jeans4-0148.html")  
@app.route("/jeans5-0149.html")
def jeans5():
    return render_template("jeans5-0149.html")  
@app.route("/jeans6-0150.html")
def jeans6():
    return render_template("jeans6-0150.html")    
@app.route("/jeans7-0151.html")
def jeans7():
    return render_template("jeans7-0151.html") 
@app.route("/jeans8-0152.html")
def jeans8():
    return render_template("jeans8-0152.html") 
@app.route("/jeans9-0153.html")
def jeans9():
    return render_template("jeans9-0153.html") 
@app.route("/jeans10-0154.html")
def jeans10():
    return render_template("jeans10-0154.html") 
@app.route("/jeans11-0155.html")
def jeans11():
    return render_template("jeans11-0155.html") 
@app.route("/jeans12-0156.html")
def jeans12():
    return render_template("jeans12-0156.html") 
@app.route("/jeans13-0157.html")
def jeans13():
    return render_template("jeans13-0157.html") 
@app.route("/jeans14-0158.html")
def jeans14():
    return render_template("jeans14-0158.html")   
@app.route("/jeans15-0159.html")
def jeans15():
    return render_template("jeans15-0159.html") 
@app.route("/jeans16-0160.html")
def jeans16():
    return render_template("jeans16-0160.html")
@app.route("/bshirts.html")
def bshirts():
    return render_template("bshirts.html")
@app.route("/bshirts1-0374.html")
def bshirts1():
    return render_template("bshirts1-0374.html")
@app.route("/bshirts2-0375.html")
def bshirts2():
    return render_template("bshirts2-0375.html")  
@app.route("/bshirts3-0376.html")
def bshirts3():
    return render_template("bshirts3-0376.html") 
@app.route("/bshirts4-0377.html")
def bshirts4():
    return render_template("bshirts4-0377.html") 
@app.route("/bshirts5-0378.html")
def bshirts5():
    return render_template("bshirts5-0378.html")   
@app.route("/bshirts6-0379.html")
def bshirts6():
    return render_template("bshirts6-0379.html")   
@app.route("/bshirts7-0380.html")
def bshirts7():
    return render_template("bshirts7-0380.html")
@app.route("/bshirts8-0381.html")
def bshirts8():
    return render_template("bshirts8-0381.html")
@app.route("/bshirts9-0382.html")
def bshirts9():
    return render_template("bshirts9-0382.html")  
@app.route("/bshirts10-0383.html")
def bshirts10():
    return render_template("bshirts10-0383.html")  
@app.route("/bshirts11-0384.html")
def bshirts11():
    return render_template("bshirts11-0384.html")  
@app.route("/bshirts12-0385.html")
def bshirts12():
    return render_template("bshirts12-0385.html")  
@app.route("/bshirts13-0386.html")
def bshirts13():
    return render_template("bshirts13-0386.html")     
@app.route("/bshirts14-0387.html")
def bshirts14():
    return render_template("bshirts14-0387.html")
@app.route("/bshirts15-0388.html")
def bshirts15():
    return render_template("bshirts15-0388.html")
@app.route("/bshirts16-0389.html")
def bshirts16():
    return render_template("bshirts16-0389.html")
@app.route("/womens_jewellery.html")
def wjewellery():
    return render_template("womens_jewellery.html") 

@app.route("/jewellery1-0097.html")
def wjewellery1():
    return render_template("jewellery1-0097.html") 

@app.route("/jewellery2-0098.html")
def wjewellery2():
    return render_template("jewellery2-0098.html")

@app.route("/jewellery3-0099.html")
def wjewellery3():
    return render_template("jewellery3-0099.html")
 
@app.route("/jewellery4-0100.html")
def wjewellery4():
    return render_template("jewellery4-0100.html")

@app.route("/jewellery5-0101.html")
def wjewellery5():
    return render_template("jewellery5-0101.html")

@app.route("/jewellery6-0102.html")
def wjewellery6():
    return render_template("jewellery6-0102.html")     
     
@app.route("/jewellery7-0103.html")
def wjewellery7():
    return render_template("jewellery7-0103.html")      

@app.route("/jewellery8-0104.html")
def wjewellery8():
    return render_template("jewellery8-0104.html") 

@app.route("/jewellery9-0105.html")
def wjewellery9():
    return render_template("jewellery9-0105.html") 

@app.route("/jewellery10-0106.html")
def wjewellery10():
    return render_template("jewellery10-0106.html")     

@app.route("/jewellery11-0107.html")
def wjewellery11():
    return render_template("jewellery11-0107.html") 

@app.route("/jewellery12-0108.html")
def wjewellery12():
    return render_template("jewellery12-0108.html") 

@app.route("/jewellery13-0109.html")
def wjewellery13():
    return render_template("jewellery13-0109.html")

@app.route("/jewellery14-0110.html")
def wjewellery14():
    return render_template("jewellery14-0110.html")

@app.route("/jewellery15-0111.html")
def wjewellery15():
    return render_template("jewellery15-0111.html")

@app.route("/jewellery16-0112.html")
def wjewellery16():
    return render_template("jewellery16-0112.html")  
@app.route("/appleLap.html")
def apple():
    return render_template("appleLap.html")  
@app.route("/Apple1-0257.html")
def apple1():
    return render_template("Apple1-0257.html")  
   
@app.route("/apple2-0258.html")
def apple2():
    return render_template("apple2-0258.html")
@app.route("/apple3-0259.html")
def apple3():
    return render_template("apple3-0259.html")   
@app.route("/apple4-0260.html")
def apple4():
    return render_template("apple4-0260.html")  
@app.route("/apple5-0261.html")
def apple5():
    return render_template("apple5-0261.html")
@app.route("/apple6-0262.html")
def apple6():
    return render_template("apple6-0262.html")
@app.route("/apple7-0263.html")
def apple7():
    return render_template("apple7-0263.html")
@app.route("/apple8-0264.html")
def apple8():
    return render_template("apple8-0264.html")
@app.route("/apple9-0265.html")
def apple9():
    return render_template("apple9-0265.html")
@app.route("/apple10-0266.html")
def apple10():
    return render_template("apple10-0266.html")
@app.route("/apple11-0267.html")
def apple11():
    return render_template("apple11-0267.html")
@app.route("/apple12-0268.html")
def apple12():
    return render_template("apple12-0268.html")
@app.route("/apple13-0269.html")
def apple13():
    return render_template("apple13-0269.html") 
@app.route("/apple14-0270.html")
def apple14():
    return render_template("apple14-0270.html")   
@app.route("/apple15-0271.html")
def apple15():
    return render_template("apple15-0271.html")   
@app.route("/apple16-0272.html")
def apple16():
    return render_template("apple16-0272.html")    
@app.route("/DellLap.html")
def dell():
    return render_template("DellLap.html")
@app.route("/dell1-0273.html")
def dell1():
    return render_template("dell1-0273.html") 
@app.route("/dell2-0274.html")
def dell2():
    return render_template("dell2-0274.html") 
@app.route("/dell3-0275.html")
def dell3():
    return render_template("dell3-0275.html")
@app.route("/dell4-0276.html")
def dell4():
    return render_template("dell4-0276.html")   
@app.route("/dell5-0277.html")
def dell5():
    return render_template("dell5-0277.html")   
@app.route("/dell6-0278.html")
def dell6():
    return render_template("dell6-0278.html")   
@app.route("/dell7-0279.html")
def dell7():
    return render_template("dell7-0279.html")  
@app.route("/dell8-0280.html")
def dell8():
    return render_template("dell8-0280.html") 
@app.route("/dell9-0281.html")
def dell9():
    return render_template("dell9-0281.html")
@app.route("/dell10-0282.html")
def dell10():
    return render_template("dell10-0282.html")
@app.route("/dell11-0283.html")
def dell11():
    return render_template("dell11-0283.html")
@app.route("/dell12-0284.html")
def dell12():
    return render_template("dell12-0284.html")
@app.route("/dell13-0285.html")
def dell13():
    return render_template("dell13-0285.html")  
@app.route("/dell14-0286.html")
def dell14():
    return render_template("dell14-0286.html")  
@app.route("/dell15-0287.html")
def dell15():
    return render_template("dell15-0287.html")  
@app.route("/dell16-0288.html")
def dell16():
    return render_template("dell16-0288.html")    
@app.route("/Memory(RAM).html")
def dmemory():
    return render_template("Memory(RAM).html")

@app.route("/D_Memory1-0289.html")
def dmemory1():
    return render_template("D_Memory1-0289.html")

@app.route("/D_Memory2-0290.html")
def dmemory2():
    return render_template("D_Memory2-0290.html")

@app.route("/D_Memory3-0291.html")
def dmemory3():
    return render_template("D_Memory3-0291.html")

@app.route("/D_Memory4-0292.html")
def dmemory4():
    return render_template("D_Memory4-0292.html")

@app.route("/D_Memory5-0293.html")
def dmemory5():
    return render_template("D_Memory5-0293.html")

@app.route("/D_Memory6-0294.html")
def dmemory6():
    return render_template("D_Memory6-0294.html")

@app.route("/D_Memory7-0295.html")
def dmemory7():
    return render_template("D_Memory7-0295.html")

@app.route("/D_Memory8-0296.html")
def dmemory8():
    return render_template("D_Memory8-0296.html")            
@app.route("/Motherboards.html")
def dmotherboard():
    return render_template("Motherboards.html") 

@app.route("/D_Motherboard1-0297.html")
def dmotherboard1():
    return render_template("D_Motherboard1-0297.html") 

@app.route("/D_Motherboard2-0298.html")
def dmotherboard2():
    return render_template("D_Motherboard2-0298.html")

@app.route("/D_Motherboard3-0299.html")
def dmotherboard3():
    return render_template("D_Motherboard3-0299.html")

@app.route("/D_Motherboard4-0300.html")
def dmotherboard4():
    return render_template("D_Motherboard4-0300.html")

@app.route("/D_Motherboard5-0301.html")
def dmotherboard5():
    return render_template("D_Motherboard5-0301.html")

@app.route("/D_Motherboard6-0302.html")
def dmotherboard6():
    return render_template("D_Motherboard6-0302.html")

@app.route("/D_Motherboard7-0303.html")
def dmotherboard7():
    return render_template("D_Motherboard7-0303.html")

@app.route("/D_Motherboard8-0304.html")
def dmotherboard8():
    return render_template("D_Motherboard8-0304.html")

@app.route("/D_Motherboard9-0305.html")
def dmotherboard9():
    return render_template("D_Motherboard9-0305.html")
@app.route("/camera.html")
def camera():
    return render_template("camera.html")     
@app.route("/camera1-0306.html")
def camera1():
    return render_template("camera1-0306.html")   
@app.route("/camera2-0307.html")
def camera2():
    return render_template("camera2-0307.html") 
@app.route("/camera3-0308.html")
def camera3():
    return render_template("camera3-0308.html")
@app.route("/camera4-0309.html")
def camera4():
    return render_template("camera4-0309.html")
@app.route("/camera5-0310.html")
def camera5():
    return render_template("camera5-0310.html")
@app.route("/camera6-0311.html")
def camera6():
    return render_template("camera6-0311.html")
@app.route("/camera7-0312.html")
def camera7():
    return render_template("camera7-0312.html")
@app.route("/camera8-0313.html")
def camera8():
    return render_template("camera8-0313.html")
@app.route("/camera9-0314.html")
def camera9():
    return render_template("camera9-0314.html")
@app.route("/camera10-0315.html")
def camera10():
    return render_template("camera10-0315.html")
@app.route("/camera11-0316.html")
def camera11():
    return render_template("camera11-0316.html")
@app.route("/camera12-0317.html")
def camera12():
    return render_template("camera12-0317.html")
@app.route("/mobileapple.html")
def mobileapple():
    return render_template("mobileapple.html")
@app.route("/mapple1-0326.html")
def mobileapple1():
    return render_template("mapple1-0326.html")    
@app.route("/mapple2-0327.html")
def mobileapple2():
    return render_template("mapple2-0327.html")  
@app.route("/mapple3-0328.html")
def mobileapple3():
    return render_template("mapple3-0328.html") 
@app.route("/mapple4-0329.html")
def mobileapple4():
    return render_template("mapple4-0329.html")   
@app.route("/mapple5-0330.html")
def mobileapple5():
    return render_template("mapple5-0330.html")    
@app.route("/mapple6-0331.html")
def mobileapple6():
    return render_template("mapple6-0331.html")  
@app.route("/mapple7-0332.html")
def mobileapple7():
    return render_template("mapple7-0332.html")     
@app.route("/mapple8-0333.html")
def mobileapple8():
    return render_template("mapple8-0333.html") 
@app.route("/mapple9-0334.html")
def mobileapple9():
    return render_template("mapple9-0334.html")
@app.route("/mapple10-0335.html")
def mobileapple10():
    return render_template("mapple10-0335.html")
@app.route("/mapple11-0336.html")
def mobileapple11():
    return render_template("mapple11-0336.html")
@app.route("/mapple12-0337.html")
def mobileapple12():
    return render_template("mapple12-0337.html")
@app.route("/mapple13-0338.html")
def mobileapple13():
    return render_template("mapple13-0338.html")
@app.route("/mapple14-0339.html")
def mobileapple14():
    return render_template("mapple14-0339.html")
@app.route("/mapple15-0340.html")
def mobileapple15():
    return render_template("mapple15-0340.html")
@app.route("/mapple16-0341.html")
def mobileapple16():
    return render_template("mapple16-0341.html")

@app.route("/Flashes.html")
def Flashes():
    return render_template("Flashes.html")

@app.route("/flash1-0318.html")
def Flash1():
    return render_template("flash1-0318.html")

@app.route("/flash2-0319.html")
def Flash2():
    return render_template("flash2-0319.html")

@app.route("/flash3-0320.html")
def Flash3():
    return render_template("flash3-0320.html")

@app.route("/flash4-0321.html")
def Flash4():
    return render_template("flash4-0321.html")

@app.route("/flash5-0322.html")
def Flash5():
    return render_template("flash5-0322.html")

@app.route("/flash6-0323.html")
def Flash6():
    return render_template("flash6-0324.html")

@app.route("/flash7-0324.html")
def Flash7():
    return render_template("flash7-0324.html")

@app.route("/flash8-0325.html")
def Flash8():
    return render_template("flash8-0325.html")
@app.route("/samsung.html")
def samsung():
    return render_template("samsung.html")
@app.route("/samsung1-0342.html")
def samsung1():
    return render_template("samsung1-0342.html")
@app.route("/samsung2-0343.html")
def samsung2():
    return render_template("samsung2-0343.html")
@app.route("/samsung3-0344.html")
def samsung3():
    return render_template("samsung3-0344.html")
@app.route("/samsung4-0345.html")
def samsung4():
    return render_template("samsung4-0345.html")
@app.route("/samsung5-0346.html")
def samsung5():
    return render_template("samsung5-0346.html")
@app.route("/samsung6-0347.html")
def samsung6():
    return render_template("samsung6-0347.html")
@app.route("/samsung7-0348.html")
def samsung7():
    return render_template("samsung7-0348.html")
@app.route("/samsung8-0349.html")
def samsung8():
    return render_template("samsung8-0349.html")
@app.route("/samsung9-0350.html")
def samsung9():
    return render_template("samsung9-0350.html")
@app.route("/samsung10-0351.html")
def samsung10():
    return render_template("samsung10-0351.html")
@app.route("/samsung11-0352.html")
def samsung11():
    return render_template("samsung11-0352.html")
@app.route("/samsung12-0353.html")
def samsung12():
    return render_template("samsung12-0353.html")
@app.route("/samsung13-0354.html")
def samsung13():
    return render_template("samsung13-0354.html")
@app.route("/samsung14-0355.html")
def samsung14():
    return render_template("samsung14-0355.html")
@app.route("/samsung15-0356.html")
def samsung15():
    return render_template("samsung15-0356.html")
@app.route("/samsung16-0357.html")
def samsung16():
    return render_template("samsung16-0357.html")
@app.route("/mens_sunglasses.html")
def Sunglasses():
    return render_template("mens_sunglasses.html") 

@app.route("/mens_glass1-0358.html")
def Sunglasses1():
    return render_template("mens_glass1-0358.html")

@app.route("/mens_glass2-0359.html")
def Sunglasses2():
    return render_template("mens_glass2-0359.html")

@app.route("/mens_glass3-0360.html")
def Sunglasses3():
    return render_template("mens_glass3-0360.html")

@app.route("/mens_glass4-0361.html")
def Sunglasses4():
    return render_template("mens_glass4-0361.html")

@app.route("/mens_glass5-0362.html")
def Sunglasses5():
    return render_template("mens_glass5-0362.html")

@app.route("/mens_glass6-0363.html")
def Sunglasses6():
    return render_template("mens_glass6-0363.html")

@app.route("/mens_glass7-0364.html")
def Sunglasses7():
    return render_template("mens_glass7-0364.html")

@app.route("/mens_glass8-0365.html")
def Sunglasses8():
    return render_template("mens_glass8-0365.html")

@app.route("/mens_glass9-0366.html")
def Sunglasses9():
    return render_template("mens_glass9-0366.html")

@app.route("/mens_glass10-0367.html")
def Sunglasses10():
    return render_template("mens_glass10-0367.html")

@app.route("/mens_glass11-0368.html")
def Sunglasses11():
    return render_template("mens_glass11-0368.html")

@app.route("/mens_glass12-0369.html")
def Sunglasses12():
    return render_template("mens_glass12-0369.html")

@app.route("/mens_glass13-0370.html")
def Sunglasses13():
    return render_template("mens_glass13-0370.html")            

@app.route("/mens_glass14-0371.html")
def Sunglasses14():
    return render_template("mens_glass14-0371.html")

@app.route("/mens_glass15-0372.html")
def Sunglasses15():
    return render_template("mens_glass15-0372.html")

@app.route("/mens_glass16-0373.html")
def Sunglasses16():
    return render_template("mens_glass16-0373.html")

@app.route("/my-wishlist.html")
def wishlist():
    return render_template("my-wishlist.html")

@app.route("/OrderConf.html")
def Order():
    return render_template("OrderConf.html")

@app.route("/terms-conditions.html")
def terms():
    return render_template("terms-conditions.html")

if __name__ == "__main__":
    app.run(debug=True)
 