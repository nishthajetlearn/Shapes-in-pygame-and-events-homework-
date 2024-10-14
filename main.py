import pygame

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))
blue = (0, 0, 255)
red = (255, 0, 0)
pygame.display.update()

# Circle class
class Circle():
    def __init__(self, color, pos, radius, width):
        self.circle_color = color
        self.circle_pos = pos
        self.circle_radius = radius
        self.circle_width = width
        self.circle_surface = screen

    def draw(self):
        self.Draw_Circle = pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)

    def grow(self, r):
        self.circle_radius = self.circle_radius + r
        self.Draw_Circle = pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)

# Rectangle class
class Rectangle():
    def __init__(self, color, pos, width, height, thickness):
        self.rect_color = color
        self.rect_pos = pos  # Position is the top-left corner (x, y)
        self.rect_width = width
        self.rect_height = height
        self.rect_thickness = thickness
        self.rect_surface = screen

    def draw(self):
        # Draw the rectangle using pygame.draw.rect
        self.Draw_Rect = pygame.draw.rect(
            self.rect_surface, 
            self.rect_color, 
            (self.rect_pos[0], self.rect_pos[1], self.rect_width, self.rect_height),
            self.rect_thickness
        )

    def grow(self, w, h):
        # Increase the rectangle's width and height
        self.rect_width += w
        self.rect_height += h
        # Redraw the rectangle
        self.Draw_Rect = pygame.draw.rect(
            self.rect_surface, 
            self.rect_color, 
            (self.rect_pos[0], self.rect_pos[1], self.rect_width, self.rect_height),
            self.rect_thickness
        )

# Create a Circle and Rectangle object
circle = Circle(blue, (300, 300), 50, 0)  # A circle at (300, 300) with radius 50
rectangle = Rectangle(red, (150, 150), 100, 50, 0)  # A rectangle at (150, 150) with width 100, height 50

# Main loop
while True:
    for event in pygame.event.get():
        # Close the game window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Draw the circle when the mouse button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255, 255, 255))  # Clear the screen
            circle.draw()  # Draw the circle
            rectangle.draw()  # Draw the rectangle
            pygame.display.update()

        # Grow the circle and rectangle when the mouse button is released
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255, 255, 255))  # Clear the screen
            circle.grow(10)  # Increase the circle's radius
            rectangle.grow(20, 10)  # Increase the rectangle's width by 20 and height by 10
            pygame.display.update()