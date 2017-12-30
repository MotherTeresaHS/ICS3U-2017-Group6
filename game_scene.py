# This is the scene that user gets to play in it

# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the game_scene.

from scene import *
import ui
from numpy import random

class GameScene(Scene):
    
    def setup(self):
        # this method is called, when user moves to this scene
        
        
        
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        self.spacecube_attack_rate = 1
        self.spacecubes = []
        self.spacecube_attack_speed = 20
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
        
        return self.size_of_screen_x, self.size_of_screen_y, self.screen_center_x, self.screen_center_y
        
        
    
    def create_new_spacecube(self):
        # add a new spacecube to come down
        
        spacecube_start_position = Vector2()
        spacecube_start_position.x = random.randint(100, 
                                         self.size_of_screen_x - 100)
        spacecube_start_position.y = self.size_of_screen_y + 100
        
        spacecube_end_position = Vector2()
        spacecube_end_position.x = random.randint(100, 
                                        self.size_of_screen_x - 100)
        spacecube_end_position.y = -100
        
        space_cube_number = random.randint(1,4)
        
        if space_cube_number == 1:
        
            self.spacecubes.append(SpriteNode('./assets/sprites/green_spacecube.png',
                                 position = spacecube_start_position,
                                 parent = self,
                                 scale = 0.25))
                                 
                                 
            spacecube_lives = 1
        
        elif space_cube_number == 2:
            self.spacecubes.append(SpriteNode('./assets/sprites/blue_spacecube.png',
                                 position = spacecube_start_position,
                                 parent = self,
                                 scale = 0.03))
                                 
                                 
                                 
            spacecube_lives = 2
            
        elif space_cube_number == 3:
            self.spacecubes.append(SpriteNode('./assets/sprites/red_spacecube.png',
                                 position = spacecube_start_position,
                                 parent = self,
                                 scale = 0.35))
                                 
                                 
            spacecube_lives = 3
        
        # make missile move forward
        spacecubeMoveAction = Action.move_to(spacecube_end_position.x, 
                                         spacecube_end_position.y, 
                                         self.spacecube_attack_speed,
                                         TIMING_SINODIAL)
        self.spacecubes[len(self.spacecubes)-1].run_action(spacecubeMoveAction)
        
        return spacecube_lives
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        #####
        
        #####
        # check if new spacecube should be added
        #####
        
        space_cube_number = random.randint(1,3)
        spacecube_create_chance = random.randint(1, 220)
        
        if spacecube_create_chance <= self.spacecube_attack_rate:
            #space_cubes.SpaceCubes.create_new_spacecube(space_cubes.SpaceCubes(), space_cube_number)
            self.create_new_spacecube()
        
        for space_cube in self.spacecubes:
            if space_cube.position.y < -50:
                space_cube.remove_from_parent()
                self.spacecubes.remove(space_cube)
                # you might want to end the game, or take points away
        
        ################################################################
        
        
        #####
        # check every update if an alien is off screen
        #####
        
        for space_cube in self.spacecubes:
            if space_cube.position.y < -50:
                space_cube.remove_from_parent()
                self.spacecubes.remove(space_cube)
                # you might want to end the game, or take points away
                
            
        ################################################################
        
        
        #####
        # check every update to see if a missile has touched a space alien
        #####
        
        if len(self.spacecubes) > 0 and len(self.lasers) > 0:
            #print('missile check')
            for space_cube in self.spacecubes:
                for laser in self.lasers:
                    if space_cube.frame.contains_rect(laser.frame):
                        laser.remove_from_parent()
                        self.lasers.remove(laser)
                        
                        #space_cube.remove_from_parent()
                        #self.spacecubes.remove(space_cube)
                        # since you destroyed one, make more show up
                        #self.alien_attack_rate = self.alien_attack_rate + 1
        else:
            pass
            #print(len(self.aliens))
        
        ################################################################
        
        #####
        # check if the spacecube should vanish 
        #####
        
        for space_cube in self.spacecubes:
            if spacecube_lives <= 0:
                space_cube.remove_from_parent()
                self.spacecubes.remove(space_cube)
                
            
        
        #################################################################
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        if touch.location in self.space_ship.frame :
            self.space_ship.position = touch.location
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.fire_button.frame.contains_point(touch.location):
            self.create_new_laser()
            
        
    
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
        laser_start_position = Vector2()
        laser_start_position.x = self.space_ship.position.x
        laser_start_position.y = self.space_ship.position.y
        
        laser_end_position = Vector2()
        laser_end_position.x = laser_start_position.x
        laser_end_position.y = self.size_of_screen_y + 100
        
        self.lasers.append(SpriteNode('./assets/sprites/laser.png',
                             position = laser_start_position,
                             parent = self))
        
        # make missile move forward
        laserMoveAction = Action.move_to(laser_end_position.x, 
                                           laser_end_position.y + 100, 
                                           5.0)
        self.lasers[len(self.lasers)-1].run_action(laserMoveAction)
    
    
