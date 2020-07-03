import pygame
import random
import sys

pygame.init()

win = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Sorting Visualizer")

# sound = True

nextSortTime = 0
nextSortDelay = 10

possibleHeights = []
heightsList = []
sortedList = []


def generateNewHeights():
    global possibleHeights, heightsList, sortedList

    sortedList = []
    possibleHeights = []
    heightsList = []

    for i in range(0, 720, 10):
        possibleHeights.append(i)

    for i in range(0, len(possibleHeights)):
        choice = random.choice(possibleHeights)
        possibleHeights.remove(choice)
        heightsList.append(choice)


def renderText(text, fontSize, pos, width, height, color=(0, 0, 0)):
    # LOAD FONT
    font = pygame.font.SysFont('Helvetica', fontSize)

    # SET TEXT
    textSurface = font.render(str(text), True, color)

    # CENTER TEXT
    textRect = textSurface.get_rect()
    textRect.center = ((pos[0] + (width / 2)), (pos[1] + (height / 2)))

    # DRAW TEXT TO WINDOW
    win.blit(textSurface, textRect)


def main():
    global sortedList, nextSortTime

    clock = pygame.time.Clock()

    sorting = False

    generateNewHeights()

    button0Rect = pygame.rect.Rect(440, 327.5, 200, 65)

    while True:
        clock.tick(60)

        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True

        win.fill((0, 0, 0))

        keys = pygame.key.get_pressed()

        mouseX, mouseY = pygame.mouse.get_pos()

        if keys[pygame.K_SPACE]:
            sorting = False
            generateNewHeights()
            nextSortTime = 0

        if button0Rect.collidepoint(mouseX, mouseY):
            if clicked:
                sorting = True
        if not sorting:
            pygame.draw.rect(win, (255, 255, 255), button0Rect)
            renderText("Start", 32, (440, 327.5), 200, 65)
        else:

            if len(heightsList) != 0:
                nextSortTime += 1

                if nextSortTime >= nextSortDelay:
                    sortedList.append(min(heightsList))
                    heightsList.remove(min(heightsList))
                    nextSortTime = 0

            index = 0
            for height in sortedList:
                pygame.draw.rect(win, (255, height / 5, height / 5), (index * 15, 720 - height, 15, height))
                index += 1

            for height in heightsList:
                pygame.draw.rect(win, (255, height / 5, height / 5), (index * 15, 720 - height, 15, height))
                index += 1

        pygame.display.update()


if __name__ == '__main__':
    main()
