#!
#install

mkdir kivytest
cd kivytest
virtualenv -p python3.8 venv

. home/alex/kivytest/venv/bin/activate
#install kivy
pip install kivy
#install spacy
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download de_core_news_sm
#install python-docx
pip install python-docx
#run kivy version
python test.py
#run kivyMD version
python main.py
