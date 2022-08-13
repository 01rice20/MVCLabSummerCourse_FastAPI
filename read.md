
# FastAPIHomework
	

	## Description
	### Welcome! This is 2022 MVCLab Summer training homework, it simulates a company's employee database, and supports finding the best available employee at the moment
	

	### Setup Guide
	* **How to run**
	    * **Step 1: Install Python Packages**
	        * > pip install -r requirements.txt
	    * **Step 2: Run by uvicorn (Localhost)**
	        * > uvicorn main:app --reload
	        * Default host = 127.0.0.1, port = 8000
	    * **Step 3: Test your API using Swagger UI**
	        * http://127.0.0.1:8000/docs
	

	

	## JSON Object Data Structure
	### Fields
	* id: int = Product's number
	* name: Union [str, None] = None, product's name
	* price: int = product's price
	* calories: float = product's calories
	* sugar_content: float = product's sugar content
	

	## Fuctions
	### GET 
	    * > /all-products
	        * Show all products' name
	    * > /over-calories/{int}
	        * Show all products that calories are over {int}
	    * > /find-drinks/{int}
	        * Every drinks got an ID, enter number 1-7 to check out detail infos of all drinks
	### POST 
	    * > /highest
	        * Show the highest calories drinks
	    * > /upload
	        * Upload a file to the server

