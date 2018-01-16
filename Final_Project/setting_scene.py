


# Created by: Alireza Teimoori
# Created on: Jan 2018
# Created for: ICS3U
# this scene is the setting scene

from scene import *
import ui
import config

class SettingScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = '#3faa48', 
                                     parent = self, 
                                     size = self.size)
        
        self.back_button_position = self.size
        self.back_button_position.x = 100
        self.back_button_position.y = self.back_button_position.y - 100
        self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                       parent = self,
                                       position = self.back_button_position)
        
        self.instruction_label_position = Vector2()
        self.instruction_label_position.x = self.screen_center_x
        self.instruction_label_position.y = self.screen_center_y + 150
        self.Instruction_label = LabelNode('FX sounds are ON right now',
                                            parent = self,
                                            position = self.instruction_label_position,
                                            color = 'black')
        
        self.sound_on_button_position = Vector2()
        self.sound_on_button_position.x = self.screen_center_x + 180
        self.sound_on_button_position.y = self.screen_center_y
        self.sound_on_button = SpriteNode('./assets/sprites/sound_on.png',
                                          position = self.sound_on_button_position,
                                          parent = self,
                                          scale = 0.7)
        
        self.sound_off_button_position = Vector2()
        self.sound_off_button_position.x = self.screen_center_x - 120
        self.sound_off_button_position.y = self.screen_center_y
        self.sound_off_button = SpriteNode('./assets/sprites/sound_off.png',
                                          position = self.sound_off_button_position,
                                          parent = self,
                                          scale = 0.2)
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        if config.fx_sound_on == True:
            if self.Instruction_label.text != 'FX sounds are ON right now' and self.Instruction_label.color != 'black':
                self.Instruction_label.text = 'FX sounds are ON right now'
            self.Instruction_label.color = 'black'
            
        elif config.fx_sound_on == False:
            if self.Instruction_label.text != 'FX sounds are OFF right now' and self.Instruction_label.color != 'red':
                self.Instruction_label.text = 'FX sounds are OFF right now'
            self.Instruction_label.color = 'red'
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if back button is pressed, go to main menu
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
            
        
        if self.sound_on_button.frame.contains_point(touch.location):
            config.fx_sound_on = True
            self.Instruction_label.text = 'FX sounds are ON right now'
            self.Instruction_label.color = 'black'
        
        if self.sound_off_button.frame.contains_point(touch.location):
            config.fx_sound_on = False
            self.Instruction_label.text = 'FX sounds are OFF right now'
            self.Instruction_label.color = 'red'
        
        
    
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
    
