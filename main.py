import os
import sys
import time
import random
import rich
from rich import print

import version
from game import Game

from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Label, Button, TextArea, Footer

class MyCity(App):
    BINDINGS = [
        ('q', 'exit', 'Quit')
    ]

    MENUS = [
        'Main',
        'Credits',
        'Game'
    ]

    def __init__(self):
        super().__init__()
        self.try_exit = False
        self.notify('Welcome!')
        

    def compose(self) -> ComposeResult:
        if self.try_exit:
            text = Label('Are you sure you want to exit?')
            text._on_click
            yield Label('Are you sure you want to exit?')
            yield HorizontalGroup(Button('Yes', id='exit_yes', variant='success'), Button('No', id='exit_no', variant='error'))
        yield Button(id='test', label='Test', tooltip='this is a test')
        yield Footer(show_command_palette=False)

    def action_exit(self):
        # Shutdown the server or the client and exit
        self.try_exit = True
        self.notify('Try exit is: ' + str(self.try_exit))
        self.refresh(recompose=True, layout=True)

    def shutdown(self, exit_code : int):
        # Shutdown server or client
        exit(exit_code)

if __name__ == '__main__':
    mycity = MyCity()
    mycity.run()
