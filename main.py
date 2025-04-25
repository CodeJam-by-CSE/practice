# main file
import pygame
import sys
import datetime
from src.calculator import (
    calculate_average,
    calculate_grade,
    validate_scores,
    time_left_until_competition,
    get_result_text_color,
    get_time_left_text_color,
)

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grade Calculator Visualizer")

font = pygame.font.Font(None, 32)
input_box = pygame.Rect(50, 100, 500, 40)
color_inactive = pygame.Color("lightskyblue3")
color_active = pygame.Color("dodgerblue2")
color = color_inactive

text = ""
active = False
result_text = ""
button_rect = pygame.Rect(50, 160, 120, 40)
clear_button_rect = pygame.Rect(200, 160, 120, 40)

# Set competition end time (change as needed)
competition_end = datetime.datetime(2025, 4, 30, 23, 59, 59)

color_map = {
    "green": pygame.Color("green"),
    "red": pygame.Color("red"),
    "blue": pygame.Color("blue"),
}


def draw_button(rect, text, screen):
    pygame.draw.rect(screen, pygame.Color("lightgray"), rect)
    label = font.render(text, True, pygame.Color("black"))
    screen.blit(label, (rect.x + 10, rect.y + 5))


while True:
    screen.fill((255, 255, 255))

    time_left_text = time_left_until_competition(competition_end)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            if button_rect.collidepoint(event.pos):
                scores = validate_scores(text)
                if scores is not None:
                    avg = calculate_average(scores)
                    grade = calculate_grade(avg)  # use avg instead of scores[-1]
                    result_text = f"Average: {avg:.2f}, Grade: {grade}"
                else:
                    result_text = "Invalid input"

            elif clear_button_rect.collidepoint(event.pos):
                text = ""
                result_text = ""
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    pass
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Draw input box
    color = color_active if active else color_inactive
    pygame.draw.rect(screen, color, input_box, 2)
    txt_surface = font.render(text, True, pygame.Color("black"))
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

    # Draw buttons
    draw_button(button_rect, "Calculate", screen)
    draw_button(clear_button_rect, "Clear", screen)

    result_text_color = color_map[get_result_text_color(result_text)]
    time_text_color = color_map[get_time_left_text_color(time_left_text)]

    # Display result text
    if result_text:
        result_surface = font.render(result_text, True, result_text_color)
        screen.blit(result_surface, (50, 230))

    # Display countdown timer
    time_surface = font.render(time_left_text, True, time_text_color)
    screen.blit(time_surface, (50, 20))

    pygame.display.flip()
    pygame.time.Clock().tick(30)
