# flask-boilerplate

> TODO

### Documentation

* [Flask](http://flask.pocoo.org)
* [Python setup](doc/python.md)

### Setup

```
# create virtualenv
virtualenv -p $(which python3) env

# activate virtualenv
source env/bin/activate

# deactivate virtualenv
deactivate

# install requirements
pip install -r requirements.txt

# verify code
pylint app.py
find . -iname "*.py" | xargs pylint
```
