from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import MDScreen
import sqlite3
from kivy.network.urlrequest import UrlRequest
import json

class MyApp(MDApp):
    def build(self):
        self.init_local_database()
        screen = MDScreen()

        # Input Field for Notes
        self.note_input = MDTextField(
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            size_hint=(0.8, 0.1)
        )
        screen.add_widget(self.note_input)

        # Save Locally Button
        save_btn = MDFlatButton(
            text="Save Locally",
            pos_hint={'center_x': 0.3, 'center_y': 0.5},
            on_release=self.save_note_locally
        )
        screen.add_widget(save_btn)

        # Upload to Server Button
        upload_btn = MDFlatButton(
            text="Upload to Server",
            pos_hint={'center_x': 0.7, 'center_y': 0.5},
            on_release=self.upload_note_to_server
        )
        screen.add_widget(upload_btn)

        return screen

    def init_local_database(self):
        self.local_db_conn = sqlite3.connect('local_notes.db')
        self.local_db_conn.execute('''CREATE TABLE IF NOT EXISTS notes
                                      (id INTEGER PRIMARY KEY, content TEXT)''')
        self.local_db_conn.commit()

    def save_note_locally(self, instance):
        note_content = self.note_input.text
        if note_content:
            self.local_db_conn.execute('INSERT INTO notes (content) VALUES (?)', (note_content,))
            self.local_db_conn.commit()
            self.note_input.text = ''

    def upload_note_to_server(self, instance):
        note_content = self.note_input.text
        if note_content:
            encoded_data = json.dumps({'content': note_content})
            headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
            UrlRequest('http://127.0.0.1:5000/upload_note', method='POST', on_success=self.on_upload_success, req_body=encoded_data, req_headers=headers)

    def on_upload_success(self, request, result):
        print("Note uploaded successfully")

if __name__ == '__main__':
    MyApp().run()
