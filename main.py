import pygame

pygame.init()

size = (900, 780)
display = pygame.display.set_mode(size)
caption = "SuperEngine"
pygame.display.set_caption(caption)

class game:
    def __init__():
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            pygame.display.flip()
            
pygame.quit()
            
if __name__ == '__main__':
    gameplay = game
    gameplay.run()
