import pygame
import random

# Pygame setup
pygame.init()
Logo = pygame.image.load("IDk.png")
W_icon = pygame.image.load("L.png")
pygame.display.set_icon(W_icon)
pygame.display.set_caption('Wordle')
font = pygame.font.Font('Abel-Regular.ttf', 60)
font_small = pygame.font.Font('Abel-Regular.ttf', 30)
width,height = 1000,1000
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
dt = 0

# Game setup
word_file = open("words.txt",'r')
words_list = word_file.read().split()
key_pressed = ''
grid_coords = {}
grid_val = {} # (What, Does it have something, Where to display)
Xcoord = width/10 + 20
Ycoord = height/10 + 20
game_state = "start_game"
add_word = ''
game_result = 'lose'
result = ''

def get_random_word():
    wrd = random.choice(words_list)
    return wrd  

word = get_random_word()    

def reset_game():
    global grid_coords, grid_val, Xcoord, Ycoord, word, word_file, words_list
    word_file = open("words.txt",'r')
    words_list = word_file.read().split()
    word = get_random_word() 
    grid_coords = {}
    grid_val = {}
    for i in range(1,6):
            for j in range(1,6):
                grid_coords[f'C{i}R{j}'] = (Xcoord,Ycoord,136,136)
                grid_val[f'C{i}R{j}'] = ['',False,(grid_coords[f'C{i}R{j}'][0] + 65,grid_coords[f'C{i}R{j}'][1] + 65)]
                Xcoord = Xcoord + 136 + 20
            Xcoord = width/10 + 20
            Ycoord = Ycoord + 136 + 20    
    Xcoord = width/10 + 20
    Ycoord = height/10 + 20

reset_game()

def disp_letters():
    C1R1_text = font.render(grid_val['C1R1'][0], True, (255, 255, 255))
    C1R1_text_rect = C1R1_text.get_rect(center=grid_val['C1R1'][-1])
    screen.blit(C1R1_text, C1R1_text_rect)

    C1R2_text = font.render(grid_val['C1R2'][0], True, (255, 255, 255))
    C1R2_text_rect = C1R2_text.get_rect(center=grid_val['C1R2'][-1])
    screen.blit(C1R2_text, C1R2_text_rect)

    C1R3_text = font.render(grid_val['C1R3'][0], True, (255, 255, 255))
    C1R3_text_rect = C1R3_text.get_rect(center=grid_val['C1R3'][-1])
    screen.blit(C1R3_text, C1R3_text_rect)

    C1R4_text = font.render(grid_val['C1R4'][0], True, (255, 255, 255))
    C1R4_text_rect = C1R4_text.get_rect(center=grid_val['C1R4'][-1])
    screen.blit(C1R4_text, C1R4_text_rect)

    C1R5_text = font.render(grid_val['C1R5'][0], True, (255, 255, 255))
    C1R5_text_rect = C1R5_text.get_rect(center=grid_val['C1R5'][-1])
    screen.blit(C1R5_text, C1R5_text_rect)


    C2R1_text = font.render(grid_val['C2R1'][0], True, (255, 255, 255))
    C2R1_text_rect = C2R1_text.get_rect(center=grid_val['C2R1'][-1])
    screen.blit(C2R1_text, C2R1_text_rect)

    C2R2_text = font.render(grid_val['C2R2'][0], True, (255, 255, 255))
    C2R2_text_rect = C2R2_text.get_rect(center=grid_val['C2R2'][-1])
    screen.blit(C2R2_text, C2R2_text_rect)

    C2R3_text = font.render(grid_val['C2R3'][0], True, (255, 255, 255))
    C2R3_text_rect = C2R3_text.get_rect(center=grid_val['C2R3'][-1])
    screen.blit(C2R3_text, C2R3_text_rect)

    C2R4_text = font.render(grid_val['C2R4'][0], True, (255, 255, 255))
    C2R4_text_rect = C2R4_text.get_rect(center=grid_val['C2R4'][-1])
    screen.blit(C2R4_text, C2R4_text_rect)

    C2R5_text = font.render(grid_val['C2R5'][0], True, (255, 255, 255))
    C2R5_text_rect = C2R5_text.get_rect(center=grid_val['C2R5'][-1])
    screen.blit(C2R5_text, C2R5_text_rect)



    C3R1_text = font.render(grid_val['C3R1'][0], True, (255, 255, 255))
    C3R1_text_rect = C3R1_text.get_rect(center=grid_val['C3R1'][-1])
    screen.blit(C3R1_text, C3R1_text_rect)

    C3R2_text = font.render(grid_val['C3R2'][0], True, (255, 255, 255))
    C3R2_text_rect = C3R2_text.get_rect(center=grid_val['C3R2'][-1])
    screen.blit(C3R2_text, C3R2_text_rect)

    C3R3_text = font.render(grid_val['C3R3'][0], True, (255, 255, 255))
    C3R3_text_rect = C3R3_text.get_rect(center=grid_val['C3R3'][-1])
    screen.blit(C3R3_text, C3R3_text_rect)

    C3R4_text = font.render(grid_val['C3R4'][0], True, (255, 255, 255))
    C3R4_text_rect = C3R4_text.get_rect(center=grid_val['C3R4'][-1])
    screen.blit(C3R4_text, C3R4_text_rect)

    C3R5_text = font.render(grid_val['C3R5'][0], True, (255, 255, 255))
    C3R5_text_rect = C3R5_text.get_rect(center=grid_val['C3R5'][-1])
    screen.blit(C3R5_text, C3R5_text_rect)


    C4R1_text = font.render(grid_val['C4R1'][0], True, (255, 255, 255))
    C4R1_text_rect = C4R1_text.get_rect(center=grid_val['C4R1'][-1])
    screen.blit(C4R1_text, C4R1_text_rect)

    C4R2_text = font.render(grid_val['C4R2'][0], True, (255, 255, 255))
    C4R2_text_rect = C4R2_text.get_rect(center=grid_val['C4R2'][-1])
    screen.blit(C4R2_text, C4R2_text_rect)

    C4R3_text = font.render(grid_val['C4R3'][0], True, (255, 255, 255))
    C4R3_text_rect = C4R3_text.get_rect(center=grid_val['C4R3'][-1])
    screen.blit(C4R3_text, C4R3_text_rect)

    C4R4_text = font.render(grid_val['C4R4'][0], True, (255, 255, 255))
    C4R4_text_rect = C4R4_text.get_rect(center=grid_val['C4R4'][-1])
    screen.blit(C4R4_text, C4R4_text_rect)

    C4R5_text = font.render(grid_val['C4R5'][0], True, (255, 255, 255))
    C4R5_text_rect = C4R5_text.get_rect(center=grid_val['C4R5'][-1])
    screen.blit(C4R5_text, C4R5_text_rect)



    C5R1_text = font.render(grid_val['C5R1'][0], True, (255, 255, 255))
    C5R1_text_rect = C5R1_text.get_rect(center=grid_val['C5R1'][-1])
    screen.blit(C5R1_text, C5R1_text_rect)

    C5R2_text = font.render(grid_val['C5R2'][0], True, (255, 255, 255))
    C5R2_text_rect = C5R2_text.get_rect(center=grid_val['C5R2'][-1])
    screen.blit(C5R2_text, C5R2_text_rect)

    C5R3_text = font.render(grid_val['C5R3'][0], True, (255, 255, 255))
    C5R3_text_rect = C5R3_text.get_rect(center=grid_val['C5R3'][-1])
    screen.blit(C5R3_text, C5R3_text_rect)

    C5R4_text = font.render(grid_val['C5R4'][0], True, (255, 255, 255))
    C5R4_text_rect = C5R4_text.get_rect(center=grid_val['C5R4'][-1])
    screen.blit(C5R4_text, C5R4_text_rect)

    C5R5_text = font.render(grid_val['C5R5'][0], True, (255, 255, 255))
    C5R5_text_rect = C5R5_text.get_rect(center=grid_val['C5R5'][-1])
    screen.blit(C5R5_text, C5R5_text_rect)

def start_game():
    global running, start_text_rect, game_state, aw_text_rect, result, Logo
    screen.fill('#181b1c')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_text_rect.collidepoint(mouse_pos):
                game_state = "main_game"
            elif aw_text_rect.collidepoint(mouse_pos):
                game_state = "addWords_game"
 
    screen.blit(Logo, (width/4, 75))

    start_text = font.render("Start", True, (255, 255, 255))
    start_text_rect = start_text.get_rect(center=(width/2,height/2))
    screen.blit(start_text, start_text_rect)

    aw_text = font_small.render("Add Words", True, (255, 255, 255))
    aw_text_rect = aw_text.get_rect(center=(width/2,height/2 + 100))
    screen.blit(aw_text, aw_text_rect)

def main_game():
    global word, grid_val, running, key_pressed, game_state, game_result

    screen.fill('#181b1c')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key >= 97 and event.key <= 122:
                key_pressed = (str(chr(event.key).upper()))
                for i in grid_val:
                    if grid_val[i][1] == False:
                        grid_val[i][0] = str(chr(event.key).upper())
                        grid_val[i][1] = True
                        break
            else:
                pass

    disp_letters()

    #word_text = font.render(f"{word.upper()}", True, (255, 255, 255))
    #word_text_rect = word_text.get_rect(center=(width/2,(height/2) + (height/3)))
    #screen.blit(word_text, word_text_rect)

    pygame.draw.rect(screen,(255,255,255),(width/10,height/10,800,800),5, 15,) # Outline 

    pygame.draw.rect(screen,(255,255,255),grid_coords["C1R1"], 5, 15,) # C1R1
    pygame.draw.rect(screen,(255,255,255),grid_coords["C1R2"], 5, 15,) # C1R2
    pygame.draw.rect(screen,(255,255,255),grid_coords["C1R3"], 5, 15,) # C1R3
    pygame.draw.rect(screen,(255,255,255),grid_coords["C1R4"], 5, 15,) # C1R4
    pygame.draw.rect(screen,(255,255,255),grid_coords["C1R5"], 5, 15,) # C1R5

    pygame.draw.rect(screen,(255,255,255),grid_coords["C2R1"], 5, 15,) # C2R1
    pygame.draw.rect(screen,(255,255,255),grid_coords["C2R2"], 5, 15,) # C2R2
    pygame.draw.rect(screen,(255,255,255),grid_coords["C2R3"], 5, 15,) # C2R3
    pygame.draw.rect(screen,(255,255,255),grid_coords["C2R4"], 5, 15,) # C2R4
    pygame.draw.rect(screen,(255,255,255),grid_coords["C2R5"], 5, 15,) # C2R5

    pygame.draw.rect(screen,(255,255,255),grid_coords["C3R1"], 5, 15,) # C3R1
    pygame.draw.rect(screen,(255,255,255),grid_coords["C3R2"], 5, 15,) # C3R2
    pygame.draw.rect(screen,(255,255,255),grid_coords["C3R3"], 5, 15,) # C3R3
    pygame.draw.rect(screen,(255,255,255),grid_coords["C3R4"], 5, 15,) # C3R4
    pygame.draw.rect(screen,(255,255,255),grid_coords["C3R5"], 5, 15,) # C3R5

    pygame.draw.rect(screen,(255,255,255),grid_coords["C4R1"], 5, 15,) # C4R1
    pygame.draw.rect(screen,(255,255,255),grid_coords["C4R2"], 5, 15,) # C4R2
    pygame.draw.rect(screen,(255,255,255),grid_coords["C4R3"], 5, 15,) # C4R3
    pygame.draw.rect(screen,(255,255,255),grid_coords["C4R4"], 5, 15,) # C4R4
    pygame.draw.rect(screen,(255,255,255),grid_coords["C4R5"], 5, 15,) # C4R5

    pygame.draw.rect(screen,(255,255,255),grid_coords["C5R1"], 5, 15,) # C5R1
    pygame.draw.rect(screen,(255,255,255),grid_coords["C5R2"], 5, 15,) # C5R2
    pygame.draw.rect(screen,(255,255,255),grid_coords["C5R3"], 5, 15,) # C5R3
    pygame.draw.rect(screen,(255,255,255),grid_coords["C5R4"], 5, 15,) # C5R4
    pygame.draw.rect(screen,(255,255,255),grid_coords["C5R5"], 5, 15,) # C5R5

    for i in range(1,6):
        if grid_val[f'C{i}R1'][0] == word.upper()[0] :
            pygame.draw.rect(screen,(3, 252, 136),grid_coords[f'C{i}R1'], 5, 15,)
        elif grid_val[f'C{i}R1'][0] in word.upper() and grid_val[f'C{i}R1'][1] == True:
            pygame.draw.rect(screen,(240, 176, 58),grid_coords[f'C{i}R1'], 5, 15,)
        elif grid_val[f'C{i}R1'][0] != word.upper()[0] and grid_val[f'C{i}R1'][1] == True:
            pygame.draw.rect(screen,(181, 68, 40),grid_coords[f'C{i}R1'], 5, 15,)

        if grid_val[f'C{i}R2'][0] == word.upper()[1] :
            pygame.draw.rect(screen,(3, 252, 136),grid_coords[f'C{i}R2'], 5, 15,)
        elif grid_val[f'C{i}R2'][0] in word.upper() and grid_val[f'C{i}R2'][1] == True:
            pygame.draw.rect(screen,(240, 176, 58),grid_coords[f'C{i}R2'], 5, 15,)
        elif grid_val[f'C{i}R2'][0] != word.upper()[0] and grid_val[f'C{i}R2'][1] == True:
            pygame.draw.rect(screen,(181, 68, 40),grid_coords[f'C{i}R2'], 5, 15,)

        if grid_val[f'C{i}R3'][0] == word.upper()[2] :
            pygame.draw.rect(screen,(3, 252, 136),grid_coords[f'C{i}R3'], 5, 15,)
        elif grid_val[f'C{i}R3'][0] in word.upper() and grid_val[f'C{i}R3'][1] == True:
            pygame.draw.rect(screen,(240, 176, 58),grid_coords[f'C{i}R3'], 5, 15,)
        elif grid_val[f'C{i}R3'][0] != word.upper()[0] and grid_val[f'C{i}R3'][1] == True:
            pygame.draw.rect(screen,(181, 68, 40),grid_coords[f'C{i}R3'], 5, 15,)

        if grid_val[f'C{i}R4'][0] == word.upper()[3] :
            pygame.draw.rect(screen,(3, 252, 136),grid_coords[f'C{i}R4'], 5, 15,)
        elif grid_val[f'C{i}R4'][0] in word.upper() and grid_val[f'C{i}R4'][1] == True:
            pygame.draw.rect(screen,(240, 176, 58),grid_coords[f'C{i}R4'], 5, 15,)
        elif grid_val[f'C{i}R4'][0] != word.upper()[0] and grid_val[f'C{i}R4'][1] == True:
            pygame.draw.rect(screen,(181, 68, 40),grid_coords[f'C{i}R4'], 5, 15,)

        if grid_val[f'C{i}R5'][0] == word.upper()[4] :
            pygame.draw.rect(screen,(3, 252, 136),grid_coords[f'C{i}R5'], 5, 15,)
        elif grid_val[f'C{i}R5'][0] in word.upper() and grid_val[f'C{i}R5'][1] == True:
            pygame.draw.rect(screen,(240, 176, 58),grid_coords[f'C{i}R5'], 5, 15,)
        elif grid_val[f'C{i}R5'][0] != word.upper()[0] and grid_val[f'C{i}R5'][1] == True:
            pygame.draw.rect(screen,(181, 68, 40),grid_coords[f'C{i}R5'], 5, 15,)

            
        if grid_val[f'C{i}R1'][0] + grid_val[f'C{i}R2'][0] + grid_val[f'C{i}R3'][0] + grid_val[f'C{i}R4'][0] + grid_val[f'C{i}R5'][0] == word.upper():
             game_result = 'win'
             game_state = "end_game"
        elif grid_val['C5R5'][1] == True and grid_val[f'C{i}R1'][0] + grid_val[f'C{i}R2'][0] + grid_val[f'C{i}R3'][0] + grid_val[f'C{i}R4'][0] + grid_val[f'C{i}R5'][0] != word.upper():
             game_result = 'lose'
             game_state = "end_game"

def end_game():
    global running ,game_result, back_text_rect, game_state, tww_text_rect, Logo

    screen.fill('#181b1c')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if back_text_rect.collidepoint(mouse_pos):
                game_state = "start_game"
                reset_game()

    if game_result == "win":
        result = '!!! YAY, you won !!!'
    else :
        result = 'Better luck next time'

    screen.blit(Logo, (width/4, 75))

    YAY_text = font.render(result, True, (255, 255, 255))
    YAY_text_rect = YAY_text.get_rect(center=(width/2,height/2))
    screen.blit(YAY_text, YAY_text_rect)

    tww_text = font_small.render(f"The word was {word.lower().capitalize()}", True, (255, 255, 255))
    tww_text_rect = tww_text.get_rect(center=(width/2,height/2 + 50))
    screen.blit(tww_text, tww_text_rect)

    back_text = font_small.render("Back To Home", True, (255, 255, 255))
    back_text_rect = back_text.get_rect(center=(width / 2, height / 2 + height / 4 + 125))
    screen.blit(back_text, back_text_rect)

def add_words():
    global running, word_file, words_list, key_pressed, add_word, words_text, y_offset, font_small, font, width, height, screen, game_state, back_text_rect, clear_text_rect, confirm_text_rect

    screen.fill('#181b1c')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if back_text_rect.collidepoint(mouse_pos):
                game_state = "start_game"
            elif clear_text_rect.collidepoint(mouse_pos):
                add_word = ''
            elif confirm_text_rect.collidepoint(mouse_pos) and len(add_word) == 5:
                with open("words.txt", 'a') as wrdfile:
                    wrdfile.write(add_word.lower().capitalize() + '\n')
                    words_list.append(add_word.lower().capitalize())
                    add_word = ''
        elif event.type == pygame.KEYDOWN:
            if 97 <= event.key <= 122:  # Check if key is a lowercase letter
                key_pressed = chr(event.key).upper()
                add_word += key_pressed

    screen.blit(Logo, (width/4, 700))

    # Update words_text based on words_list
    words_text = [font_small.render(i.lower().capitalize(), True, (255, 255, 255)) for i in words_list]

    y_offset = 50
    for text_surface in words_text:
        screen.blit(text_surface, (50, y_offset))
        y_offset += 32

    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - 125, height / 2 + height / 4, 250, 100), 2, 15)  # Add Box
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 + 125 + 10, height / 2 + height / 4 + 25, 150, 50), 2, 15) # Clear
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - 125 - 150 - 10, height / 2 + height / 4 + 25, 150, 50), 2, 15) # Confirm

    add_text = font.render(add_word, True, (255, 255, 255))
    add_text_rect = add_text.get_rect(center=(width / 2, height / 2 + height / 4 + 50))
    screen.blit(add_text, add_text_rect)

    clear_text = font_small.render("Clear", True, (255, 255, 255))
    clear_text_rect = clear_text.get_rect(center=(width / 2 + 125 + 75 + 10, height / 2 + height / 4 + 50))
    screen.blit(clear_text, clear_text_rect)

    confirm_text = font_small.render("Confirm", True, (255, 255, 255))
    confirm_text_rect = confirm_text.get_rect(center=(width / 2 - 125 - 75 - 10, height / 2 + height / 4 + 50))
    screen.blit(confirm_text, confirm_text_rect)

    back_text = font_small.render("Back To Home", True, (255, 255, 255))
    back_text_rect = back_text.get_rect(center=(width / 2, height / 2 + height / 4 + 125))
    screen.blit(back_text, back_text_rect)

    pygame.display.flip()

while running:
    # Game code
    if game_state == "start_game":
        start_game()
    elif game_state == "main_game":
        main_game()
    elif game_state == "end_game":
        end_game()
    elif game_state == "addWords_game":
        add_words()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
pygame.quit()