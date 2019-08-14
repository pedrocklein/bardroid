#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:10:28 2019

@author: pklein
"""

import os

from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from functools import partial

class SoundBoard(App):
    def build(self):
        #pasta aonde o programa vai procurar as musicas/sons para adiconionar na board
        #no caso procura na pasta /music dentro da pasta atual.

        '''gambi, avaliar aonde esta o arquivo ao inves de procurar o [3] dos files'''
        #self.musicFolder = os.listdir(os.path.dirname(os.path.abspath(__file__)))[3]+"/music"
        self.musicFolder = "./music"
        
        self.files = os.listdir(os.path.dirname(os.path.abspath(self.musicFolder)))
        #cria o layout para o programa
        self.masterlayout = BoxLayout(orientation="vertical")
        self.layout = GridLayout(cols=3)
        self.masterlayout.add_widget(self.layout)
        self.playing = []
        Window.borderless = False
        Window.size = (500,500)
        contador = 0
        for som in self.files:
            print(contador)
            #para cada som na pasta das musicas cria um botao novo
            name, ext = os.path.splitext(som)
            btn = Button(text=name)
            #adiciona a funcao de tocar a musica ao apertar o botao
            btn.bind(on_press=partial(self.playSound, self.files[contador]))
            self.layout.add_widget(btn)
            contador+=1
        #botao para parar o player
        btnStahp = Button(text="Staaahp", size_hint_x=1, size_hint_y = 0.3)
        btnStahp.bind(on_press=self.stopSound)
        self.masterlayout.add_widget(btnStahp)

        #completa a acao adicionando o layout a aplicacao
        return self.masterlayout

    
    def playSound(self,som,instance):
        #funcao que toca a musica/som
        song = SoundLoader.load("music/"+som)
        song.play()
        self.playing.append(song)

    
    def stopSound(self,instance):
        #para todos os sons sendo tocados
        for f in self.playing:
            f.stop()


SoundBoard().run()