# django_library_project  

## Study "Library" project on Django  

**Requirements:**  
Python & PostgreSQL installed  

**Install instructions:**  
- Install PostgreSQL  
- Create and activate a virtual environment:  
> \>>> py -m venv <venv_name>  
> \>>> <venv_name>\Scripts\activate  
- Install dependencies:  
> \>>> pip install -r requirements.txt  
- Set up a Django project:  
> \>>> py manage.py migrate  
> \>>> py manage.py createsuperuser  
- In pgAdmin4 create and set up a PostgreSQL DB with keys from DATABASES object in settings.py
- Populate DB:  
> \>>> python manage.py loaddata my_data.xml  

**Usage:**  
- Run server:  
> \>>> py manage.py runserver  

- Admin page:  
> http://127.0.0.1:8000/admin/  

- General library page:  
> http://127.0.0.1:8000/index/  

- List of authors:  
> http://127.0.0.1:8000/authors/  

- List of publishers:  
> http://127.0.0.1:8000/publisers/

- You can create authors and books:  
> http://127.0.0.1:8000/author/create/  

> http://127.0.0.1:8000/author/create_many/  

> http://127.0.0.1:8000/author_book/create_many  
