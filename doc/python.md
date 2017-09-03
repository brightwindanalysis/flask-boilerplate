## Python

* [pip](https://pip.pypa.io/en/stable/user_guide)
* [virtualenv](https://virtualenv.pypa.io/en/stable/userguide)
* [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)
* [venv](https://docs.python.org/3/library/venv.html)

### Setup

```
# install pip + setuptools
curl https://bootstrap.pypa.io/get-pip.py | python -

# upgrade pip
pip install -U pip

# install virtualenv globally 
sudo pip install virtualenv

# create virtualenv
virtualenv env
virtualenv -p python3 env
virtualenv -p $(which python3) env

# activate virtualenv
source env/bin/activate

# verify virtualenv
which python
python --version

# deactivate virtualenv
deactivate

# install new package
pip install <package>

# update requirements with new package
pip freeze > requirements.txt

# install all requirements
pip install -r requirements.txt

# generate rc file
pylint --generate-rcfile > .pylintrc
```
