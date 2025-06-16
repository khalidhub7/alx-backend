python3 --version
pip3 install flask_babel==2.0.0


# format html and python files
prettier --write templates/5-index.html
autopep8 5-app.py --in-place --aggressive --aggressive


# extract msgs, init langs (en, fr)
pybabel extract -F babel.cfg -o messages.pot . && \
pybabel init -i messages.pot -d translations -l en && \
pybabel init -i messages.pot -d translations -l fr
# edit .po files, then compile translations
pybabel compile -d translations


# run app
python3 3-app.py
curl -H "Accept-Language: fr" http://127.0.0.1:5000/


# babel.cfg for task 3
: '
[python: 3-app.py]
[jinja2: templates/3-index.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
'


# workflow
: '
Request → set user → choose locale (for translations) → 
choose timezone (for time) → format time → 
render template with translations
'
