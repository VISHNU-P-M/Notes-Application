# API for Posting notes

Here you have Four APIs for getting all posted notes, creating new note, getting specific datas of note, and updating fields of that specific nore, generating jwt access and refresh token, and generating jwt access token by refreshing.
#### Call 'api/token/' POST API for creating jwt token.
#### Call 'api/token/refresh/' POST API for create access token by refresh token.
#### Call 'api/notes/' GET API for read all notes.
#### Call 'api/notes/' POST API for add creating a new note.
#### Call 'api/details/<note_id>/ GET API for read the details of the note.
#### Call 'api/details/<note_id>/' PUT API for update the feilds of the note.

## Creating Environment

Create an environment on your system

```bash
Install virtual environment:
python -m pip install --user virtualenv

Creating new environment:
py -m venv env

Activate environment:
.\env\Scripts\activate
```

## Install all requirments

Install all package that needs to run this application

```bash
pip install requirements.txt 
```

## Run Application
First you need to migrate, create a super user for creating the jwt token, and then Run

```bash
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

```