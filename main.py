from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from learny import clozetest, wordsearch, PresentOrPast, colorsyllables, infinitive, specialwords


KV = '''
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: "vertical"

                    MDToolbar:
                        title: "Menü"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    MDTextField:
                        id: input
                        hint_text:"Text eingeben"
                        pos_hint: {"center_y": .5, "center_y": .5}
                        multiline: True
                        halign: "center"



                    MDRaisedButton:
                        text: "Lückentext"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 1, 1
                        md_bg_color: 1, 0, 1, 1
                        on_press: app.clozeTest(input.text)
                    MDFlatButton:
                        text: "Suchsel"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 1, 1
                        on_press: app.wordSearch(input.text)
                    MDFlatButton:
                        text: "Zeitformen"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 1, 1
                        on_press: app.presentOrPast(input.text)
                    MDFlatButton:
                        text: "Infinitiv"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 1, 1
                        on_press: app.infinitiveGet(input.text)
                    MDLabel:
                        text: ""
                        halign: "center"

    MDNavigationDrawer:
        id: nav_drawer
        ContentNavigationDrawer:




'''
#Builder.load_file("/home/alex/kivytest/testmd.kv")
class ContentNavigationDrawer(BoxLayout):
    pass
class Glearny(MDApp):

    def pow(self):
        print("OK")
    def clozeTest(self, inputfield):
        clozetest.cloze_test(inputfield, "Sprache: Deutsch")
    #wordsearch
    def wordSearch (self, inputfield):
        words = specialwords.nouns(inputfield, "Sprache: Deutsch")
        wordsearch.wordsearch(words)

    def presentOrPast (self, inputfield):
        PresentOrPast.present_or_past(inputfield, "Sprache: Deutsch")

    #def infinitive
    def infinitiveGet(self, inputfield):
        infinitive.infinitive(inputfield, "Sprache: Deutsch")


    def build(self):
        self.icon = '/home/alex/kivytest/learny.png'

        return Builder.load_string(KV)


Glearny().run()
