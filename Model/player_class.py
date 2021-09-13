import pygame

#Player icon made by Pixel Buddha from www.flaticon.com

class player_(pygame.sprite.Sprite):
    def __init__(self, player_file, starting_location, movement_speed, grav_factor, floor):
        super().__init__()
        self.image = pygame.image.load(player_file).convert_alpha()
        self.rect = self.image.get_rect(midbottom = starting_location)
        self.gravity = 0
        self.gravity_factor = grav_factor
        self.movement_speed = movement_speed
        self.applied_gravity = self.gravity_factor 
        self.floor = floor
        self.on_platform = False
        self.in_air = False
        

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.right += self.movement_speed
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and (self.rect.bottom == self.floor or self.on_platform):
                self.gravity = -self.applied_gravity
                self.in_air = True
        elif keys[pygame.K_LEFT]:
            self.rect.left -= self.movement_speed
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and (self.rect.bottom == self.floor or self.on_platform):
                self.gravity = -self.applied_gravity
                self.in_air = True
        elif keys[pygame.K_UP] and (self.rect.bottom == self.floor or self.on_platform):
            self.gravity = -self.applied_gravity
            self.in_air = True
        
        #create left border
        if self.rect.left <= 0:
            self.rect.left = 0
        
    def apply_gravity(self):
        if self.in_air:
            
            if not (self.gravity > self.gravity_factor):
                self.gravity += 1
                
            self.rect.y += self.gravity

            if self.rect.bottom >= self.floor:
                self.rect.bottom = self.floor


    def reset_position(self, location):
        self.rect.midbottom = (location)

    def reset_gravity(self):
        self.gravity = 0
        self.applied_gravity = self.gravity_factor

    def update(self):
        self.player_input()
        self.apply_gravity()