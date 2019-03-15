import pygame
import os


width = 1400
height = 960
board_width = height * 3 // 5


def visualization(info, visu_mode):
    info['tile_size'], info['sound'] = board_width // info['board_size'], None
    info['cpu_step'], info['player_step'] = 0, 0
    info['player_state'], info['cpu_state'] = info['initial_state'], info['initial_state']
    show_visu = True

    pygame.init()
    if visu_mode == 'fight':
        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("N_puzzle: battle to death")
    else:
        window = pygame.display.set_mode((width // 2, height))
        pygame.display.set_caption("N_puzzle: learn from the master")
    info = music_update(info)
    while show_visu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                show_visu = False
            if event.type == pygame.KEYDOWN:
                info = update_info(info, event.key, visu_mode)
                info = music_update(info, event.key)
        if visu_mode == 'fight':
            solution_visualization(window, board_width + 230, info)
            player_visualization(window, 20, info)
        else:
            solution_visualization(window, 20, info)
        pygame.display.flip()


def music_update(info, key=None):
    if key is None:
        if os.path.exists('music.mp3'):
            pygame.mixer.music.load('music.mp3')
            pygame.mixer.music.play()
        if os.path.exists('sound.wav'):
            info['sound'] = pygame.mixer.Sound('sound.wav')
    if key == pygame.K_m and os.path.exists('music.mp3'):
        pygame.mixer.music.stop()

    return info


def update_info(info, key, visu_mode):
    play_sound = False
    if visu_mode == 'fight' and key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_DOWN, pygame.K_UP]:
        info = move(info, key)
        info['cpu_state'] = info['solution_list'][info['cpu_step']].state
        play_sound = True
    if visu_mode != 'fight' and key == pygame.K_RIGHT and info['cpu_step'] < info['search_algo_best_solution']:
        info['cpu_step'] += 1
        info['cpu_state'] = info['solution_list'][info['cpu_step']].state
        play_sound = True
    if visu_mode != 'fight' and key == pygame.K_LEFT and info['cpu_step'] > 0:
        info['cpu_step'] -= 1
        info['cpu_state'] = info['solution_list'][info['cpu_step']].state
        play_sound = True
    if play_sound is True and 'sound' in info.keys():
        info['sound'].play()
    return info


def player_visualization(window, position, info):
    draw_board(window, position, (0, 123, 0), info['player_state'], info)
    content = ["Step: {}".format(info['player_step'])]
    info['player_solved'] = info['player_state'] == info['goal_state']
    write_info(window, position, content, info['player_solved'])  # content, solved, board_width + 230)


def solution_visualization(window, position, info):
    draw_board(window, position, (123, 0, 0), info['cpu_state'], info)
    content = ["Step: {:0>{}}/{}".format(info['cpu_step'], len(str(info['search_algo_best_solution'])),
                                         info['search_algo_best_solution']),
               "Search algorithm used: {}".format(info['search_algo']),
               "Solution time complexity: {}".format(info['time_complexity']),
               "Solution space_complexity: {}".format(info['space_complexity'])]
    info['cpu_solved'] = info['cpu_step'] == info['search_algo_best_solution']
    write_info(window, position, content, info['cpu_solved'])


def draw_board(window, x_offset, color, state, info):
    basic_font = pygame.font.Font('freesansbold.ttf', 20)
    tile_size = info['tile_size']
    for position, tile_number in enumerate(state):
        x_position = position % info['board_size']
        y_position = position // info['board_size']
        tile_x_position = x_position * tile_size + x_offset
        tile_y_position = y_position * tile_size
        tile = str(tile_number) if tile_number > 0 else None
        content = basic_font.render(tile, True, (255, 255, 255))

        pygame.draw.rect(window, color, (tile_x_position, tile_y_position, tile_size, tile_size))
        pygame.draw.rect(window, (255, 255, 255), (tile_x_position, tile_y_position, tile_size, tile_size), 3)
        text_position = content.get_rect()
        text_position.center = tile_x_position + int(tile_size / 2), tile_y_position + int(tile_size / 2)

        window.blit(content, text_position)


# noinspection SpellCheckingInspection
def write_info(window, x_position, content, solved):
    basic_font = pygame.font.Font('Helvetica-Normal.ttf', 20)

    for index, item in enumerate(content):
        text_surf = basic_font.render(item, False, (123, 0, 0), (0, 0, 0))
        text_rect = text_surf.get_rect()
        if index == 0:
            top_adjustment = 30
        else:
            top_adjustment = 50
        text_rect.topleft = (x_position, board_width + top_adjustment + index * 30)
        window.blit(text_surf, text_rect)
    if solved:
        message = "Puzzle solved!!!"
        text_surf = basic_font.render(message, False, (123, 0, 0), (0, 0, 0))
        text_rect = text_surf.get_rect()
        text_rect.topleft = (x_position, board_width + 200)
        window.blit(text_surf, text_rect)
    else:
        pygame.draw.rect(window, (0, 0, 0), (x_position, board_width + 200, board_width, 100))


def move(info, key):
    player_state, cpu_step, player_step = info['player_state'], info['cpu_step'], info['player_step']
    board_size = info['board_size']
    x_zero = player_state.index(0) % board_size
    y_zero = player_state.index(0) // board_size

    if x_zero > 0 and key == pygame.K_RIGHT:
        player_state[y_zero * board_size + x_zero] = player_state[y_zero * board_size + x_zero - 1]
        player_state[y_zero * board_size + x_zero - 1] = 0
        player_step += 1
        cpu_step += cpu_step < info['search_algo_best_solution']
    if x_zero < board_size - 1 and key == pygame.K_LEFT:
        player_state[y_zero * board_size + x_zero] = player_state[y_zero * board_size + x_zero + 1]
        player_state[y_zero * board_size + x_zero + 1] = 0
        player_step += 1
        cpu_step += cpu_step < info['search_algo_best_solution']
    if y_zero < board_size - 1 and key == pygame.K_UP:
        player_state[y_zero * board_size + x_zero] = player_state[y_zero * board_size + x_zero + board_size]
        player_state[y_zero * board_size + x_zero + board_size] = 0
        player_step += 1
        cpu_step += cpu_step < info['search_algo_best_solution']
    if y_zero > 0 and key == pygame.K_DOWN:
        player_state[y_zero * board_size + x_zero] = player_state[y_zero * board_size + x_zero - board_size]
        player_state[y_zero * board_size + x_zero - board_size] = 0
        player_step += 1
        cpu_step += cpu_step < info['search_algo_best_solution']
    info['player_state'], info['cpu_step'], info['player_step'] = player_state, cpu_step, player_step
    return info
