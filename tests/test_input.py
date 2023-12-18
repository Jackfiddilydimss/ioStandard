import pygame
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ioStandard.input import textBox, slider, button, checkBox, fileUploader
from ioStandard.output import text, progressBar

pygame.init()
clock = pygame.time.Clock()

width, height = 800, 600
sc = pygame.display.set_mode((width, height))
pygame.display.set_caption("Input Test")

def test01():
    # Create UI Elements
    inputBox = textBox(100, 100, prompt="Enter Text: ")
    currentText = text(100, 164)
    outputText = text(100, 196)

    inputSlider = slider(0, 250, width)
    sliderText = text(100, 282)
    percentText = text(100, 314)
    progressBarTest = progressBar(0, 200, width)

    buttonTest = button(100, 350, lambda: print("Pressed"))

    buttonTestToggle = button(100, 400, lambda: print("Pressed"), toggleable=True)

    checkBoxTest = checkBox(100, 500, lambda: print("Toggled"))

    fileUploaderTest = fileUploader(200, 100)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            inputBox.handleEvent(event)
            inputSlider.handleEvent(event)
            buttonTest.handleEvent(event)
            buttonTestToggle.handleEvent(event)
            checkBoxTest.handleEvent(event)
            fileUploaderTest.handleEvent(event)

        # Logic
        currentText.text = inputBox.text
        outputText.text = inputBox.finalText
        sliderText.text = f"Value: {inputSlider.value}"
        percentText.text = f"Value: {inputSlider.percent}%"
        progressBarTest.setValue(inputSlider.value)

        if buttonTestToggle.selected:
            print("Toggled On.")

        # Render
        sc.fill((255,214,186))
        inputBox.draw(sc)
        currentText.draw(sc)
        outputText.draw(sc)
        inputSlider.draw(sc)
        sliderText.draw(sc)
        percentText.draw(sc)
        buttonTest.draw(sc)
        buttonTestToggle.draw(sc)
        checkBoxTest.draw(sc)
        fileUploaderTest.draw(sc)
        progressBarTest.draw(sc)

        pygame.display.flip()

    pygame.quit()

test01()