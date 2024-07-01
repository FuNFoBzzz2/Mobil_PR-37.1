from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Ellipse, Line
class MyPaintWidget(Widget):
    def __init__(self, **kwargs):
        super(MyPaintWidget, self).__init__(**kwargs)
        self.line_color = (1, 1, 1)  # default line color
        self.line_thickness = 2  # default line thickness

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.line_color, mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.line_thickness)
    def on_touch_move(self, touch):
        if 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]
class MyPaintApp(App):
    def build(self):
        parent = BoxLayout(orientation='horizontal')
        self.painter = MyPaintWidget()
        control_panel = BoxLayout(orientation='vertical')
        clearbtn = Button(text='Clear', size_hint_y=None, height=40)
        clearbtn.bind(on_release=self.clear_canvas)
        color_slider = Slider(min=0, max=1, value=1, orientation='vertical', size_hint_y=None, height=100)
        color_slider.bind(value=self.change_line_color)
        thickness_slider = Slider(min=1, max=10, value=2, orientation='vertical', size_hint_y=None, height=100)
        thickness_slider.bind(value=self.change_line_thickness)
        control_panel.add_widget(clearbtn)
        control_panel.add_widget(color_slider)
        control_panel.add_widget(thickness_slider)
        parent.add_widget(self.painter)
        parent.add_widget(control_panel)
        return parent
    def clear_canvas(self, obj):
        self.painter.canvas.clear()
    def change_line_color(self, slider, value):
        hue = value  # slider value ranges from 0 to 1, so we can use it as the hue value
        self.painter.line_color = (hue, 1, 1)  # set the line color to an HSV color
    def change_line_thickness(self, slider, value):
        self.painter.line_thickness = value  # change line thickness
if __name__ == '__main__':
    MyPaintApp().run()