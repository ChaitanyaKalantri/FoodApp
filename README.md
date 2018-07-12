# FoodApp

## Introduction:
The purpose of this project is to develop a Online Food Ordering Application. It is an application that enables customers to place their order online at any time and place. Besides that it provides a user friendly web pages, and attractive graphics. The basic layout of the application is as follows. Initially the customer will have to select the Restaurant name from which he/she wants to order. Then, the Customer will have to select the Category of food he/she wants to order (Breakfast, Lunch or Dinner). Based on that the next page will show the corresponding items, from which the customer can chose which ever items he/she wants. Hence, the order is successfully placed. Once the order is placed, the customer will get the unique order id number. Which the user can enter to get the details of the food items placed.


## Specifications:
1. Programming Languages used - ***Python***
2. Scripting languages used - ***HTML***
3. UI/UX Python library used - ***Flask***
4. Backend used - ***Mysql***


## Steps to Install:
1. Install Python
	- Install Python version 2.7
		[https://www.python.org/downloads/]
	- In case, you have Python version 3 and above.
	You can execute the project using "conda environment"
	Use the below commands:
		(i) conda create -n zappos python=2.7 anaconda
			To create the conda environment
		(ii) source activate zappos
			To activate the conda environment
2. Install Flask:
	- Install flask from command line:
		`sudo pip install Flask`
	- In case, if that doesn't work and you don't have pip installed; then go through the following steps:
		[http://www1.cmc.edu/pages/faculty/alee/cs40/penv/installFlaskOnMac.html]
3. Install Mysql:
	- Install mysql using command line:
		`pip install Mysql-python`
	- If this doesn't work, then try: (assuming brew is installed already)
		`brew install mysql`
		`sudo pip install MySQL-python`


## Steps of execution of the project:
Once the installation is complete: download the complete folder "ZapposFoodApp" from GITHUB
1. First open the command prompt and go to the directory location of 'ZapposFoodApp' folder.
	- To verify: when you type 'ls'; it should contain all the python files and the template, static, test folders.
2. Get into the mysql terminal:
	- Type the following commands
	(i)	mysql -uroot
	(ii) create database pythonroot
	(iii) Now come out of the mysql terminal: Command+D
3. Execute this command to create and load the database tables. Please note that we are using MqSQL database.
	- python createdb.py
4. Now execute this command:
	- python index_startApp.py
5. Then, paste the URL " http://127.0.0.1:5002/ " in the browser to place the order.
6. Now there are two parts:
	(i)	Place the order as per the available food items at various restaurants.
	(ii) Add the item in the revelant restaurant

## Brief description:
### For placing the order:
1. Click on ***"Do you want to place the order?"*** submit button.
2. Then simply follow the steps
3. Once the order is placed, an ***Order ID*** is generated. With the help of Order ID the user can check the items he/she has placed.
4. You are all done!
5. In case, if you want to place a ***new order or edit*** the same order. You can add your "OrderId" generated on the successful order placed page. And then click on "Want to edit the order?" submit button.
6. You will be redirected to the front page. And you can follow the same procedure.

### For adding the item in the revelant restaurant: 
1. Click on ***"Do you want to add the item?"*** submit button.
2. Then for ***logging*** in, use the following credentials.
	UserName: Zappos
	Password: Family
	I have hard coded these parameters because there can just be a single owner of the company, which can add the items.
3. Then simply follow the steps
4. You are all done!


## Testing Phase:
I have created the "testcreatedb.py" file. The testing file is present in the "test" folder.
To execute the file, follow the below mentioned steps:
1. First open the command prompt and go to the directory location of 'ZapposFoodApp' folder.
	To verify: when you type 'ls'; it should contain all the python files and the template, static, test folders.
2. Now, excute this command "python tests/testcreatedb.py"
	It will test whether the file is running properly or not
	If the file is running properly you will be able to get the output
