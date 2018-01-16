# This is the scene that user gets to play in it

# Created by: Alireza Teimoori
# Created on: Jan 2018
# Created for: ICS3U

# This scene shows the game_scene.

from scene import *
import ui
from numpy import random
from game_over_scene import *
import config
import sound

class GameScene(Scene):
    
    def setup(self):
        # this method is called, when user moves to this scene
        
        
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        
        
        self.spacecubes = []
        self.spacecube_attack_rate = 1.0
        self.spacecube_attack_speed = 24
        
        
        self.rarecubes = []
        self.rarecube_attack_rate = 1.0
        self.rarecube_attack_speed = 12
        
        
        self.lasers = []
        
        
        self.user_lives = 3
        
        
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
        
        
        
        self.score_position = Vector2()
        self.score_position.x = 80
        self.score_position.y = self.size_of_screen_y - 50
        
        self.score_label = LabelNode(text = 'Score: ',
                                     parent = self,
                                     position = self.score_position)
                                     
        
        
        self.highscore_position = Vector2()
        self.highscore_position.x = 80
        self.highscore_position.y = self.size_of_screen_y -150
        
        self.highscore_label = LabelNode(text = 'Highscore: ' + str(config.highscore),
                                         parent = self,
                                         position = self.highscore_position)
        
        
        self.lives_position = Vector2()
        self.lives_position.x = 80
        self.lives_position.y = self.size_of_screen_y - 100
        
        self.lives_label = LabelNode(text = 'Lives: x  x  x',
                                   parent = self,
                                   position = self.lives_position)
                                   
        
        
    
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
        
            self.spacecubes.append(SpriteNode(texture = './assets/sprites/green_spacecube.png',
                                 position = spacecube_start_position,
                                 parent = self,
                                 scale = 0.25))
                                 
                                 
            spacecube_lives = 1
        
        elif space_cube_number == 2:
            self.spacecubes.append(SpriteNode(texture = './assets/sprites/blue_spacecube.png',
                                 position = spacecube_start_position,
                                 parent = self,
                                 scale = 0.03))
                                 
                                 
                                 
            spacecube_lives = 2
            
        elif space_cube_number == 3:
            self.spacecubes.append(SpriteNode(texture = './assets/sprites/red_spacecube.png',
                                 position = spacecube_start_position,
                                 parent = self,
                                 scale = 0.35))
                                 
                                 
            spacecube_lives = 3
        
        # make spacecube move forward
        spacecubeMoveAction = Action.move_to(spacecube_end_position.x, 
                                         spacecube_end_position.y, 
                                         self.spacecube_attack_speed,
                                         TIMING_SINODIAL)
        self.spacecubes[len(self.spacecubes)-1].run_action(spacecubeMoveAction)
        
    def create_new_rarecube(self):
        # add a new rare cube to go across the scene
        
        rarecube_start_position = Vector2()
        rarecube_start_position.x = - 100
        rarecube_start_position.y = random.randint(self.size_of_screen_y -(self.size_of_screen_y/2), self.size_of_screen_y + 50)
        
        
        
        rarecube_end_position = Vector2()
        rarecube_end_position.x = self.size_of_screen_x + 60
        rarecube_end_position.y = random.randint(self.size_of_screen_y -(self.size_of_screen_y/2), self.size_of_screen_y + 50)
        
        
        self.rarecubes.append(SpriteNode('./assets/sprites/rare_cube.png',
                                 position = rarecube_start_position,
                                 parent = self,
                                 scale = 0.6))
                                 
                                 
        
        # make rarecube move forward
        rarecubeMoveAction = Action.move_to(rarecube_end_position.x, 
                                         rarecube_end_position.y, 
                                         self.rarecube_attack_speed,
                                         TIMING_SINODIAL)
        self.rarecubes[len(self.rarecubes)-1].run_action(rarecubeMoveAction)
    
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        #####
        
        #####
        # check if new spacecube should be added or is off the screen
        #####
        
        space_cube_number = random.randint(1,3)
        spacecube_create_chance = random.randint(1, 200)
        
        if spacecube_create_chance <= self.spacecube_attack_rate and config.game_over == False :
            #space_cubes.SpaceCubes.create_new_spacecube(space_cubes.SpaceCubes(), space_cube_number)
            self.create_new_spacecube()
        
        for space_cube in self.spacecubes:
            if space_cube.position.y < -50:
                space_cube.remove_from_parent()
                self.spacecubes.remove(space_cube)
                
                config.score = config.score - 2000
                if config.score < 0:
                    config.score = 0
                # you might want to end the game, or take points away
        
        ################################################################
        
        
        #####
        # check if new rarecube should be added or is off the screen
        #####
        
        rarecube_create_chance = random.randint(1, 1400)
        
        if rarecube_create_chance <= self.rarecube_attack_rate and config.game_over == False:
            #space_cubes.SpaceCubes.create_new_spacecube(space_cubes.SpaceCubes(), space_cube_number)
            self.create_new_rarecube()
        
        for rare_cube in self.rarecubes:
            if rare_cube.position.x > self.size_of_screen_x + 50:
                rare_cube.remove_from_parent()
                self.rarecubes.remove(rare_cube)
                #print("done")
        
        ################################################################
        
        
        #####
        # check every update to see if a missile has gone off the screen
        #####
        
        for laser in self.lasers:
            if laser.position.y > self.size_of_screen_y + 50:
                laser.remove_from_parent()
                self.lasers.remove(laser)
                #print("laser")
        
        ################################################################
        
        
        #####
        # check every update to see if a missile has touched a spacecube
        #####
        
        if len(self.spacecubes) > 0 and len(self.lasers) > 0:
            #print('missile check')
            for space_cube in self.spacecubes:
                for laser in self.lasers:
                    if space_cube.frame.contains_rect(laser.frame):
                        
                        if space_cube.scale == 0.25:
                            # green
                            config.score = config.score + 250
                            #print(config.score )
                        elif space_cube.scale == 0.03:
                            # blue
                            config.score = config.score  + 325
                            #print(config.score )
                        elif space_cube.scale == 0.35:
                            # red
                            config.score = config.score + 475
                            #print(config.score)
                        
                        
                        laser.remove_from_parent()
                        self.lasers.remove(laser)
                        
                        space_cube.remove_from_parent()
                        self.spacecubes.remove(space_cube)
                        # since you destroyed one, make more show up
                        self.spacecube_attack_rate = self.spacecube_attack_rate + 0.1
                        
         
         ################################################################
         
        #####
        # check every update to see if a missile has touched a rarecube
        #####
        
        if len(self.rarecubes) > 0 and len(self.lasers) > 0:
            #print('missile check')
            for rare_cube in self.rarecubes:
                for laser in self.lasers:
                    if rare_cube.frame.contains_rect(laser.frame):
                        laser.remove_from_parent()
                        self.lasers.remove(laser)
                        
                        rare_cube.remove_from_parent()
                        self.rarecubes.remove(rare_cube)
                        # since you destroyed one, make more show up
                        self.rarecube_attack_rate = self.rarecube_attack_rate + 0.1
                        config.score = config.score + 3000
                        
        
        ################################################################
        
        
        #####
        # check every update to see alien touches spaceship
        #####
        
        if len(self.spacecubes) > 0:
            #print('checking')
            for spacecube_hit in self.spacecubes:
                #print('alien ->' + str(alien_hit.frame))
                #print('ship  ->' + str(self.spaceship.frame))
                if spacecube_hit.frame.intersects(self.space_ship.frame):
                    #print('a hit')
                    #self.space_ship.remove_from_parent()
                    
                    #self.dismiss_modal_scene()
                    
                    if config.fx_sound_on == True:
                        
                        sound.play_effect('./assets/sounds/BarrelExploding.wav')
                        
                    
                    spacecube_hit.remove_from_parent()
                    self.spacecubes.remove(spacecube_hit)
                    self.user_lives = self.user_lives - 1
                    #print(self.user_lives)
                    
                    # since game over, move to next scene
                    
                
            
        
        ################################################################
        
        
        #####
        # Show user lives
        #####
        
        
        if self.user_lives == 3:
            if self.lives_label.text != "Lives: o  o  o":
                self.lives_label.text = 'Lives: o  o  o'
        elif self.user_lives == 2:
            if self.lives_label.text != "Lives: o o ":
                    self.lives_label.text = "Lives: o o "
        elif self.user_lives == 1:
                if self.lives_label.text != "Lives: o " :
                    self.lives_label.text = "Lives: o "
        
        ################################################################
        
        #####
        # Show user score and highscore
        #####
        
        if self.score_label.text != 'Score: ' + str(config.score):
            self.score_label.text = 'Score: ' + str(config.score)
        
        ###
        
        if config.score > config.highscore:
            config.highscore = config.score
            if self.highscore_label.text != 'Highscore: ' + str(config.highscore):
                self.highscore_label.text = 'Highscore: ' + str(config.highscore)
                
            
        
        ################################################################
        
        #####
        # Check if game is over or not
        #####
        
        if self.user_lives <= 0 :
            if config.game_over != True:
                config.game_over = True
                #print("game over")
                self.dismiss_modal_scene()
                
        
        ################################################################
        
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
        
        if config.fx_sound_on == True:
            
            sound.play_effect('./assets/sounds/laser1.wav')
            
        
        # make missile move forward
        laserMoveAction = Action.move_to(laser_end_position.x, 
                                           laser_end_position.y + 100, 
                                           5.0)
        self.lasers[len(self.lasers)-1].run_action(laserMoveAction)
    
    
