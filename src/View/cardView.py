import pygame

# Draw token cards from deck
def drawTokenCardsFromDeck(cards, window, xCenter, yCenter, font):
    n = len(cards)
    cardWidth = 200
    cardHeight = 200
    vspace = 20
    startX = xCenter - (cardWidth*(n/2))
    startY = yCenter - (cardHeight/2)
    if(n%2 == 0):
        startX -= (vspace/2)+(vspace*((n/2) -1))
    else:
        startX -= int(n/2)*vspace
    for i in range(n):
        image = cards[i].getImage()
        image = pygame.transform.scale(image, (cardWidth, cardHeight))
        cards[i].drawCard(image, window, startX+((cardWidth+vspace)*i), startY, font)
