# To-do →Flask App

## Contents

## Project specification

The specification for this project was to create a CRUD app using the python framework Flask. It had to use Flask-SQLAlchemy and mySQL for configuring the database. The app had to be uploaded to a GitHub repository using Git commands and be available for the instructors to see what you did and the evidence of that work.

The project had to have a Cloud instance up and running with Ubuntu version 18.04. This was used throughout the Bootcamp and so I was familiar with it. We had to install and run Jenkins on our instance and then show a live example of the Flask website.

## Initial project

The initial project was to create a Quiz app which would meet most of the requirements of the specification. However this did not end up working as whilst I was working with my code on the GCP Ubuntu instance, it corrupted and would not allow me access to it. This was because I was installing Jenkins onto that instance in order to practice on the software, in order to be fully ready on the day of the demo.

This lead to the loss of all of my work thus far and as this was on the last day to complete the project and what I already has was quite complex to finish I decided that I had to restart the entire project for a chance of passing.

Here are some of the Diagrams that I created and the state of the Kanban Board when my instance failed:

### Kanban Board

[Quiz app project](https://www.notion.so/cecb90a6322446e99fc96d1bd11a8fe7)

[]()

### Wireframes of the Website
![alt text](C:\Users\Code\Downloads\ERD_Quiz_template.jpeg)
![To-do%20%E2%86%92Flask%20App%20f57c6a8556ed4d19932cdb61be4053b4/Quiz_app_wireframe_(1).jpeg](To-do%20%E2%86%92Flask%20App%20f57c6a8556ed4d19932cdb61be4053b4/Quiz_app_wireframe_(1).jpeg)

### Database Diagram
![alt text](C:\Users\Code\Downloads\ERD_Quiz_template.jpeg)

### Risk Assessment

[Quiz App → Risk Assessment](https://www.notion.so/31abe604815d4f21af54e07cd1628e28)

## To-do → Project

### Introduction

This new project was very time constrained; the time limit is a day. thus the project chosen was a CRUD to-do app. submitted to GitHub. The aim is to create a basic flask app, with CRUD functionality. Thus I am also only using one webpage which has editing functionality. 

### Kanban Board

The tasks set for this are very basic as I didn't have a lot of time for planning.

[To-do App](https://www.notion.so/a38ef866df3840ee99a26d79510ea911)

[Set up a GCP Instance and install the basic dependencies → not installing Jenkins](https://www.notion.so/Set-up-a-GCP-Instance-and-install-the-basic-dependencies-not-installing-Jenkins-0023f29b853a481fb2fe3a5925bcde2b)

### To-do → wireframe

![To-do%20%E2%86%92Flask%20App%20f57c6a8556ed4d19932cdb61be4053b4/Todo_wireframe.jpeg](To-do%20%E2%86%92Flask%20App%20f57c6a8556ed4d19932cdb61be4053b4/Todo_wireframe.jpeg)

### Risk Assessment

It is the same as the last project and hasn't changed

### Developing the project

The main [app.py](http://app.py) was made as a basic Flask app:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # this is the home page 
    return render_template('index.html', incomplete=incomplete, complete=complete)

# run the app with debug true
# on the localhost and at port 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
```

There was a simple html template and that was developed to look like the wireframe. 

There was also a simple database class:

```python
class Todo(db.Model):
    # has the is as primary key
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    # the text of teh task can be a max of 75 chars long
    text = db.Column(db.String(75), nullable=False)
    # is the task completed??
    complete = db.Column(db.Boolean, nullable=False)
```

As you can see the database only had one table and it only had three elements; id, text and complete. The id is needed as a unique identifier, that is needed if more tables were added for the authentication.

### Tests

The tests done to this project was a simple get request check, but the lack of time to do more prevented there from being a coverage report. This is an example of a test case:

```python
class TestAccess(TestBase):
    # check that the page access was successful
    def test_access_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

class TestAdd(TestBase):

    def test_add_post(self):
        response = self.client.post(
            url_for('home'),
            data=dict(todolist="mow the lawn"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
```

## Conclusion

I believe that had I accounted for more safety measures I could have finished this task a lot better. There was clear need of more tests and overall functionality. Overall this has allowed me to not underestimate any other work I have to do in the future and I will make sure there is more success to be had in those projects.

## Acknowledgements

This was made whilst on the GMCA DevOps Bootcamp provided my QA. I received tutorials from the instructors on most things covered in this application.
