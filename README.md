# Flask Examples from the Internet

## FlaskCRUD-master
Demonstrates a CRUD application with a Sqlite datastore. Access is synchronous as does not use AJAX.
https://medium.com/technest/build-a-crud-app-with-flask-bootstrap-heroku-60dfa3a788e8


## flaskmvc-master
Demonstrates wiring routes, in the form of blueprints, to controllers in separate modules. 
It can be difficult to pass `app` between modules in this project because the `app.py` file is at the same level as the controllers, rather than above a package containing the controllers.
https://github.com/sheetalkumar105/flaskmvc


## flask-mvc-master
Demonstrates 
* Reading multiple controllers in an MVC application. 
* Placing the starting .PY above a package containing all other files.


## project-dream-team-two-master
CRUD with Python 2
Demonstrates
* Login
* Admin User
* Admin Dashboard
* Sqlite
https://github.com/mbithenzomo/project-dream-team-two


## project-dream-team-three-master
A follow-up to project-dream-team-two-master
CRUD with Python 2
Demonstrates
* Custom error pages
https://github.com/mbithenzomo/project-dream-team-three
https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-three 


# My Project

## SubDocReview
Demonstrates 
* Importing of `app` between modules, as well as the use of `current_app`. 
* Demonstrates reading a pandas dataframe when starting the server. 
* Sqlite database.
* Reading multiple controller modules from the `controllers` pack using `__all__`.

### Idea for alternative method of passing `app`. 
Notice that flaskmvc uses `mongo = PyMongo(app)`, and FlaskCRUD uses `db = SQLAlchemy(app)`. It might be worth trying `Document(app)`.

### IP Addresses
Windows does not seem to like host `0.0.0.0`. Try `127.0.0.1`. 