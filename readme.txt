Build and Deploy Process
------------------------
See https://packaging.python.org/tutorials/packaging-projects/ for a tutorial.

Update Tools
------------
python3 -m pip install --upgrade setuptools wheel
python3 -m pip install --upgrade twine

Run Tests
---------
python3.7 setup.py test

Build Deployment
----------------
python3 setup.py sdist bdist_wheel

Upload to PyPi
--------------
To live
    python3 -m twine upload dist/*
To test
    python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

Installing in Consuming Environment
-----------------------------------
From Live PyPi
    sudo pip3 install decawave-1001-rjg

From Test PyPi
    sudo pip3 --index-url https://test.pypi.org/simple/ decawave-1001-rjg