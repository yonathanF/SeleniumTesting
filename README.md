# CS 4501 Software Testing 
## Selenium Testing, Extra Credit 

### Getting started 
1. Clone the repo
2. Install needed packages with pip
  ```python 
  pip install -r requirements.txt
  ```
3. Migrate DB using: 
    ```python 
    python manage.py makemigrations
    python manage.py migrate
    ```
4. Insert data using fixture provided 
    ```python 
    python manage.py loaddata fixture.json
    ```
5. [Optional] Run server
    ```python 
    python manage.py runserver
    ```
6. [Demo] Run tests
    ```python 
    python manage.py test selenium_tests
    ```
    
#### Notes
If you change the project structure, please make sure you are in the right dir when running manage.py
