# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the game over scene.


from scene import *
import ui
from game_scene import *

class GameOverScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.dismiss_modal_scene(GameScene())
        self.present_modal_scene(GameScene())
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = '#313aaa', 
                                     parent = self, 
                                     size = self.size)
        
    
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
        pass
    
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
    
