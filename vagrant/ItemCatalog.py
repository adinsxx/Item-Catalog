from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, ListItems, User
from flask import session as login_session
import random
import string

# IMPORTS FOR THIS STEP
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

# Connect to Database and create database session
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create anti-forgery state token

#DISCONNECT - Revoke a current user's token and reser their login_session.

# JSON APIs to view Category Information

# Show all categories

# Create a new category

# Edit a category

# Delete a category

# Show a category

# Create a new list item

# Edit a list item

# Delete a menu item

#Clear the session
