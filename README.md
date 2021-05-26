# python_ml_ds
for https://www.udemy.com/course/python-for-machine-learning-data-science-masterclass course

sa naredbom pipenv install -r requirements.txt
instaliras sve dependecije iz requirements.txt-a u pipfile

sa naredbom iz pipfilea kreiras requirements.txt
pipenv lock -r > requirements.txt

-------
moras iskljuciti auto save za jupyter fajlove, kako bi fukcioniralo spremanje
u user settings.json iznad
"files.autoSave": "onFocusChange",

dodas

"files.exclude": {
    "**/.ipynb": true,
},

------------------

ako napravis discard changes, moras zatvoriti otvoreni ipynb fajl i opet ga otvoriti

------
