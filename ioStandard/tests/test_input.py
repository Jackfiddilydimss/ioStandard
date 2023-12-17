import pygame
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ioStandard.input import textBox  # Assuming your module is in the ioStandard package
from ioStandard.output import text

pygame.init()

width, height = 800, 600
sc = pygame.display.set_mode((width, height))
pygame.display.set_caption("Input Test")

def test01():
    # Create UI Elements
    inputBox = textBox(100, 100, prompt="Enter Text: ")
    currentText = text(100, 164)
    outputText = text(100, 196)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            inputBox.handleEvent(event)

        # Logic
        currentText.text = inputBox.text
        outputText.text = inputBox.finalText

        # Render
        sc.fill((255,214,186))
        inputBox.draw(sc)
        currentText.draw(sc)
        outputText.draw(sc)

        pygame.display.flip()

    pygame.quit()

test01()