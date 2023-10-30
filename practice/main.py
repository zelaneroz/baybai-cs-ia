from kivymd.app import MDApp
from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder
from functools import partial
import json
import urllib.parse
PATH = 'http://127.0.0.1:5000/'
class MyApp(MDApp):
    def build(self):
        self.load_text()
        return Builder.load_file('main.kv')
        # return self.root

    def update_label(self, request, result):
        print(result)
        self.root.ids.label.text = result

    def update_response_label(self, request, result):
        print('Result: ', result)
        self.root.ids.response_label.text = result

    def send_data(self):
        text = self.root.ids.text_input.text
        #self.root.ids.text_input.text returns a string even you input a number. You need to explicitly do int() or float()\
        encoded_data = json.dumps(text)
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        UrlRequest('http://127.0.0.1:5000/send_text', method ='POST', on_success=self.update_response_label, req_body=encoded_data, req_headers=headers)

        #SAME METHOD IN MAIN.PY AND SERVER.PY FOR ANY DATA TYPE, WHEN SENDING DATA TO SERVER AND THEN BACK TO CLIENT
        # !--- MDLABEL only accepts string so turn result to str in update_label method----!

    def load_text(self):
        UrlRequest('http://127.0.0.1:5000/', on_success=self.update_label)

    def get_string(self):
        UrlRequest('http://127.0.0.1:5000/get_string', on_success=self.update_response_label)

if __name__ == '__main__':
    MyApp().run()

#
