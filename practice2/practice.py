# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.scrollview import ScrollView
# from kivymd.uix.card import MDCard
# from kivymd.uix.label import MDLabel
# from kivy.core.window import Window
# from kivy.graphics import Color, Line  # Import Color and Line
# from kivy.core.text import LabelBase
# from kivy.uix.screenmanager import ScreenManager
# from kivymd.app import MDApp
# from kivymd.uix.boxlayout import MDBoxLayout
# from kivymd.uix.button import MDIconButton
# from kivymd.uix.list import MDList
#
# class CardList(BoxLayout):
#     def __init__(self, **kwargs):
#         super(CardList, self).__init__(**kwargs)
#         self.orientation = 'vertical'
#         self.size_hint_y = None
#         self.bind(minimum_height=self.setter('height'))
#         md_list = MDList()
#
#         # Add cards to the layout
#         for i in range(10):  # Example: Creating 10 cards
#             container = BoxLayout(padding="10dp", size_hint_y=None, height="200dp")
#
            # card = MDCard(size_hint_y=None,size_hint_x=0.5, height=200)  # Set the size of each card
            #
            # card.canvas.before.add(Color(rgba=(0, 0, 0, 1)))
            # card.canvas.before.add(Line(width=5, rectangle=(card.x + 1, card.y + 1, card.width - 2, card.height - 2)))
            # left_box = MDBoxLayout(size_hint=(0.15, 1), md_bg_color=(0.6, 0.31, 1, 1), orientation='vertical')
            # left_box.add_widget(MDIconButton(icon="images/arrow-up.png", pos_hint={'center_x': 0.5, 'center_y': 0.5}))
            # left_box.add_widget(MDIconButton(icon="images/arrow-down.png", pos_hint={'center_x': 0.5, 'center_y': 0.5}))
            # card.add_widget(left_box)
            #
            # right_box = MDBoxLayout(size_hint=(0.85, 1), orientation='vertical')
            # user_box = MDBoxLayout(orientation='horizontal', padding=[40, 0, 0, 0])
            # user_box.add_widget(MDLabel(text='username', font_name='Helvetica', font_size='25px'))
            # user_box.add_widget(MDLabel(text='Sep 12 2023',font_name='Helvetica', font_size='18', theme_text_color='Custom', text_color=(0.28, 0.28, 0.28, 1)))
            # right_box.add_widget(user_box)
            # right_box.add_widget(MDLabel(text='Lorem ipsum dolor sit amet, consectetur adipiscing elit...', font_name='Helvetica', font_size='22sp', halign='center'))
            #
            # card.add_widget(right_box)
#
#             container.add_widget(card)
#             md_list.add_widget(container)
#         return md_list
#             # self.add_widget(card)
#
# class MyApp(MDApp):
#     def build(self):
#         #FONTS
#         LabelBase.register(name='Helvetica', fn_regular='fonts/HelveticaNeue-01.ttf',
#                                fn_bold='fonts/HelveticaNeue-Bold-02.ttf', fn_bolditalic='fonts/HelveticaNeue-BoldItalic-04.ttf',
#                                fn_italic='fonts/HelveticaNeue-Italic-03.ttf')
#         # Create a scroll view
#         scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
#         scroll_view.add_widget(CardList())
#         return scroll_view
#
# if __name__ == '__main__':
#     MyApp().run()


from kivy.app import App
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

class MyApp(MDApp):
    def build(self):
        #FONTS
        LabelBase.register(name='Helvetica', fn_regular='fonts/HelveticaNeue-01.ttf',
                               fn_bold='fonts/HelveticaNeue-Bold-02.ttf', fn_bolditalic='fonts/HelveticaNeue-BoldItalic-04.ttf',
                               fn_italic='fonts/HelveticaNeue-Italic-03.ttf')
        # Create a scroll view
        scroll_view = ScrollView(size_hint=(0.8, None), size=(Window.width, Window.height),pos_hint={"center_x":0.5,"center_y":0.5})
        scroll_view.add_widget(CardList())
        return scroll_view

class CardList(BoxLayout):
    def __init__(self, **kwargs):
        super(CardList, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.bind(minimum_height=self.setter('height'))

        # Title Bar
        title_bar = MDLabel(
            text="Title Bar",
            size_hint_y=None,
            height=dp(40),
            halign='center'
        )
        self.add_widget(title_bar)

        #SCROLL VIEW FOR CARDS
        md_list = MDList()  # Create an MDList
        # Add cards to the layout
        for i in range(10):  # Example: Creating 10 cards
            container = BoxLayout(padding="10dp", size_hint_y=None, height="200dp")
            card = MDCard(size_hint_y=None, size_hint_x=0.5, height=200)

            card.canvas.before.add(Color(rgba=(0, 0, 0, 1)))
            card.canvas.before.add(Line(width=5, rectangle=(card.x + 1, card.y + 1, card.width - 2, card.height - 2)))
            left_box = MDBoxLayout(size_hint=(0.15, 1), md_bg_color=(0.6, 0.31, 1, 1), orientation='vertical')
            left_box.add_widget(MDIconButton(icon="images/arrow-up.png", pos_hint={'center_x': 0.5, 'center_y': 0.5}))
            left_box.add_widget(MDIconButton(icon="images/arrow-down.png", pos_hint={'center_x': 0.5, 'center_y': 0.5}))
            card.add_widget(left_box)

            right_box = MDBoxLayout(size_hint=(0.85, 1), orientation='vertical')
            user_box = MDBoxLayout(orientation='horizontal', padding=[40, 0, 0, 0])
            user_box.add_widget(MDLabel(text='username', font_name='Helvetica', font_size='25px'))
            user_box.add_widget(MDLabel(text='Sep 12 2023',font_name='Helvetica', font_size='18', theme_text_color='Custom', text_color=(0.28, 0.28, 0.28, 1)))
            right_box.add_widget(user_box)
            right_box.add_widget(MDLabel(text='Lorem ipsum dolor sit amet, consectetur adipiscing elit...', font_name='Helvetica', font_size='22sp', halign='center'))

            card.add_widget(right_box)

            container.add_widget(card)
            md_list.add_widget(container)

        self.add_widget(md_list)  # Add the MDList to the BoxLayout



if __name__ == '__main__':
    MyApp().run()