from kivymd.app import MDApp
from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder
from functools import partial

class MyApp(MDApp):
    def build(self):
        self.load_text()
        return Builder.load_file('main.kv')
        # return self.root

    def update_label(self, request, result):
        self.root.ids.label.text = result

    def load_text(self):
        UrlRequest('http://127.0.0.1:5000/', on_success=self.update_label)

if __name__ == '__main__':
    MyApp().run()
