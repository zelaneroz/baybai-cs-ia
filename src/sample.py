from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.relativelayout import RelativeLayout
from kivy.animation import Animation
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.core.text import LabelBase


class FlipCard(RelativeLayout):
    def __init__(self, front_text='Front', back_text='Back', **kwargs):
        super().__init__(**kwargs)
        self.front_card = MDCard(
            # border_radius=20,
            radius=[14],
            md_bg_color='#9851FF',
            size_hint=(0.7, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        self.front_card.add_widget(
            MDLabel(
                text=front_text,
                halign='center',
                font_name='Noto',
                color=(1, 1, 1, 1),
                font_size='250px',
                bold=True
            )
        )
        self.add_widget(self.front_card)

        self.back_card = MDCard(
            # border_radius=20,
            radius=[14],
            md_bg_color='#9851FF',
            size_hint=(0.7, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        self.back_card.add_widget(
            MDLabel(
                text=back_text,
                halign='center',
                font_name='Noto',
                color=(1, 1, 1, 1),
                font_size='250px',
                bold=True
            )
        )
        self.add_widget(self.back_card)

        self.is_flipped = False

    def flip_card(self):
        if self.is_flipped:
            anim = Animation(rotation_y=0, d=0.5)
            anim.start(self.front_card)
            self.back_card.rotation_y = 180
            self.is_flipped = False
        else:
            anim = Animation(rotation_y=180, d=0.5)
            anim.start(self.front_card)
            self.back_card.rotation_y = 0
            self.is_flipped = True

class MyApp(MDApp):
    def build(self):
        LabelBase.register(name='Noto', fn_regular='fonts/NotoSansTagalog.ttf')
        return Builder.load_file('sample.kv')


if __name__ == '__main__':
    MyApp().run()
