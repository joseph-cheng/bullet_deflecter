from vec2 import Vec2
import pygame
import math

class Player:
    def __init__(self, x, y):

        self.pos = Vec2(x, y)
        self.vel = Vec2(0, 0)

        self.move_speed = 1


        # Angle the deflector is facing
        self.deflector_angle = 0

        # Width of deflector
        self.deflector_width = 25
        
        #Distance the delfector is from the centre of player
        self.deflector_distance_from_player = 25

        # collisions are done using circles, so we store the radius of the player
        self.radius = 10


    # Update the player
    def update(self, input_state):
        #Get the current velocity based on input
        self.vel = Vec2(input_state.move_right * self.move_speed - input_state.move_left * self.move_speed,
                        input_state.move_down * self.move_speed - input_state.move_up * self.move_speed)
        #Change the position
        self.pos += self.vel

        #Calculate the angle the deflector is facing by finding the vector between the mouse and the player and getting the angle of it
        self.deflector_angle = -(Vec2.from_tuple(input_state.mouse_pos) - self.pos).angle()


    def render(self, screen):
        # Draw the main player
        pygame.draw.circle(screen, (0,0,0), self.pos.to_int().to_tuple(), self.radius)


        # Find the middle of the deflector
        deflector_mid_point = self.pos + Vec2(self.deflector_distance_from_player*math.cos(self.deflector_angle),
                                              -self.deflector_distance_from_player*math.sin(self.deflector_angle))

        #Find the vector that takes you from the middle to the end of the deflector (to get to the start, just do the negative of this vector
        vec_to_end = Vec2((self.deflector_width/2)*math.sin(self.deflector_angle),
                          (self.deflector_width/2)*math.cos(self.deflector_angle))

        # Find the start and end of the deflector
        # These are stored as member variables because they are useful in the detection of collisions between the deflector and bullets
        self.deflector_start = deflector_mid_point - vec_to_end 
        self.deflector_end = deflector_mid_point + vec_to_end

        # Draw the deflector
        pygame.draw.line(screen, (0,0,0), self.deflector_start.to_int().to_tuple(), self.deflector_end.to_int().to_tuple())



