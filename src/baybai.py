from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.animation import Animation
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView
import sqlite3
from kivy.utils import get_color_from_hex
from kivymd.uix.datatables import MDDataTable
from kivy.properties import StringProperty, NumericProperty
from kivy.graphics import Ellipse
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
Window.size = (375,812)
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextFieldRect, MDTextField
from syllabify import translate, syllabify
from kivymd.uix.list import OneLineListItem
import pyperclip
from kivy.clock import Clock
from encrypt import encrypt_password, check_password
from kivymd.uix.list import OneLineListItem, MDList,OneLineAvatarIconListItem, IconLeftWidget
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.graphics import Color, Line  # Import Color and Line
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import MDList

path = 'baybai.db'
currrent_user = ""
class database_handler:
    def __init__(self,namedb:str):
        self.connection = sqlite3.Connection(namedb)
        self.cursor = self.connection.cursor()

    def run_query(self, query: str):
        self.cursor.execute(query)
        self.connection.commit()
    def close(self):
        self.connection.close()
    def search(self,query:str):
        result = self.cursor.execute(query).fetchall()
        return [item[0] for item in result]

    def search2(self,query:str):
        result = self.cursor.execute(query).fetchall()
        return result

class IntroScreen(MDScreen):
    pass
    def signup_screen(self):
        self.parent.current = "SignUpScreen"

    def login_screen(self):
        self.parent.current = "LoginScreen"

class SignUpScreen(MDScreen):
    def login_screen(self):
        self.parent.current = "LoginScreen"

    def popup(self,out: str):
        self.dialog = MDDialog(text=out)
        self.dialog.open()

    def validate_register(self, uname: str, pass1: str, conpass: str):
        global path
        db = database_handler(namedb=path)
        print('!!!!!PATH: ', path)
        popup_text = ""

        if uname in db.search(f"SELECT uname FROM users WHERE uname='{uname}'"):
            popup_text += f"Username [color=0000FF]{uname}[/color] already exists."
        elif len(pass1) <= 6:
            popup_text += "\nPassword needs to be longer than 6 characters."
        elif pass1 != conpass:
            popup_text += "\nPasswords don't match."
        else:
            return True

        popup_text += "\nPlease try again."
        db.close()
        self.popup(popup_text)
        return False

    def try_register(self):
        global path
        db = database_handler(namedb=path)
        db.run_query("""CREATE TABLE if not exists users(
                        id INTEGER primary key autoincrement,
                        name TEXT not null,
                        uname TEXT not null,
                        password TEXT not null);""")
        #TAKE ALL INPUTS, VALIDATE, AND APPEND TO DATABASE
        name,uname,pass1,con_pass = self.ids.name.text,self.ids.uname.text,self.ids.password.text,self.ids.confirm_password.text

        if self.validate_register(uname, pass1, con_pass):
            db.run_query(f"INSERT INTO USERS (name,uname,password) VALUES ('{name}','{uname}','{encrypt_password(pass1)}')")
            self.popup("[color=ACFF3C]Registration completed. Welcome![/color]")
            db.close()

            self.ids.name.text,self.ids.uname.text,self.ids.password.text,self.ids.confirm_password.text="","","",""
            current_user = uname
            self.clear_inputs()
            self.parent.current = "HomeScreen"

    def clear_inputs(self):
        self.ids.name.text = ""
        self.ids.uname.text = ""
        self.ids.password.text = ""
        self.ids.confirm_password.text = ""

class LoginScreen(MDScreen):
    def popup(self,out: str):
        self.dialog = MDDialog(text=out)
        self.dialog.open()

    def signup_screen(self):
        self.parent.current = "SignUpScreen"

    def move_to_home_screen(self):
        self.manager.current = "HomeScreen"

    def validate_login(self,uname:str,passwd:str):
        global path
        db = database_handler(namedb=path)
        popup_text = ""
        if uname == "" or passwd == "":
            popup_text="Please enter required fields"
        elif uname in db.search(f"SELECT uname from users where uname='{uname}'"):
            if check_password(passwd,db.search(f"SELECT password from users where uname='{uname}'")[0]):
                popup_text = "Successfully logged in. Welcome!"
                return True, popup_text
            else:
                popup_text = "Incorrect Password. Try again."
        else:
            popup_text = "User does not exist."
        return False, popup_text

    def try_login(self):
        global path
        db = database_handler(namedb=path)
        uname,passwd = self.ids.uname.text,self.ids.password.text
        db.close()
        global currrent_user

        if self.validate_login(uname, passwd)[0]:
            currrent_user = uname
            self.popup(self.validate_login(uname, passwd)[1])
            self.parent.current = "HomeScreen"
            Clock.schedule_once(lambda dt: self.move_to_home_screen(), 2)

class HomeScreen(MDScreen):
    def tolearn(self):
        self.manager.current = 'LearnScreen'
    def home2saved(self):
        self.manager.current = "SavedScreen"
    def home2translate(self):
        self.manager.current = "TranslateScreen"
    def home2stats(self):
        self.manager.current = "StatsScreen"
    def home2net(self):
        self.manager.current = "NetworkScreen"

level = 1
label_text = ""
level_dict = {1: "About Baybayin", 2: "Tagalog Transcription and Prerequisites", 3: "Baybayin Basics",
              4: "Vowels and Kudlit", 5: "Ba,Ka,Da,Ga", 6: "Ha, La, Ma, Na, Nga", 7: "Pa, Sa, Ta, Wa, Ya",
              8: "Common Words"}


class LearnScreen(MDScreen):
    def backtohome(self):
        baybai.backtohome(self)

    def learn1(self):
        self.parent.current = 'Learn_1_1_Screen'

    def learn2(self):
        self.parent.current = 'Learn_1_1_Screen'

    def learn_gen(self, card):
        global level
        global label_text
        level_dict = {1:"About Baybayin",2:"Tagalog Transcription and Prerequisites",3:"Baybayin Basics",4:"Vowels and Kudlit",5:"Ba,Ka,Da,Ga",6:"Ha, La, Ma, Na, Nga",7:"Pa, Sa, Ta, Wa, Ya",8:"Common Words"}
        #GET THE LEVEL NAME
        for child in card.children:
            if isinstance(child, MDBoxLayout):  # Change to your actual layout if it's not MDBoxLayout
                for box_child in child.children:
                    if isinstance(box_child, MDLabel):
                        label_text = box_child.text
                        # print(print('Label Text Updated:', label_text))
                        break
        level = next((k for k, v in level_dict.items() if v == label_text), None)
        # print(label_text)
        if level<3:
            print('TBD')
        else:
            Learn_1_1_Screen.level = level
            Learn_1_1_Screen.label_text = label_text
            self.parent.current = 'Learn_1_1_Screen'
            # Learn_1_1_Screen.on_enter()

class Learn_1_1_Screen(MDScreen):
    label_text_main = StringProperty("Initial Text")

    def __init__(self, **kwargs, ):
        super().__init__(**kwargs)
        self.flashcard_contents = ['']
        self.saved_cards = []

    def on_enter(self, *args):
        global label_text
        global level
        global path
        self.label_text_main = label_text
        self.current_card_index = 0
        self.level = level
        db = database_handler(namedb=path)
        word_pairs = db.search2(f"SELECT fro,bck FROM contents where lvl is {level}")
        db.close()
        self.tagalog, self.baybayin = zip(*word_pairs)
        self.is_tagalog = True  # Initially showing Tagalog
        self.starred_states = [False] * len(self.tagalog)  # Initialize starred states for each card
        self.update_flashcard_content()

    def backtolearn(self):
        global path
        db = database_handler(path)
        existing_cards = db.search2("SELECT * FROM saved")
        for lvl, dex in self.saved_cards:
            if (lvl, dex) not in existing_cards:
                db.run_query(f"INSERT INTO saved (lvl, dex) VALUES ({lvl}, {dex})")
        db.close()
        self.parent.current = 'LearnScreen'

    def backtohome(self):
        baybai.backtohome(self)


    def next_card(self):
        self.current_card_index += 1
        if self.current_card_index >= len(self.tagalog):  # Use length of tagalog list
            self.current_card_index = 0  # Reset to the first card if we've reached the end
        self.update_flashcard_content()
        print('LEVEL: ', self.level)

    def prev_card(self):
        if self.current_card_index > 0:
            self.current_card_index -= 1
        else:
            self.current_card_index = len(self.tagalog) - 1  # Go to the last card if at the first card
        self.update_flashcard_content()

    def flip_card(self):
        self.is_tagalog = not self.is_tagalog  # Toggle between Tagalog and Baybayin
        if self.ids.card_input.md_bg_color == get_color_from_hex("#9851FF"):
            self.ids.card_input.md_bg_color = get_color_from_hex("#D346FF")
        else:
            self.ids.card_input.md_bg_color = get_color_from_hex("#9851FF")
        self.update_flashcard_content()

    def update_flashcard_content(self):
        # Update the flashcard content
        if self.is_tagalog:
            self.ids.flashcard_content.text = self.tagalog[self.current_card_index]
        else:
            self.ids.flashcard_content.text = self.baybayin[self.current_card_index]

        # Update the star icon based on the starred state of the current card
        if self.starred_states[self.current_card_index]:
            self.ids.star_button.icon = "star"
        else:
            self.ids.star_button.icon = "star-outline"

        print(f'Index: {self.current_card_index}')

    def toggle_star(self):
        # Toggle the starred state for the current card
        card_info = [self.level, self.current_card_index]
        self.starred_states[self.current_card_index] = not self.starred_states[self.current_card_index]

        # Update the star icon and database based on the new starred state
        if self.starred_states[self.current_card_index]:
            self.ids.star_button.icon = "star"
            if card_info not in self.saved_cards:
                self.saved_cards.append(card_info)
            print(f"Card starred: Index {self.current_card_index}, Level: {self.level}")

        else:
            self.ids.star_button.icon = "star-outline"
            if card_info in self.saved_cards:
                self.saved_cards.remove(card_info)
            print(f"Card unstarred: Index {self.current_card_index}, Level: {self.level}")

class SavedScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global path
        db = database_handler(namedb=path)
        self.content_indexes = db.search2(f"SELECT * from saved")
        self.flashcard_contents = []
        contents = []
        for i,j in self.content_indexes:
            content = db.search2(f"SELECT fro,bck from contents where lvl={i} and dex={j}")
            contents.append(content[0])
        print(contents)
        self.tagalog,self.baybayin = zip(*contents)
        self.tagalog, self.baybayin = list(self.tagalog),list(self.baybayin)
        self.flashcard_contents = self.tagalog
        self.current_card_index = 0
        self.is_tagalog = True
        self.dialog = None
    def backtohome(self):
        baybai.backtohome(self)

    def flip_card(self):
        self.is_tagalog = not self.is_tagalog  # Toggle between Tagalog and Baybayin
        if self.ids.saved_card_input.md_bg_color == get_color_from_hex("#9851FF"):
            self.ids.saved_card_input.md_bg_color = get_color_from_hex("#D346FF")
            self.ids.saved_card_content.text = self.baybayin[self.current_card_index]
        else:
            self.ids.saved_card_input.md_bg_color = get_color_from_hex("#9851FF")
            self.ids.saved_card_content.text = self.tagalog[self.current_card_index]
        # self.update_flashcard_content()

    def next_card(self):
        self.current_card_index += 1
        if self.current_card_index >= len(self.tagalog):  # Use length of tagalog list
            self.current_card_index = 0  # Reset to the first card if we've reached the end
        self.update_flashcard_content()

    def prev_card(self):
        self.current_card_index -= 1
        if self.current_card_index >= len(self.tagalog):  # Use length of tagalog list
            self.current_card_index = 0  # Reset to the first card if we've reached the end
        self.update_flashcard_content()
    def update_flashcard_content(self):
        if self.flashcard_contents:
            self.ids.saved_card_content.text = self.flashcard_contents[self.current_card_index]
        else:
            self.ids.saved_card_content.text = ""

    def remove_flashcard(self, *args):
        self.dialog.dismiss()
        global path
        print(f"Content Indexes: {self.content_indexes}\nFlashcard Contents: {self.flashcard_contents}\nself.tagalog: {self.tagalog},\nself.baybayin: {self.baybayin}")
        print(f"Current Index: {self.current_card_index}")
        del self.tagalog[self.current_card_index]
        del self.baybayin[self.current_card_index]
        db = database_handler(path)
        lvl,dex = self.content_indexes[self.current_card_index][0], self.content_indexes[self.current_card_index][1]
        db.run_query(f"DELETE FROM saved where lvl={lvl} and dex={dex}")
        db.close()
        self.update_flashcard_content()
    def toggle_star(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title='Remove Flashcard',
                text='Are you sure you want to remove this flashcard from Saved Cards?',
                buttons=[
                    MDFlatButton(
                        text='CANCEL',
                        on_release=self.close_dialog
                    ),
                    MDFlatButton(
                        text='REMOVE',
                        on_release=self.remove_flashcard
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()
class Flashcards(MDScreen):
    pass
class TranslateScreen(MDScreen):
    #ADD ERROR MESSAGE FOR WHEN WORD IS NOT TAGALOG.
    dialog=None
    def translate(self):
        # self.ids.translation.text=str(self.ids.tbd.text)
        self.ids.translation.text = str(translate(str(self.ids.tbd.text)))

    def dismiss_popup(self,dt):
        self.dialog.dismiss()
    def copy_translation(self):
        def popup():
            if self.ids.translation.text == '':
                self.dialog = MDDialog(text="Clipboard empty. Please enter a word to be translated")
            else:
                self.dialog = MDDialog(text="Baybayin script copied to clipboard!")
            self.dialog.open()
            Clock.schedule_once(self.dismiss_popup,1)
        pyperclip.copy(str(self.ids.translation.text))
        popup()

    def backtohome(self):
        baybai.backtohome(self)

class StatsScreen(MDScreen):
    dialog=None

class NetworkScreen(MDScreen):
    def __init__(self, **kwargs):
        super(NetworkScreen, self).__init__(**kwargs)

        # FONTS
        LabelBase.register(name='Helvetica', fn_regular='fonts/HelveticaNeue-01.ttf',
                           fn_bold='fonts/HelveticaNeue-Bold-02.ttf',
                           fn_bolditalic='fonts/HelveticaNeue-BoldItalic-04.ttf',
                           fn_italic='fonts/HelveticaNeue-Italic-03.ttf')

        # Main layout
        main_layout = BoxLayout(orientation='vertical',spacing=50)

        # Upper bar
        upper_bar = BoxLayout(orientation='horizontal', size_hint_y=0.10)

        back_arrow = MDIconButton(icon='images/arrow_back.png',pos_hint={'center_x': 0.2, 'center_y': 0.5})
        back_arrow.bind(on_release=self.backtohome)

        logo_image = Image(source='images/logo_b.png', size_hint=(None, None), size=(dp(220), dp(220)),
                           allow_stretch=True, pos_hint={"center_y": 0.5}, size_hint_y=0.7, opacity=0.7)
        title = MDLabel(text='BaiNet', font_name='Helvetica', bold=True, font_size=dp(90))

        upper_bar.add_widget(back_arrow)
        upper_bar.add_widget(logo_image)
        upper_bar.add_widget(title)




        #CONTENT
        content_layout = BoxLayout(orientation='vertical', size_hint=(0.9, 0.8),
                                   pos_hint={'center_x': 0.5, 'center_y': 0.5}, spacing=40, padding=[0, 30, 20, 0])
        create_post_button = MDFlatButton(text='Create post', md_bg_color=(1, 0.19, 0.76, 1),
                                          size_hint_x=1.0, size_hint_y=0.05,
                                          font_name='Helvetica')
        create_post_button.bind(on_release=self.create_post)



        super(NetworkScreen, self).__init__(**kwargs)
        # Register fonts here if needed, or better, do it in the build method of your app
        scroll_view = ScrollView(size_hint=(0.8, None), size=(Window.width, Window.height),
                                 pos_hint={"center_x": 0.5, "center_y": 0.5})
        scroll_view.add_widget(CardList())
        posts_scrolls = BoxLayout(size_hint=(1.0, 0.8),spacing=10,orientation='vertical',pos_hint={'center_x':0.5,'center_y':0.5})


        content_layout.add_widget(create_post_button)
        # content_layout.add_widget(scroll_view)
        posts_scrolls.add_widget(scroll_view)
        content_layout.add_widget(posts_scrolls)

        main_layout.add_widget(upper_bar)
        main_layout.add_widget(content_layout)

        self.add_widget(main_layout)


    def create_post(self,instance):
        self.manager.current = "CreatePostScreen"

    def backtohome(self,instance):
        self.manager.current = "HomeScreen"

from kivy.uix.image import Image
from kivy.metrics import dp

class CardList(BoxLayout):
    def __init__(self, **kwargs):
        super(CardList, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.bind(minimum_height=self.setter('height'))

        # Example posts data
        posts = {
            1: ['zelan811', 'My First Post', 'This is the content of the first post.', 'Sep 12, 2023'],
            2: ['zelan811', 'My SECOND Post', 'This is the content of the 2nd post.', 'Sep 12, 2023']
            # ... more posts
        }

        md_list = MDList()
        md_list.spacing = 0

        # Add cards to the layout
        for post_id, post_data in posts.items():
            username, title, content, timestamp = post_data

            container = BoxLayout(size_hint_y=None, height="150dp")
            card = MDCard(size_hint_y=None, size_hint_x=0.5, height=200)

            card.canvas.before.add(Color(rgba=(0, 0, 0, 1)))
            card.canvas.before.add(Line(width=5, rectangle=(card.x + 1, card.y + 1, card.width - 2, card.height - 2)))

            # Left box with upvote/downvote
            left_box = self.create_vote_box()
            card.add_widget(left_box)

            # Right box with post info
            right_box = self.create_post_box(username, timestamp, title, content)
            card.add_widget(right_box)

            container.add_widget(card)
            md_list.add_widget(container)

        self.add_widget(md_list)

    def create_vote_box(self):
        left_box = MDBoxLayout(size_hint=(0.15, 1), md_bg_color=(0.6, 0.31, 1, 1), orientation='vertical')
        upvote_button = MDIconButton(icon="images/arrow-up.png", pos_hint={'center_x': 0.5, 'center_y': 0.5})
        upvote_button.bind(on_release=self.upvote_post)
        downvote_button = MDIconButton(icon="images/arrow-down.png", pos_hint={'center_x': 0.5, 'center_y': 0.5})
        downvote_button.bind(on_release=self.downvote_post)
        left_box.add_widget(upvote_button)
        left_box.add_widget(downvote_button)
        return left_box

    def create_post_box(self, username, timestamp, title, content):
        right_box = MDBoxLayout(size_hint=(0.85, 1), orientation='vertical')
        user_box = MDBoxLayout(orientation='horizontal', padding=[40, 0, 0, 0])
        user_box.add_widget(MDLabel(text=username, font_name='Helvetica', font_size='25px'))
        user_box.add_widget(MDLabel(text=timestamp, font_name='Helvetica', font_size='18', theme_text_color='Custom', text_color=(0.28, 0.28, 0.28, 1)))
        right_box.add_widget(user_box)
        right_box.add_widget(MDLabel(text=f"{title}\n{content}", font_name='Helvetica', font_size='22sp', halign='center'))
        return right_box

# class CardList(BoxLayout):
#     def __init__(self, **kwargs):
#         super(CardList, self).__init__(**kwargs)
#         self.orientation = 'vertical'
#         self.size_hint_y = None
#         self.bind(minimum_height=self.setter('height'))
#
#         #key (post_id): [username, title, post_content,timestamp]
#         posts = {1:['zelan811','title','postxyz','timestamp']}
#
#
#         md_list = MDList()  # Create an MDList
#         md_list.spacing=0
#
#         # Add cards to the layout
#         for i in range(10):  # Example: Creating 10 cards
#             # container = BoxLayout(padding="10dp", size_hint_y=None, height="200dp")
#             container = BoxLayout(size_hint_y=None, height="150dp")
#             card = MDCard(size_hint_y=None, size_hint_x=0.5, height=200)
#
#             card.canvas.before.add(Color(rgba=(0, 0, 0, 1)))
#             card.canvas.before.add(Line(width=5, rectangle=(card.x + 1, card.y + 1, card.width - 2, card.height - 2)))
#             left_box = MDBoxLayout(size_hint=(0.15, 1), md_bg_color=(0.6, 0.31, 1, 1), orientation='vertical')
#
#             # Upvote button
#             upvote_button = MDIconButton(icon="images/arrow-up.png", pos_hint={'center_x': 0.5, 'center_y': 0.5})
#             upvote_button.bind(on_release=self.upvote_post)
#             left_box.add_widget(upvote_button)
#
#             # Downvote button
#             downvote_button = MDIconButton(icon="images/arrow-down.png", pos_hint={'center_x': 0.5, 'center_y': 0.5})
#             downvote_button.bind(on_release=self.downvote_post)
#             left_box.add_widget(downvote_button)
#
#             card.add_widget(left_box)
#
#             right_box = MDBoxLayout(size_hint=(0.85, 1), orientation='vertical')
#             user_box = MDBoxLayout(orientation='horizontal', padding=[40, 0, 0, 0])
#             user_box.add_widget(MDLabel(text='username', font_name='Helvetica', font_size='25px'))
#             user_box.add_widget(MDLabel(text='Sep 12 2023',font_name='Helvetica', font_size='18', theme_text_color='Custom', text_color=(0.28, 0.28, 0.28, 1)))
#             right_box.add_widget(user_box)
#             right_box.add_widget(MDLabel(text='Lorem ipsum dolor sit amet, consectetur adipiscing elit...', font_name='Helvetica', font_size='22sp', halign='center'))
#
#             card.add_widget(right_box)
#
#             container.add_widget(card)
#             md_list.add_widget(container)
#
#         self.add_widget(md_list)

    def downvote_post(self,instance):
        print("Downvote triggered")
        pass

    def upvote_post(self,instance):
        print("Upvote triggered")
        pass

    def net2home(self):
        self.manager.current = "HomeScreen"

    def net2stats(self):
        self.manager.current = "StatsScreen"



class CreatePostScreen(MDScreen):
    pass

class stats(MDScreen):
    dialog=None

class baybai(MDApp):
    def backtohome(self):
        self.parent.current='HomeScreen'
    def build(self):
        LabelBase.register(name='Helvetica',fn_regular='fonts/HelveticaNeue-01.ttf',fn_bold='fonts/HelveticaNeue-Bold-02.ttf',fn_bolditalic='fonts/HelveticaNeue-BoldItalic-04.ttf',fn_italic='fonts/HelveticaNeue-Italic-03.ttf')
        LabelBase.register(name='Baybayin', fn_regular='fonts/Baybayin.ttf')
        LabelBase.register(name='Noto', fn_regular='fonts/NotoSansTagalog.ttf')
        screen_manager = ScreenManager()
        home_screen = HomeScreen(name='HomeScreen')  # Create an instance of your HomeScreen
        learn_screen = LearnScreen(name='LearnScreen')
        scroll_view = ScrollView(size_hint=(0.8, None), size=(Window.width, Window.height),
                                 pos_hint={"center_x": 0.5, "center_y": 0.5})
        scroll_view.add_widget(CardList())
        network_screen = LearnScreen(name='NetworkScreen')
        network_screen.add_widget(scroll_view)
        screen_manager.add_widget(home_screen)  # Add the HomeScreen to the ScreenManager
        screen_manager.add_widget(learn_screen)



        return Builder.load_file('baybai.kv')

test = baybai()
test.run()