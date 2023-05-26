import sqlite3

#Open database
conn = sqlite3.connect('new_db.db')

conn.execute('''CREATE TABLE signin (
    id character varying NOT NULL,
    email_id character varying,
    last_visited timestamp without time zone,
    logout_time timestamp without time zone
)


''')
conn.execute('''CREATE TABLE signup (
    id character varying NOT NULL,
    email_id character varying,
    name character varying NOT NULL,
    phone_number character varying NOT NULL,
    password character varying NOT NULL,
    confirm_password character varying NOT NULL,
    created_at timestamp without time zone,
    modified_at timestamp without time zone
);''')

conn.execute('''CREATE TABLE add_to_cart (
    id character varying NOT NULL,
    email_id character varying,
    product_image character varying,
    product_name character varying NOT NULL,
    product_id varchar(20),
    product_qty integer not null,
    price float
)''')

conn.execute('''CREATE TABLE order_confirmation (id INTEGER PRIMARY KEY AUTOINCREMENT, email_id character varying,cart text,total_price float,bfname character varying,blname character varying, billing_address character varying, bcity character varying,bstate character varying,bpincode varchar(10), sfname character varying,slname character varying, shipping_address character varying,scity character varying, sstate character varying,spincode varchar(10),card_number varchar(20), card_name character varying,cvv varchar(4),expiry_date varchar(10))''')



conn.execute('''create table final_product(product_id varchar(20) primary key, product_type varchar(50),category varchar(50),subcategory varchar(50),product_name varchar(50),price float,label varchar(30),rating integer,image varchar(50),description varchar(300));''')


product_insert_query='''insert into final_product (product_id,product_type,category,subcategory,product_name,price,label,rating,image,description) values(?,?,?,?,?,?,?,?,?,?)'''

product_entries=[('0001','Clothing','Men','Shirts','Black Print shirt',450.99 ,'new',4,'assets/images/products/s1.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
('0002','Clothing','Men','Shirts','Red Print Shirt',450.99 ,'sale',4,'assets/images/products/s2.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
('0003','Clothing','Men','Shirts','whilte-line Print shirt',450.99 ,'hot',4,'assets/images/products/s3.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
('0004','Clothing','Men','Shirts','half-sleaves shirt',450.99 ,'hot',4,'assets/images/products/s4.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
('0005','Clothing','Men','Shirts','Sky-blue Print shirt',450.99 ,'hot',4,'assets/images/products/s5.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
('0006','Clothing','Men','Shirts','white Print shirt',450.99 ,'hot',4,'assets/images/products/s6.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
('0007','Clothing','Men','Shirts','Blue-checks Print shirt',450.99 ,'hot',4,'assets/images/products/s7.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
('0008','Clothing','Men','Shirts','Black Print shirt',450.99 ,'hot',4,'assets/images/products/s8.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
('0009','Clothing','Men','Shirts','White-checks Print shirt',450.99 ,'hot',4,'assets/images/products/s9.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
('0010','Clothing','Men','Shirts','Yellow Print shirt',450.99 ,'hot',4,'assets/images/products/s10.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
('0011','Clothing','Men','Shirts','Yellow-checks Print shirt',450.99 ,'hot',4,'assets/images/products/s11.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
('0012','Clothing','Men','Shirts','White Full-sleaves shirt',450.99 ,'hot',4,'assets/images/products/s12.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
('0013','Clothing','Men','Shirts','Blue-line Print shirt',450.99 ,'hot',4,'assets/images/products/s13.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
('0014','Clothing','Men','Shirts','Plane-Blue shirt',450.99 ,'hot',4,'assets/images/products/s14.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
('0015','Clothing','Men','Shirts','Dark blue Print Shirt',450.99 ,'hot',4,'assets/images/products/s15.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
('0016','Clothing','Men','Shirts','Green Print shirt',450.99 ,'hot',4,'assets/images/products/s16.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0017','Clothing','Men','Shoes','Walking Shoes',450.99,'new',4,'assets/images/products/MSho1.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0018','Clothing','Men','Shoes','Casual Shoes',450.99,'sale',4,'assets/images/products/MSho2.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0019','Clothing','Men','Shoes','Grid White Shoes',450.99,'hot',4,'assets/images/products/MSho3.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0020','Clothing','Men','Shoes','Grid White Shoes',450.99,'hot',4,'assets/images/products/MSho4.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0021','Clothing','Men','Shoes','Black Casual Shoes',450.99,'hot',4,'assets/images/products/MSho5.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0022','Clothing','Men','Shoes','Boat Shoes',450.99,'hot',4,'assets/images/products/MSho6.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0023','Clothing','Men','Shoes','Formal Shoes',450.99,'hot',4,'assets/images/products/MSho7.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0024','Clothing','Men','Shoes','Athletic Shoes',450.99,'hot',4,'assets/images/products/MSho8.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0025','Clothing','Men','Shoes','Jazz Shoes',450.99,'hot',4,'assets/images/products/MSho9.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0026','Clothing','Men','Shoes','Dress Shoes',450.99,'hot',4,'assets/images/products/MSho10.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0027','Clothing','Men','Shoes','Clog Shoes',450.99,'hot',4,'assets/images/products/MSho11.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0028','Clothing','Men','Shoes','Brogan  Shoes',450.99,'hot',4,'assets/images/products/MSho12.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0029','Clothing','Men','Shoes','Black Shoes',450.99,'hot',4,'assets/images/products/MSho13.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0030','Clothing','Men','Shoes','White Shoes',450.99,'hot',4,'assets/images/products/MSho14.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0031','Clothing','Men','Shoes','Ankle Shoes',450.99,'hot',4,'assets/images/products/MSho15.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0032','Clothing','Men','Shoes','Road-running Shoes',450.99,'hot',4,'assets/images/products/MSho16.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0033','Clothing','Men','Jackets','Field Jacket',400.99,'new',4,'static/assets/images/products/mj1.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0034','Clothing','Men','Jackets','Bomber Jacket',550.99,'sale',4,'static/assets/images/products/mj2.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0035','Clothing','Men','Jackets','Chore Coat',350.99,'hot',4,'static/assets/images/products/mj3.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0036','Clothing','Men','Jackets','Denim Jacket',250.99,'hot',4,'static/assets/images/products/mj4.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0037','Clothing','Men','Jackets','Trucker Jacket',150.99,'hot',4,'static/assets/images/products/mj5.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0038','Clothing','Men','Jackets','Moto Jacket',650.99,'hot',4,'static/assets/images/products/mj6.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0039','Clothing','Men','Jackets','Shirt Jacket',850.99,'hot',4,'static/assets/images/products/mj7.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0040','Clothing','Men','Jackets','Harrington Jacket',900.99,'hot',4,'static/assets/images/products/mj8.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0041','Clothing','Men','Jackets','Leather Jacket',200.99,'hot',4,'static/assets/images/products/mj9.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0042','Clothing','Men','Jackets','Fleece Jacket',100.99,'hot',4,'static/assets/images/products/mj10.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0043','Clothing','Men','Jackets','Shearling Jacket',322.99,'hot',4,'static/assets/images/products/mj11.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0044','Clothing','Men','Jackets','Mac Jacket',443.99,'hot',4,'static/assets/images/products/mj12.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0045','Clothing','Men','Jackets','Puffer Jacket',656.99 ,'hot',4,'static/assets/images/products/mj13.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0046','Clothing','Men','Jackets','Coach Jacket',543.99,'hot',4,'static/assets/images/products/mj14.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0047','Clothing','Men','Jackets','Packable Jacket',564.99,'hot',4,'static/assets/images/products/mj15.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0048','Clothing','Men','Jackets','Varsity Jacket',444.99,'hot',4,'static/assets/images/products/mj16.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0065','Clothing','Women','Tops','Purple Top',350.00,'new',4,'assets/images/products/top1.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0066','Clothing','Women','Tops','Grey Top',450.00,'sale',4,'assets/images/products/top2.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0067','Clothing','Women','Tops','Light Orange Top',250.00 ,'hot',4,'assets/images/products/top3.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0068','Clothing','Women','Tops','Cotton',550.00,'hot',4,'assets/images/products/top4.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0069','Clothing','Women','Tops','White Top',340.00 ,'hot',4,'assets/images/products/top5.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0070','Clothing','Women','Tops','Sea Green Top',320.00 ,'hot',4,'assets/images/products/top6.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0071','Clothing','Women','Tops','Crop Top',599.00 ,'hot',4,'assets/images/products/top7.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0072','Clothing','Women','Tops','Pink Top',299.00 ,'hot',4,'assets/images/products/top8.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0073','Clothing','Women','Tops','Navy Blue Top',349.00,'hot',4,'assets/images/products/top9.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0074','Clothing','Women','Tops','OFF White Top',599.00,'hot',4,'assets/images/products/top10.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0075','Clothing','Women','Tops','White Cheques Top',330.00 ,'hot',4,'assets/images/products/top11.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0076','Clothing','Women','Tops','Baby Pink Top',479.00,'hot',4,'assets/images/products/top12.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0077','Clothing','Women','Tops','Black&White Top',899.00,'hot',4,'assets/images/products/top13.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0078','Clothing','Women','Tops','Denim Top',659.00,'hot',4,'assets/images/products/top14.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0079','Clothing','Women','Tops','Off Golden Top',999.00 ,'hot',4,'assets/images/products/top15.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0080','Clothing','Women','Tops','White Fancy Top',789.00,'hot',4,'assets/images/products/top16.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0081','Clothing','Women','Handbags','White Handbag',450.99,'new',4,'assets/images/products/h1.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0082','Clothing','Women','Handbags','Brown Handbag',450.99,'sale',4,'assets/images/products/h2.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0083','Clothing','Women','Handbags','SkyBlue Handbag',450.99,'hot',4,'assets/images/products/h3.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0084','Clothing','Women','Handbags','Brown Leather Handbag',450.99,'hot',4,'assets/images/products/h4.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0085','Clothing','Women','Handbags','Grey Handbag',450.99,'hot',4,'assets/images/products/h5.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0086','Clothing','Women','Handbags','Maroon Handbag',450.99,'hot',4,'assets/images/products/h6.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0087','Clothing','Women','Handbags','Olive Green Bag',450.99,'hot',4,'assets/images/products/h7.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0088','Clothing','Women','Handbags','Gucci handbag',450.99,'hot',4,'assets/images/products/h8.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0089','Clothing','Women','Handbags','Locca Handbag',450.99,'hot',4,'assets/images/products/h9.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0090','Clothing','Women','Handbags','Premium Handbag',450.99,'hot',4,'assets/images/products/h10.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0091','Clothing','Women','Handbags','Pink Premium Handbag',450.99,'hot',4,'assets/images/products/h11.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0092','Clothing','Women','Handbags','Cereal Handbag',450.99,'hot',4,'assets/images/products/h12.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0093','Clothing','Women','Handbags','Black Handbag',450.99,'hot',4,'assets/images/products/h13.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0094','Clothing','Women','Handbags','Green Handbag',450.99,'hot',4,'assets/images/products/h14.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0095','Clothing','Women','Handbags','Cera Handbags',450.99,'hot',4,'assets/images/products/h15.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0096','Clothing','Women','Handbags','Castle Handbag',450.99,'hot',4,'assets/images/products/h16.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0129','Clothing','Boys','Toys & Games','soft toy',450.99 ,'new',4,'assets/images/products/t1.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0130','Clothing','Boys','Toys & Games','soft boy toy',450.99 ,'sale',4,'assets/images/products/t2.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0131','Clothing','Boys','Toys & Games','pink unicorn toy',450.99 ,'hot',4,'assets/images/products/t3.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0132','Clothing','Boys','Toys & Games','rabbit toy',450.99 ,'hot',4,'assets/images/products/t4.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0133','Clothing','Boys','Toys & Games','Dinosaur Soft Toys',450.99 ,'hot',4,'assets/images/products/t5.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0134','Clothing','Boys','Toys & Games','Bluebells toys',450.99 ,'hot',4,'assets/images/products/t6.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0135','Clothing','Boys','Toys & Games','pink teddy',450.99 ,'hot',4,'assets/images/products/t7.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0136','Clothing','Boys','Toys & Games','kitty',450.99 ,'hot',4,'assets/images/products/t8.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0137','Clothing','Boys','Toys & Games','white rabbit',450.99 ,'hot',4,'assets/images/products/t9.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0138','Clothing','Boys','Toys & Games','white unicorn',450.99 ,'hot',4,'assets/images/products/t10.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0139','Clothing','Boys','Toys & Games','chotta Raju',450.99 ,'hot',4,'assets/images/products/t11.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0140','Clothing','Boys','Toys & Games','lady toy',450.99 ,'hot',4,'assets/images/products/t12.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0141','Clothing','Boys','Toys & Games','peppa pig',450.99 ,'hot',4,'assets/images/products/t13.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0142','Clothing','Boys','Toys & Games','micky mouse',450.99 ,'hot',4,'assets/images/products/t14.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0143','Clothing','Boys','Toys & Games','caterpillar toy',450.99 ,'hot',4,'assets/images/products/t15.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0144','Clothing','Boys','Toys & Games','Minnie Mouse',450.99 ,'hot',4,'assets/images/products/t16.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0257','Electronics','Laptops','Apple','MacBook',546,'new',4,'assets/images/products/Laptop1.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0258','Electronics','Laptops','Apple','MacBook',535,'sale',4,'assets/images/products/Laptop2.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0259','Electronics','Laptops','Apple','MacBook Pro',353,'hot',4,'assets/images/products/Laptop3.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0260','Electronics','Laptops','Apple','MacBook Air',767,'hot',4,'assets/images/products/Laptop4.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0261','Electronics','Laptops','Apple','MacBook Air. M1',575,'hot',4,'assets/images/products/Laptop5.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0262','Electronics','Laptops','Apple','MacBook Air.M2',575,'hot',4,'assets/images/products/Laptop6.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0263','Electronics','Laptops','Apple','MacBook Air.M3',577,'hot',4,'assets/images/products/Laptop7.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0264','Electronics','Laptops','Apple','MacBook Air.M5',575,'hot',4,'assets/images/products/Laptop8.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0265','Electronics','Laptops','Apple','MacBook Air.M6',575,'hot',4,'assets/images/products/Laptop9.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0266','Electronics','Laptops','Apple','MacBook Air.M7',575,'hot',4,'assets/images/products/Laptop10.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0267','Electronics','Laptops','Apple','MacBook Air.M8',579,'hot',4,'assets/images/products/Laptop11.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0268','Electronics','Laptops','Apple','MacBook Air.M9',456,'hot',4,'assets/images/products/Laptop12.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0269','Electronics','Laptops','Apple','MacBook Air.M10',786,'hot',4,'assets/images/products/Laptop13.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0270','Electronics','Laptops','Apple','MacBook Air.M11',668,'hot',4,'assets/images/products/Laptop14.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0271','Electronics','Laptops','Apple','MacBook Pro 13',898,'hot',4,'assets/images/products/Laptop15.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0272','Electronics','Laptops','Apple','MacBook Pro.14',365,'hot',4,'assets/images/products/Laptop16.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0273','Electronics','Laptops','Dell','Dell XPS 13 Plus',546,'new',4,'assets/images/products/Laptop17.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0274','Electronics','Laptops','Dell','Dell XPS 15',535,'sale',4,'assets/images/products/Laptop18.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0275','Electronics','Laptops','Dell','Dell XPS 17',353,'hot',4,'assets/images/products/Laptop19.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0276','Electronics','Laptops','Dell','Dell G15 gaming laptop',767,'hot',4,'assets/images/products/Laptop20.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0277','Electronics','Laptops','Dell','Dell Inspiron 15',575,'hot',4,'assets/images/products/Laptop21.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0278','Electronics','Laptops','Dell','Dell Latitude 9430',575,'hot',4,'assets/images/products/Laptop22.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0279','Electronics','Laptops','Dell','Vostro Laptop',577,'hot',4,'assets/images/products/Laptop23.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0280','Electronics','Laptops','Dell','Latitude C series',575,'hot',4,'assets/images/products/Laptop24.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0281','Electronics','Laptops','Dell','Latitude XT',575,'hot',4,'assets/images/products/Laptop25.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0282','Electronics','Laptops','Dell','Latitude XT 1',575,'hot',4,'assets/images/products/Laptop26.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0283','Electronics','Laptops','Dell','Latitude XT 2',579,'hot',4,'assets/images/products/Laptop27.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0284','Electronics','Laptops','Dell','Latitude XT 3',456,'hot',4,'assets/images/products/Laptop28.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0285','Electronics','Laptops','Dell','Latitude XT 4',786,'hot',4,'assets/images/products/Laptop29.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0286','Electronics','Laptops','Dell','Latitude XT 5',668,'hot',4,'assets/images/products/Laptop30.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0287','Electronics','Laptops','Dell','Latitude XT 6',898,'hot',4,'assets/images/products/Laptop31.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0288','Electronics','Laptops','Dell','Latitude XT 7',365,'hot',4,'assets/images/products/Laptop32.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0289','Electronics','Desktops','Memory(RAM)','RAM',532,'new',4,'assets/images/products/r1.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0290','Electronics','Desktops','Memory(RAM)','DRAM',533,'sale',4,'assets/images/products/r2.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0291','Electronics','Desktops','Memory(RAM)','SDRAM',675,'hot',4,'assets/images/products/r3.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0292','Electronics','Desktops','Memory(RAM)','SDR SDRAM',778,'hot',4,'assets/images/products/r4.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0293','Electronics','Desktops','Memory(RAM)','DDR SDRAM',665,'hot',4,'assets/images/products/r5.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0294','Electronics','Desktops','Memory(RAM)','DDR2',232,'hot',4,'assets/images/products/r6.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0295','Electronics','Desktops','Memory(RAM)','DDR3',244,'hot',4,'assets/images/products/r7.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0296','Electronics','Desktops','Memory(RAM)','DDR4',454,'hot',4,'assets/images/products/r8.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0297','Electronics','Desktops','Motherboard','AT Motherboard',355,'new',4,'assets/images/products/m1.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0298','Electronics','Desktops','Motherboards','ATX Motherboard',532,'sale',4,'assets/images/products/m2.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0299','Electronics','Desktops','Motherboards','LPX Motherboard',654,'hot',4,'assets/images/products/m3.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0300','Electronics','Desktops','Motherboards','BTX Motherboard',666,'hot',4,'assets/images/products/m4.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0301','Electronics','Desktops','Motherboards','Pico BTX motherboard',434,'hot',4,'assets/images/products/m5.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0302','Electronics','Desktops','Motherboards','Mini ITX motherboard',343,'hot',4,'assets/images/products/m6.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0303','Electronics','Desktops','Motherboards','Standard ATX',232,'hot',4,'assets/images/products/m7.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0304','Electronics','Desktops','Motherboards','Micro ATX',236,'hot',4,'assets/images/products/m8.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0305','Electronics','Desktops','Motherboards','eXtended ATX',767,'hot',4,'assets/images/products/m9.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0306','Electronics','Cameras','Film Cameras','Single-Lens Reflex (SLR) Cameras',234,'new',4,'assets/images/products/c1.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0307','Electronics','Cameras','Film Cameras','Twin-Lens Reflex (TLR) Cameras',454,'sale',4,'assets/images/products/c2.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0308','Electronics','Cameras','Film Cameras','Rangefinder Cameras',343,'hot',4,'assets/images/products/c3.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0309','Electronics','Cameras','Film Cameras','Point-and-Shoot Cameras',465,'hot',4,'assets/images/products/c4.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0310','Electronics','Cameras','Film Cameras','Instant Cameras',776,'hot',4,'assets/images/products/c5.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0311','Electronics','Cameras','Film Cameras','Stereo Cameras',543,'hot',4,'assets/images/products/c6.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0312','Electronics','Cameras','Film Cameras','Panoramic Cameras',543,'hot',4,'assets/images/products/c7.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0313','Electronics','Cameras','Film Cameras','Folding Cameras',533,'hot',4,'assets/images/products/c8.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0314','Electronics','Cameras','Film Cameras','Large Format Cameras',243,'hot',4,'assets/images/products/c9.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0315','Electronics','Cameras','Film Cameras','Box Cameras',107,'hot',4,'assets/images/products/c10.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0316','Electronics','Cameras','Film Cameras','Pinhole Cameras',453,'hot',4,'assets/images/products/c11.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0317','Electronics','Cameras','Film Cameras','Toy Cameras',355,'hot',4,'assets/images/products/c12.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0318','Electronics','Cameras','Flashes','Flash-lamp/Flash powder',776,'new',4,'assets/images/products/f1.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0319','Electronics','Cameras','Flashes','Flashbulbs',543,'sale',4,'assets/images/products/f2.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0320','Electronics','Cameras','Flashes','Electronic flash',543,'hot',4,'assets/images/products/f3.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0321','Electronics','Cameras','Flashes','High speed flash',533,'hot',4,'assets/images/products/f4.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0322','Electronics','Cameras','Flashes','Multi-flash',243,'hot',4,'assets/images/products/f5.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0323','Electronics','Cameras','Flashes','Flash intensity',107,'hot',4,'assets/images/products/f6.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0324','Electronics','Cameras','Flashes','Flash duration',453,'hot',4,'assets/images/products/f7.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0325','Electronics','Cameras','Flashes','Flash LED',123,'hot',4,'assets/images/products/f8.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0326','Electronics','Mobile Phones','Apple','iPhone 14',234,'new',4,'assets/images/products/mob1.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0327','Electronics','Mobile Phones','Apple','iPhone 14 Plus',454,'sale',4,'assets/images/products/mob2.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0328','Electronics','Mobile Phones','Apple','iPhone 14 Pro',343,'hot',4,'assets/images/products/mob3.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0329','Electronics','Mobile Phones','Apple','iPhone 14 Pro Max',465,'hot',4,'assets/images/products/mob4.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0330','Electronics','Mobile Phones','Apple','Apple iPhone SE',776,'hot',4,'assets/images/products/mob5.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0331','Electronics','Mobile Phones','Apple','iPhone 13 Pro Max',543,'hot',4,'assets/images/products/mob6.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0332','Electronics','Mobile Phones','Apple','iPhone 13 Pro',543,'hot',4,'assets/images/products/mob7.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0333','Electronics','Mobile Phones','Apple','iPhone 13 mini',533,'hot',4,'assets/images/products/mob8.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0334','Electronics','Mobile Phones','Apple','iPhone 13',243,'hot',4,'assets/images/products/mob9.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
,('0335','Electronics','Mobile Phones','Apple','iPhone 12 Pro',107,'hot',4,'assets/images/products/mob10.jpg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
]

conn.executemany(product_insert_query,product_entries)

m='INSERT INTO signup (id, email_id, name, phone_number, password, confirm_password, created_at, modified_at) VALUES(?,?,?,?,?,?,?,?)'
q = [('1', 'pratiksha@gmail.com', 'pratiksha ', '2342', '12345678', '12345678', '2022-12-08 15:22:41.385895', '2022-12-08 15:22:41.385895'),('2', 'pratibha@gmail.com', 'pratibha', '2343', 'pratibha', 'pratibha', '2022-12-08 15:23:23.529759', '2022-12-08 15:23:23.529759'),('3', 'pooja@gmail.com', 'pooja', '2323', '12345678', '12345678', '2022-12-12 17:27:18.623277', '2022-12-12 17:27:18.623277')]
conn.executemany(m,q)

sigin_query='''INSERT INTO signin (id, email_id, last_visited, logout_time) VALUES(?,?,?,?)'''
singin_members=[('3', 'pooja@gmail.com', '2022-12-13 13:31:34.409505', '2022-12-12 17:28:55'),('2', 'pratibha@gmail.com', '2022-12-13 13:45:06', '2022-12-13 13:46:22'),('1', 'pratiksha@gmail.com', '2022-12-19 11:45:30', '2022-12-19 11:45:36')] 

conn.executemany(sigin_query,singin_members)
conn.commit()

conn.close()