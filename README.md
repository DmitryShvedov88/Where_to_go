## My new app "Where to go" as part of the Django ORM course.
#### "Where to go" 
A small telegram bot that sends you the results of checking your lessons.

#### To clone repo:
```git clone https://github.com/DmitryShvedov88/Poster-on-the-map.git```

#### Environment variables:
You should have:
1. SECRET_KEY - it's Django security key/ 
2. DEBUG - True/False, debug mode
3. ALLOWED_HOSTS - List of hosts that will serve the site

#### How to install requirements
1. Python3 should already be installed.  
2. Use pip (or pip3, if there is a conflict with Python2) to install dependencies. 
  
```pip install -r requirements.txt```

#### Make migrations

```python manage.py migrate```

#### How to start:

```python manage.py runserver```

#### Crate superuser

```python manage.py createsuperuser```

Now you can add some places in admine pannel.
Go to http://127.0.0.1:8000/admine
You have several tabs where you can add coordinates, photos, description of an interesting place.

After all you can go to http://127.0.0.1:8000/
And find your places.

![alt text](image.png)

#### My site example

https://dmitryshvedov88.pythonanywhere.com/

#### Project Goals 
**This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/modules/).**