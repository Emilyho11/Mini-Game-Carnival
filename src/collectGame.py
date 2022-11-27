import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BROWN = (178,146,103)
GREEN = (131,231,73)
BLUE = (165,222,233)
DARKBLUE = (139,153,186)
GREY = (231,231,231)
DARKGREY = (172,172,172)
PINK = (255,191,221)

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y


class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()


# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
gamewindow = pygame.display.set_mode([1200, 800])

# Set the title of the window
pygame.display.set_caption('Test')

# Create the player object
player = Player(50, 50)
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)

for i in range(50):
    # This represents a block
    block = Block(YELLOW, 20, 15)

    # Set a random location for the block
    block.rect.x = random.randrange(1100)
    block.rect.y = random.randrange(700)

    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

clock = pygame.time.Clock()
score = 0
done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    # --- Game logic

    # This calls update on all the sprites
    all_sprites_list.update()

    # -- Draw everything
    # Clear screen
    gamewindow.fill(GREEN)

    # Output the Score
    font = pygame.font.SysFont('modernno20', 30)
    scorefont = font.render("Score: " + str(score), True, BLACK)
    Scorefont = scorefont.get_rect()
    Scorefont.center = (600, 80)
    gamewindow.blit(scorefont, Scorefont)

    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print(score)

    # Draw sprites
    all_sprites_list.draw(gamewindow)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(60)

pygame.quit()