import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image Upload Example")

# Initialize tkinter
root = tk.Tk()
root.withdraw()  # Hide the tkinter root window

# Define Button class
class Button:
    def __init__(self, x, y, width, height, color, text, text_color, font_size=40):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, font_size)
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        # Draw button
        pygame.draw.rect(screen, self.color, self.rect)
        # Draw text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_hovered(self, mouse_pos):
        # Check if the mouse is over the button
        return self.rect.collidepoint(mouse_pos)

    def click(self, mouse_pos):
        # Check if the mouse click is inside the button
        return self.rect.collidepoint(mouse_pos)

# Function to open the file dialog and load an image
def upload_image():
    # Ask the user to select a file
    file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image Files", "*.jpg; *.png; *.jpeg")])

    if file_path:
        try:
            # Load and resize the image to fit inside the display box
            print(file_path)
            print(file_path[(file_path.index("Images")):])
            image = pygame.image.load(file_path)
            image = pygame.transform.scale(image, (image_box_width - 20, image_box_height - 20))  # Fit inside the box
            return image
        except pygame.error as e:
            print(f"Error loading image: {e}")
            return None
    return None

# Define Image Display Box dimensions
image_box_x = 800
image_box_y = 100
image_box_width = 350
image_box_height = 500

# Create the Upload Button
upload_button = Button(100, 700, 200, 80, (0, 0, 255), "Upload Image", (255, 255, 255))

# Variable to store the loaded image
image = None

# Main loop
run = True
while run:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Check if the upload button is clicked
            if upload_button.click(mouse_pos):
                image = upload_image()
                if image:
                    print("Image uploaded successfully!")

    # Get mouse position for hover effect
    mouse_pos = pygame.mouse.get_pos()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the Image Display Box
    pygame.draw.rect(screen, (200, 200, 200), (image_box_x, image_box_y, image_box_width, image_box_height))  # Gray background
    pygame.draw.rect(screen, (0, 0, 0), (image_box_x, image_box_y, image_box_width, image_box_height), 2)  # Black border

    # Draw the uploaded image if available
    if image:
        screen.blit(image, (image_box_x + 10, image_box_y + 10))  # Add padding inside the box

    # Draw the Upload button
    upload_button.draw(screen)

    # Add hover effect (change color when hovering over the button)
    if upload_button.is_hovered(mouse_pos):
        upload_button.color = (0, 0, 200)  # Darker blue when hovered
    else:
        upload_button.color = (0, 0, 255)  # Original blue color

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()