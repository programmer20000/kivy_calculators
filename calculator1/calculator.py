from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.core.window import Window

Builder.load_file("RootLayout.kv")
Window.size = (400, 500)


class RootLayout(BoxLayout):
    pass


class MAIN(MDApp):
    def build(self):
        self.title = "Calculator"
        self.theme_cls.theme_style = "Dark"
        return RootLayout()


if __name__ == '__main__':
    MAIN().run()
