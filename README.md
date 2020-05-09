# Python-Flask-REST-API

Simple prototype for a Python Books Web API using Flask. 
The objective of this proof of concept API will be to have the capability of writing to SQL and NoSQL databases as well as for example a Kafka topic.

## How to run

Create the sqlite database
<code>
  python create_tables.py
</code>

Run the application
<code>
  python main.py
</code>

For now the API is running on 127.0.0.1:5000 (later this will be made configurable on a configuration file). You can test using your browser or an application like Postman.


## Endpoints

Get a book given its name (GET)
<code>
  /book/Harry Potter
</code>

Get all books (GET)
<code>
  /books
</code>

Create a new book (POST)
<code>
  /book/Harry Potter

  {
	"title":"Harry Potter",
	"author":"J.K. Rowling",
	"year":1998,
	"copies_sold":800000
  }
</code>

Update a book by its name (PUT)
<code>
  /book/Harry Potter

  {
	"title":"Harry Potter",
	"author":"J.K. Rowling",
	"year":2000,
	"copies_sold":800000
  }
</code>

Delete a book by its name (DELETE)
<code>
  /book/Harry Potter
</code>