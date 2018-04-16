from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)

#Declared global orderid; as I am assuming that once the application is running online it won't stop in between
orderid = 0

# This method will display all the names of the restaurant to the user
# The python flask logic will take the help of index.html page to display the restaurant names
@app.route("/")
def Restaurant():
	db_connect = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")
	conn = db_connect.cursor()
	s = "starting point"
	return render_template("active.html", result = s)

# This method will first check if the return value is item; that means it has the list of all the items and hence this will have its own logic
# The python flask logic will take the help of success.html page to display the item names selected
# In the elif part; we will check if the return valu is order; then we will display the showOrder.html page, rest all is self explanatory
# And finally in else logic, we have two parts:
# Based on the return type of the return type, which I am storing it in variable "rest"; if the type of rest is int, then try logic will be executed
# and the menuItems.html page will be called
# Otherwise, the except ValueError will be executed and this will execute the menu.html page
# Rest the logic part of all the functions is just to get the revelant values from the respective tables stored in the mysql database and display them using html pages

@app.route("/", methods= ['PUT'])
def insert(table, fields=(), values=()):
    # g.db is the database connection
    cur = g.db.cursor()
    query = 'INSERT INTO %s (%s) VALUES (%s)' % (
        table,
        ', '.join(fields),
        ', '.join(['?'] * len(values))
    )
    cur.execute(query, values)
    g.db.commit()
    id = cur.lastrowid
    cur.close()
    return id


@app.route("/", methods=['DELETE'])
def Edit():
	global orderid
	db_connect = MySQLdb.connect(host="localhost", user="root", db="pythonspot")
	conn = db_connect.cursor()

	if reques.form.get('editMain'):
		global orderid
		orderId = request.form.get('edit')
		query = "DELETE from OrderItem where order_id = %s"
		conn.execute(query, (orderid,))
		db_connect.commit()
		s = "success"
		return render_template("main.html", result = s)



@app.route("/", methods=['GET','POST'])
def Menu():
	global orderid
	db_connect = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")
	conn = db_connect.cursor()

	if request.form.get('item'):
		result = request.form.getlist('item')
		query = conn.execute("select max(order_id) from OrderItem")
		maxid = conn.fetchall()[0][0]
		print("maximum orderid  " + str(maxid))
		if maxid == None:
			orderid = 1
		else:
			orderid = int(maxid) + 1

		print(orderid)
		for item in result:
			conn.execute (" INSERT INTO OrderItem VALUES (%s, %s) ", (orderid, item ))
		db_connect.commit() 
		
		return render_template("success.html", result=orderid )
	elif request.form.get('place'):
		query = conn.execute("select * from Restaurant")
		result = {'Restaurant': [i[1] for i in conn.fetchall()]}
		return render_template("index.html", result = result)
	elif request.form.get('add'):
		s = "login"
		print("Inside login")

		return render_template("login.html", result = s)
	elif request.form.get('login'):
		print("login")
		name = request.form.get('Username')
		passw = request.form.get('Password')
		print(name)
		print(passw)
		s = "Wrong UserName or Password"
		if name == "Zappos":
			if passw == "Family":
				query = conn.execute("select * from Restaurant")
				result = {'Restaurant': [i[1] for i in conn.fetchall()]}
				return render_template("resMenu.html", result = result)
		else:
			return render_template("login.html", result = s)

	elif request.form.get('resMenu'):
		
		rest = request.form.get('resMenu')
		print(rest)
		
		try:
			print("Menu")
			rest = request.form.get('resMenu')
			sql_string = "select * from Menu where restaurant_id = ( select restaurant_id from Restaurant where name = '%s' )"
			query = conn.execute( sql_string % rest)

			result = {rest: [(int(i[0]), i[2]) for i in conn.fetchall()]} # Fetches first column that is Employee ID
			print("In Menu")
			print(result)
			return render_template("addMenu.html", result = result)
		except ValueError:
			print("Menu Items")
			#query = conn.execute("select * from MenuItems where menu_id = %d " % int(rest) ) 
			#result = {'MenuItems': [i[2] for i in conn.fetchall()]} # Fetches first column that is Employee ID
			#print(result)
			s = "Works"
			return render_template("addMenuItem.html", result = s)
	elif request.form.get('addMenu'):
		print("addMenuItem")
		restaurantName =  request.form.get('restaurant')
		category = request.form.get('addMenu')
		#query = conn.execute("select max(order_id) from OrderItem")
		#print(query)
		return render_template("addMenuItem.html", result=[category, restaurantName] )

	elif request.form.get('addMenuItem'):
		itemname = request.form.get('itemname')
		cuisine = request.form.get('cuisine')
		restaurantName = request.form.get('restaurant')
		menu_id = request.form.get('category')
		print("In Menu Items")
		print(itemname)
		print(cuisine)
		print(restaurantName)
		print(menu_id)
		mid = int(menu_id)
		query = conn.execute( "select category from Menu where menu_id=%d" % mid )
		category = conn.fetchall()[0][0]
		conn.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (mid, category, itemname, cuisine))
		db_connect.commit()

		return render_template("successfullyInserted.html" )
	elif request.form.get('order'):
		orderID = request.form['order']
		#query = conn.execute("select max(order_id) from OrderItem")
		#print(query)
		print("Order Items")
		query = conn.execute("select * from OrderItem where order_id = %d " % int(orderID) ) 
		result = {'OrderItems': [i[1] for i in conn.fetchall()]}
		return render_template("showOrder.html", result=result )
	elif request.form.get('edit'):
		global orderid
		orderId = request.form.get('edit')
		query = "DELETE from OrderItem where order_id = %s"
		conn.execute(query, (orderid,))
		db_connect.commit()
		s = "success"

		'''
		elif request.form.get('edit'):
		orderID = request.form['edit']
		#query = conn.execute("select max(order_id) from OrderItem")
		#print(query)
		print("Edit Items")
		query = "DELETE FROM OrderItem WHERE order_id = %s"
        conn.execute(query, (order_id,))
        db_connect.commit()
        return render_template("main.html", result=result )
		'''

		return render_template("main.html", result = s)
	elif request.form.get('start'):
		query = conn.execute("select * from Restaurant")
		result = {'Restaurant': [i[1] for i in conn.fetchall()]}
		return render_template("index.html", result = result)
	elif request.form.get('order'):
		orderID = request.form['order']
		#query = conn.execute("select max(order_id) from OrderItem")
		#print(query)
		print("Order Items")
		query = conn.execute("select * from OrderItem where order_id = %d " % int(orderID) ) 
		result = {'OrderItems': [i[1] for i in conn.fetchall()]}
		return render_template("showOrder.html", result=result )
	else:
		rest = request.form['r']
		rest = rest.strip()
		print(rest)
		print(request.method)
		try:
			print("Menu Items")
			query = conn.execute("select * from MenuItems where menu_id = %d " % int(rest) ) 
			result = {'MenuItems': [i[2] for i in conn.fetchall()]} # Fetches first column that is Employee ID
			#print(result)
			return render_template("menuItems.html", result = result)
		except ValueError:
			print("Menu")
			sql_string = "select * from Menu where restaurant_id = ( select restaurant_id from Restaurant where name = '%s' )"
			query = conn.execute( sql_string % rest)

			result = {'Menu': [(int(i[0]), i[2]) for i in conn.fetchall()]} # Fetches first column that is Employee ID
			print(result)
			return render_template("menu.html", result = result)

# The application will run on port number 5002
if __name__ == "__main__":
	app.run(port=5002)
