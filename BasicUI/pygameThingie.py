import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED)

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

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# Create buttons
okButton = Button(300, 700, 200, 80, (0, 255, 0), "Okay", (0, 0, 0))
notOkButton = Button(550, 700, 200, 80, (255, 0, 0), "Not Okay", (0, 0, 0))
uploadButton = Button(800, 700, 200, 80, (0, 0, 255), "Upload Image", (255, 255, 255))  # New blue button

# Create font
font = pygame.font.Font(None, 36)

# Function to display text in a scrollable box
def draw_text_box(screen, text_list, x, y, width, height, scroll_y):
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))  # Background
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height), 2)  # Border

    max_lines = height // 40  # Max lines that fit
    start_line = max(0, len(text_list) - max_lines - scroll_y)  # Scroll effect

    i = 0
    for line in text_list[start_line:]:
        text_surface = font.render(line, True, (0, 0, 0))
        screen.blit(text_surface, (x + 10, y + 10 + i * 40))
        i += 1

    # Draw scrollbar if needed
    if len(text_list) > max_lines:
        scrollbar_height = int(height * max_lines / len(text_list))
        scrollbar_y = int((scroll_y / len(text_list)) * (height - scrollbar_height))
        pygame.draw.rect(screen, (0, 0, 0), (x + width - 10, y + scrollbar_y, 10, scrollbar_height))

# Main loop
run = True
display_text = ["No button clicked yet"]
scroll_y = 0

# Events
while run:
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
                print("Upload Image button clicked!")

            # Scroll functionality
            if event.button == 4:  # Scroll up
                scroll_y = max(0, scroll_y - 1)
            elif event.button == 5:  # Scroll down
                scroll_y = min(len(display_text) - 1, scroll_y + 1)

    mouse_pos = pygame.mouse.get_pos()

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw buttons
    okButton.draw(screen)
    notOkButton.draw(screen)
    uploadButton.draw(screen)

    # Hover effect
    okButton.color = (0, 200, 0) if okButton.is_hovered(mouse_pos) else (0, 255, 0)
    notOkButton.color = (200, 0, 0) if notOkButton.is_hovered(mouse_pos) else (255, 0, 0)
    uploadButton.color = (0, 0, 200) if uploadButton.is_hovered(mouse_pos) else (0, 0, 255) 

    # Draw text box
    draw_text_box(screen, display_text, 0, 0, 400, 400, scroll_y)

    pygame.display.flip()

pygame.quit()
