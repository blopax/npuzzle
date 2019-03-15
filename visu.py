import pygame


width = 1024
height = 640
board_width = height * 4 // 5


def visualization(solution_list, board_size, solution_info):
    tile_size = board_width // board_size
    step = 0
    show_visu = True

    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("N_puzzle")
    pygame.mixer.music.load('Builder_Game_Weapon_Whip_1.mp3')
    while show_visu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                show_visu = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and step < len(solution_list) - 1:
                pygame.mixer.music.play()
                step += 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and step > 0:
                pygame.mixer.music.play()
                step -= 1

        draw_board(window, solution_list[step].state, tile_size, board_size)
        write_info(window, step, solution_info)
        pygame.display.flip()


def draw_board(window, state, tile_size, board_size):
    for index, item in enumerate(state):
        draw_tile(window, item, index, board_size, tile_size)


def draw_tile(window, tile_number, position, board_size, tile_size):
    basic_font = pygame.font.Font('freesansbold.ttf', 20)
    x_position = position % board_size
    y_position = position // board_size
    tile_x_position = x_position * tile_size
    tile_y_position = y_position * tile_size
    tile = str(tile_number) if tile_number > 0 else None
    content = basic_font.render(tile, True, (255, 255, 255))

    pygame.draw.rect(window, (123, 0, 0), (tile_x_position, tile_y_position, tile_size, tile_size))
    pygame.draw.rect(window, (255, 255, 255), (tile_x_position, tile_y_position, tile_size, tile_size), 3)
    text_position = content.get_rect()
    text_position.center = tile_x_position + int(tile_size / 2), tile_y_position + int(tile_size / 2)

    window.blit(content, text_position)


# noinspection SpellCheckingInspection
def write_info(window, step, solution_info):
    content = ["Step: {:0>{}}/{}".format(str(step), len(str(solution_info[0])), solution_info[0]),
               "Search algorithm used: {}".format(solution_info[3]),
               "Solution time complexity: {}".format(solution_info[1]),
               "Solution space_complexity: {}".format(solution_info[2])]
    basic_font = pygame.font.Font('Helvetica-Normal.ttf', 20)

    for index, item in enumerate(content):
        text_surf = basic_font.render(item, False, (123, 0, 0), (0, 0, 0))
        text_rect = text_surf.get_rect()
        if index == 0:
            top_adjustment = 30
        else:
            top_adjustment = 50
        text_rect.topleft = (board_width + 20, top_adjustment + index * 30)
        window.blit(text_surf, text_rect)
    if step == solution_info[0]:
        message = "Puzzle solved!!!"
        text_surf = basic_font.render(message, False, (123, 0, 0), (0, 0, 0))
        text_rect = text_surf.get_rect()
        text_rect.topleft = (board_width + 20, 300)
        window.blit(text_surf, text_rect)
    else:
        pygame.draw.rect(window, (0, 0, 0), (board_width, 300, width - board_width, 100))
