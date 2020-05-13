# Python-Flask-REST-API

Simple prototype for a Python Books Web API using Flask. 
The objective of this proof of concept API will be to have the capability of writing to most SQL databases.

## How to run

Run the application
<code>
  python main.py
</code>

The API is running on a given host and port specified on the config.ini file. You can test using your browser or an application like Postman.

The API can now support different SQL databases by simply configuring the DATABASE_CONNECTION_URI parameter.

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