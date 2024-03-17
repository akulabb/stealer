import socket
import pygame
import json


SERVER = 'localhost'
PORT = 1602
SCREEN_HEIGHT = 970
SCREEN_WIDTH = 1280
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((SERVER, PORT))
socket.listen()
user_socket, address = socket.accept()

user_keys = {}

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    byte_data = user_socket.recv(1024)
    str_data = byte_data.decode()
    user_keys = json.loads(str_data)
    x = 25
    y = 50
    screen.fill(WHITE)
    for key, value in user_keys.items():
        pygame.draw.rect(screen, BLACK, (x, y + 50, 30, value))
        name_font = pygame.font.Font(None, 25)
        number_font = pygame.font.Font(None, 20)
        name = name_font.render(key, True, BLACK)
        screen.blit(name, (x, y))
        number = number_font.render(str(value), True, BLACK)
        screen.blit(number, (x, y + 20))
        x += 100
        if x >= SCREEN_WIDTH:
            y += 250
            x = 25

    pygame.display.flip()
    

pygame.quit()