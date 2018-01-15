# Created by: Alireza Teimoori
# Created on: Jan 2018
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui
import config
from game_scene import *
from game_over_scene import *
from tutorial_secne import *
from setting_scene import *

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)
                                     
        
        self.start_button_position = Vector2()
        self.start_button_position.x = self.screen_center_x
        self.start_button_position.y = self.screen_center_y + 150
        self.start_button = SpriteNode('./assets/sprites/start_button.png',
                                       parent = self,
                                       position = self.start_button_position,
                                       scale = 0.5)
                                       
        
        
        self.setting_button_position = Vector2()
        self.setting_button_position.x = self.screen_center_x
        self.setting_button_position.y = self.screen_center_y 
        self.setting_button = SpriteNode('./assets/sprites/setting_button.png',
                                       parent = self,
                                       position = self.setting_button_position,
                                       scale = 0.5)
        
        
        self.tutorial_button_position = Vector2()
        self.tutorial_button_position.x = self.screen_center_x
        self.tutorial_button_position.y = self.screen_center_y - 150
        self.tutorial_button = SpriteNode('./assets/sprites/tutorial_button.png',
                                       parent = self,
                                       position = self.tutorial_button_position,
                                       scale = 0.5)
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        if config.game_over == True:
            self.present_modal_scene(GameOverScene())
            config.game_over = False
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto game scene
        if self.start_button.frame.contains_point(touch.location):
            self.present_modal_scene(GameScene())
            config.score = 0
            
        # if start button is pressed, goto game scene
        if self.setting_button.frame.contains_point(touch.location):
            self.present_modal_scene(SettingScene())
        
        # if start button is pressed, goto game scene
        if self.tutorial_button.frame.contains_point(touch.location):
            self.present_modal_scene(TutorialScene())
    
    
