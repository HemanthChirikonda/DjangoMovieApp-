Movie Full Stack App

Contents
Initial Setup Instructions
Running Server

Initial Setup Instructions

Setup Python Virtual Environment

python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt

Running Server
./mange.py migrate
./mange.py runserver

Go and check http://127.0.0.1:8000/