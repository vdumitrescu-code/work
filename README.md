**Django with Highcharts**

Short project demonstrating the integration of Highcharts with Django

### Database
[Please take note that the data is already imported in the db.sqlite3 file.]

[Full details on how to reproduce this are below.]

The default, sqlite3, database was used for storing the data.

You can check if the database has values with these commands:
* Install sqlite3 on your system if needed:
```sqlite
sudo apt install sqlite3
```
* Enter the sqlite3 CLI:
```sqlite
sqlite3 -column -header
```
* Import work/db.sqlite3 into the database first:
```sqlite
.open "/home/uer/work/db.sqlite3"
```
* Check for tables and run a simple select:
```sqlite
.tables
```

If no data is present then we need to tell Django to load our data from our fixtures.

The fixtures are located in the /work/fixtures directory.
* Enter the Terminal in /work and run:
```django
python manage.py loaddata fixture_name
```

You can now check in sqlite3 to see if the data was sent.

### Django

We are now ready to start our application.

* In the /work directory, run the server with:
```django
python manage.py runserver
```
* You can now check http://127.0.0.1:8000/

* You use the credentials for the existing superuser for Log In:
```django
username: sw
pass 12345
email: test@django.com
```
* Or create your own user with the Sign Up button:
```django
Enter your username and password and then click Sign Up.
You are now redirected to the Login Page, enter your credentials.
```
* You should now be able to view the Highcharts.
* Here you can either Log Out or Reset Password.
```django
Please take note that the Reset Password is not fully implemented.
A fake email will be sent in the /work/send_emails directory for further details.
```