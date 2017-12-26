# This is the scene that user gets to play in it

# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the game_scene.

from scene import *
import ui


class GameScene(Scene):
    
    def setup(self):
        # this method is called, when user moves to this scene
        
        
        
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        
        self.lasers = []
        
        # add background
        
        self.background = SpriteNode('./assets/sprites/blue_star_background.png',
                                       parent = self,
                                       position = self.size/2,
                                       size = self.size)
        
        space_ship_position=self.size/2
        space_ship_position.y=100
        self.space_ship=SpriteNode('./assets/sprites/user_spaceship.png',
                                   position=space_ship_position,
                                   parent=self,
                                   scale = 1.25)
                                   
                                   
        
        
        
        fire_button_position = Vector2()
        fire_button_position.x = self.size_of_screen_x - 100
        fire_button_position.y = 100
        self.fire_button = SpriteNode('./assets/sprites/fire_button.png',
                                      parent = self,
                                      position = fire_button_position,
                                      alpha = 0.5,
                                      scale = 0.25)
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        if touch.location in self.space_ship.frame :
            self.space_ship.position = touch.location
    
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
    
    def create_new_laser(self):
        # when the user hits the fire button
        pass
    
    def create_new_spacecube(self):
        # add a new spacecube to come down
        
        pass
    
    def create_new_rarecube(self):
        # add a new rare spacecube that goes across the screen
        
        pass
    
