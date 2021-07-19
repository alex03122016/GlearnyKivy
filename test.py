from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from learny import clozetest, wordsearch, PresentOrPast, colorsyllables, infinitive, specialwords
from kivy.config import Config


"""
    This is the gui with kivy without "MD" style and without the .kv language. 

"""
class InputScreen(GridLayout):

  def __init__(self, **kwargs):
	  super(InputScreen, self).__init__(**kwargs)
	  self.cols = 1
	  self.add_widget(Label(text='Hier können Sie Ihren Text einfügen.'))
	  self.username = TextInput(multiline=True)
	  self.add_widget(self.username)

	  self.Lueckentext_Btn = Button(text='Lückentext')
	  self.Lueckentext_Btn.bind(on_press=self.clozeTest)
	  self.add_widget(self.Lueckentext_Btn)

	  self.wordSearch_Btn = Button(text='Suchsel')
	  self.wordSearch_Btn.bind(on_press=self.wordSearch)
	  self.add_widget(self.wordSearch_Btn)

	  self.presentOrPast_Btn = Button(text='Zeitformen')
	  self.presentOrPast_Btn.bind(on_press=self.presentOrPast)
	  self.add_widget(self.presentOrPast_Btn)

	  self.infinitiveGet_Btn = Button(text='Infinitiv')
	  self.infinitiveGet_Btn.bind(on_press=self.infinitiveGet)
	  self.add_widget(self.infinitiveGet_Btn)

  def clozeTest(self, instance):
	  clozetest.cloze_test(self.username.text, "Sprache: Deutsch")
#wordsearch
  def wordSearch (self, instance):
	  words = specialwords.nouns(self.username.text, "Sprache: Deutsch")
	  wordsearch.wordsearch(words)

  def presentOrPast (self, instance):
	  PresentOrPast.present_or_past(self.username.text, "Sprache: Deutsch")

#def infinitive
  def infinitiveGet(self, instance):
	  infinitive.infinitive(self.username.text, "Sprache: Deutsch")

class Glearny(App):

  def build(self):
	  self.icon = '/home/alex/kivytest/learny.png'
	  return InputScreen()

if __name__ == '__main__':
  Glearny().run()
