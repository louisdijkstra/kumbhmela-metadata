Kumbh Mela (meta)data entry interface 
=====================================

This repository contains a simple webinterface for entering, storing and 
managing metadata for the [Kumbh Mela experiment][1].  

The interface is created using Django 1.9.4. The relational database
management system SQLite is used, since it is 1) light-weight, 2) easy 
to back-up (the entire database resides in just one file), and 
3) is portable. 

Note that this repository is available under the MIT license. 

For more information on the structure of the database and other details, have a look at the publicly available [Google Docs repository][2].  

## Getting started

The code/scripts in this project are written in Python. We require __Python 3__ to be installed. First, install `virtualenv` (if you haven't already): 

    $ pip install virtualenv 

Create a virtual environment called `kumbhmela` by typing in the main directory: 

    $ virtualenv -p python3 kumbhmela
    $ source kumbhmela/bin/activate

You can now easily install all requirements by typing

    $ pip install -r requirements.txt

## Running the webinterface

Enter the virtual enviroment `kumbhmela` we created in the previous section: 

    $ source kumbhmela/bin/activate

and run

    $ python manage.py runserver

You can access the site by opening your favorite browser and going to the address <http://127.0.0.1:8000/>. 

## Creating a back-up

The file `kumbhmela_db.sqlite3` contains the entire database. Simply copy this file to your (thumb) drive. 

## Adding data

For adding data, access the admin part of the site <http://127.0.0.1:8000/admin>. 

### How to change the database structure? 

Go the `dataentry/models.py` for changing the models (i.e., tables) and 
their fields. After making the desired changes, type 
    
    $ python manage.py makemigrations 
    $ python manage.py migrate 

The database is now updated. 

## Contact

Louis Dijkstra

__E-mail__: louisdijkstra (at) gmail.com


[1]: http://www.the-kumbh-mela-experiment.com/

[2]: https://drive.google.com/folderview?id=0B__PctoLRkFyY3lvem1TMmFZX2c&usp=sharing

