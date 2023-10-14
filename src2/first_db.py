from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        conn = sqlite3.connect('first_db.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE if not exists customers(
        			name text)
        		 """)
        conn.commit()
        conn.close()

        return Builder.load_file('first_db.kv')

    def submit(self):
        input_text = self.root.ids.word_input.text.strip()  # Remove leading/trailing whitespaces
        if input_text:
            # Create Database Or Connect To One
            conn = sqlite3.connect('first_db.db')

            # Create A Cursor
            c = conn.cursor()

            # Add A Record
            query = f"INSERT INTO customers VALUES ('{input_text}')"
            c.execute(query)

            # Add a little message
            self.root.ids.word_label.text = f'{input_text} Added'

            # Clear the input box
            self.root.ids.word_input.text = ''

            # Commit our changes
            conn.commit()

            # Close our connection
            conn.close()

    def show_records(self):
        # Create Database Or Connect To One
        conn = sqlite3.connect('first_db.db')

        # Create A Cursor
        c = conn.cursor()

        # Grab records from database
        c.execute("SELECT * FROM customers")
        records = c.fetchall()

        word = ''
        # Loop thru records
        for record in records:
            word = f'{word}\n{record[0]}'

        # Set label text outside the loop
        self.root.ids.word_label.text = word

        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()

MainApp().run()
