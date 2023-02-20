# portfolio_mgmt!


![image](https://user-images.githubusercontent.com/83510494/220034577-caaa7780-0fe1-44cd-bb72-9d3de60754dc.png)

To install the dependencies for the project, go to the root directory 
 - first: install pipenv
 - on root directory: pipenv sync 

To run the development server
- cd portfolio_mgmt
- python manage.py runserver

Swagger Api Documentation
- http://127.0.0.1:8000/api/docs/

Silk UI to review the db queries 
- http://127.0.0.1:8000/silk/

Database models for the portfolio and project on : root/portfolio_mgmt/portfolio/models.py

Serialization is done with rest framework serializers:  root/portfolio_mgmt/portfolio/serializers.py

Viewset logic is on :  root/portfolio_mgmt/portfolio/views.py

To refer the Thames only email validation system: root/portfolio_mgmt/users/serializers.py
