

# install flask_babel==2.0.0
pip3 install flask_babel==2.0.0


# extract all the translatable messages\
# from Python and HTML files
# create (messages.pot file)
pybabel extract -F babel.cfg -o messages.pot .


# create Translation Files (create .po files)
pybabel init -i messages.pot -d translations -l en
pybabel init -i messages.pot -d translations -l fr


# compile Translations(create .mo files)
pybabel compile -d translations


# to translate use
curl -H "Accept-Language: fr" http://127.0.0.1:5000/