# flask-boilerplate

Documentation

* [Flask](http://flask.pocoo.org)

### Setup

```
# create
virtualenv -p $(which python3) venv

# activate virtualenv
source venv/bin/activate

# deactivate virtualenv
deactivate

# install requirements
pip install -r requirements.txt
```

### Development

```
# install package
pip install Flask
pip install pylint

# update requirements
pip freeze > requirements.txt

# run tests
python tests/application_test.py
python setup.py test

# linting
pylint application/main.py
find ./application -iname "*.py" | xargs pylint

# install the application
pip install --editable .
pip install -e .

# clean cached files
rm -fr .eggs/ *.egg-info */__pycache__/

# run in debug
export FLASK_APP=application
export FLASK_DEBUG=1
flask run
```

### Docker

```
TODO
```
