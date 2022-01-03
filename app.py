from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## About
from pages.about.about import about
app.register_blueprint(about)

## singin
from pages.singin.singin import singin
app.register_blueprint(singin)

## registered
from pages.registered.registered import registered
app.register_blueprint(registered)

## contact
from pages.contact.contact import contact
app.register_blueprint(contact)

## courses
from pages.courses.courses import courses
app.register_blueprint(courses)

## QA
from pages.QA.QA import QA
app.register_blueprint(QA)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)
