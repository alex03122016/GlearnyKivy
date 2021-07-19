def language_load(language):
	import spacy #code: pip install spacy
	#load language from kivy to spacy
	lang = ""
	if language == "Sprache: Deutsch":
		lang = "de_core_news_sm"
	elif language == "Sprache: Englisch":
		lang = "en_core_web_sm"
	else:
		print(	"You didn't choose language. I will select german as language."
				+ "\n"*5)
		lang = "de_core_news_sm"

	#bundle_dir = pyinstaller --onefile --hidden-import="/home/alex/Dokumente/guis/venv/lib/python3.8/site-packages/de_core_news_sm" --hidden-import="/home/alex/Dokumente/guis/venv/lib/python3.8/site-packages/de_core_news_sm-3.1.0.dist-info" glearny.py
	#nlp = spacy.load(bundle_dir + lang)

	"""from pathlib import Path
	bundle_dir = Path(__file__).parent.absolute()
	nlp = spacy.load(bundle_dir / "de_core_news_sm")"""

	nlp = spacy.load(lang)
	return nlp
