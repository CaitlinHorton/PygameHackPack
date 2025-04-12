import pygame
import tkinter as tk
from tkinter import filedialog
# import Model

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED)

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
        pygame.draw.rect(screen, self.color, self.rect)  # Draw button
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# Function to display text in a scrollable box
def draw_text_box(screen, text_list, x, y, width, height, scroll_y):
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))  # Background
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height), 2)  # Border

    max_lines = height // 40 
    start_line = max(0, len(text_list) - max_lines - scroll_y)

    i = 0
    for line in text_list[start_line:]:
        text_surface = font.render(line, True, (0, 0, 0))
        screen.blit(text_surface, (x + 10, y + 10 + i * 40))
        i += 1

    # Draw scrollbar
    if len(text_list) > max_lines:
        scrollbar_height = int(height * max_lines / len(text_list))
        scrollbar_y = int((scroll_y / len(text_list)) * (height - scrollbar_height))
        pygame.draw.rect(screen, (0, 0, 0), (x + width - 10, y + scrollbar_y, 10, scrollbar_height))

# Function to open the file dialog and load an image
def upload_image():
    file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image Files", "*.jpg")])

    if file_path:
        try:
            # Load and resize the image to fit inside the display box
            print(file_path)
            print(file_path[(file_path.index("Images")):])
            image = pygame.image.load(file_path)
            image = pygame.transform.scale(image, (image_box_width - 20, image_box_height - 20))  # Fit inside the box
            return image, file_path  # Return both image and file path
        except pygame.error as e:
            print(f"Error loading image: {e}")
            return None, None
    return None, None

# Define Image Display Box dimensions
image_box_x = 790
image_box_y = 0
image_box_width = 400
image_box_height = 400

image = None

# Create buttons
okButton = Button(300, 700, 200, 80, (100, 255, 100), "Okay", (0, 0, 0))
notOkButton = Button(550, 700, 200, 80, (255, 100, 100), "Not Okay", (0, 0, 0))
uploadButton = Button(800, 700, 200, 80, (100, 180, 255), "Upload Image", (0, 0, 0))

# Create font
font = pygame.font.Font(None, 36)

# Main loop
run = True
display_text = ["No button clicked yet"]
scroll_y = 0

while run:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            # Okay Button
            if okButton.click(event.pos):
                display_text.append("Okay button clicked!")
                print("Okay button clicked!")

            # Not Okay Button    
            elif notOkButton.click(event.pos):
                display_text.append("Not okay button clicked!")
                print("Not Okay button clicked!")

            # Upload Button 
            elif uploadButton.click(event.pos):
                display_text.append("Upload Image")
                image, file_path = upload_image()
                if image:
                    display_text.append(f"Uploaded: {file_path[(file_path.index("Images")):]}")  # Append file path instead of image object
                    print("Image uploaded successfully!")


            # Scroll functionality
            if event.button == 4:
                scroll_y = max(0, scroll_y - 1)
            elif event.button == 5:
                scroll_y = min(len(display_text) - 1, scroll_y + 1)

    mouse_pos = pygame.mouse.get_pos()

    screen.fill((255, 255, 255))

    # Draw buttons
    okButton.draw(screen)
    notOkButton.draw(screen)
    uploadButton.draw(screen)

    # Draw text box
    draw_text_box(screen, display_text, 0, 0, 600, 500, scroll_y)

    # Draw the Image Display Box
    pygame.draw.rect(screen, (200, 200, 200), (image_box_x, image_box_y, image_box_width, image_box_height)) 
    pygame.draw.rect(screen, (0, 0, 0), (image_box_x, image_box_y, image_box_width, image_box_height), 2) 

    # Draw the uploaded image if available
    if image:
        screen.blit(image, (image_box_x + 10, image_box_y + 10)) 

    pygame.display.flip()

pygame.quit()