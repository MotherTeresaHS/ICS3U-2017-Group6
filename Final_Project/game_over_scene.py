# Created by: Alireza Teimoori
# Created on: Jan 2018
# Created for: ICS3U

# This scene shows the game over scene and also user's score and highscore


from scene import *
from main_menu_scene import *
from game_scene import *
import ui
import config



class GameOverScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = '#313aaa', 
                                     parent = self, 
                                     size = self.size)
        
        
        self.last_score = LabelNode(text = "Your final score is: " + str(config.score),
                                    parent = self,
                                    position = self.size/2)
        
        self.high_score_position = Vector2()
        self.high_score_position.y = self.screen_center_y - 100
        self.high_score_position.x = self.screen_center_x
        
        self.high_score = LabelNode(text = "High Score: " + str(config.highscore),
                                    parent = self,
                                    position =self.high_score_position)
        
        self.gameover_label_position = Vector2()
        self.gameover_label_position.y = self.screen_center_y + 150
        self.gameover_label_position.x = self.screen_center_x
        
        self.gameover_label = LabelNode(text = "Game Over",
                                        parent = self,
                                        color = "red",
                                        position = self.gameover_label_position)
        
        back_button_position = self.size
        back_button_position.x = 100
        back_button_position.y = back_button_position.y - 100
        
        
        self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                       parent = self,
                                       position = back_button_position)
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # go to previouse scene when this butten is touched (and released)
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
