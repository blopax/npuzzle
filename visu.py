import pygame
import os


width = 1400
height = 960
board_width = height * 3 // 5


def visualization(info, solution_list) -> None:
    """
    Check if visualization should be shown. If so prepares the info dictionary that will be used.
    :param dict info:
    :param list solution_list:
    :return None:
    """
    if info['show_visu'] is False:
        return None
    else:
        info['solution_list'] = solution_list
        info['search_algo_best_solution'] = len(solution_list) - 1
        info['initial_state'] = solution_list[0].state
        info['goal_state'] = solution_list[len(solution_list) - 1].state
        info['tile_size'] = board_width // info['board_size']
        info['sound'] = None
        info['cpu_step'], info['player_step'] = 0, 0
        info['cpu_state'], info['player_state'] = info['initial_state'], info['initial_state']
        return show_visualization(info)


def show_visualization(info) -> None:
    """
    Runs visualization.
    :param dict info:
    :return None:
    """
    pygame.init()
    if info['visu_mode'] == 'fight':
        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("N_puzzle: battle to death")
    else:
        window = pygame.display.set_mode((width // 2, height))
        pygame.display.set_caption("N_puzzle: learn from the master")
    info = music_update(info)
    while info['show_visu']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                info['show_visu'] = False
            if event.type == pygame.KEYDOWN:
                info = update_info(info, event.key)
                info = music_update(info, event.key)
        if info['visu_mode'] == 'fight':
            solution_visualization(window, board_width + 230, info)
            player_visualization(window, 20, info)
        else:
            solution_visualization(window, 20, info)
        pygame.display.flip()


def music_update(info, key=None) -> dict:
    """
    Updates music and sounds options
    :param dict info:
    :param event.key key: Key pressed by player
    :return dict info:
    """
    if key is None:
        if os.path.exists('music.mp3'):
            pygame.mixer.music.load('music.mp3')
            pygame.mixer.music.play()
        if os.path.exists('sound.wav'):
            info['sound'] = pygame.mixer.Sound('sound.wav')
    if key == pygame.K_m and os.path.exists('music.mp3'):
        pygame.mixer.music.stop()
    return info


def update_info(info, key) -> dict:
    """
    Updates board info and plays sounds if needed.
    :param dict info:
    :param event.key key: Key pressed by player
    :return dict info:
    """
    play_sound = False
    if info['visu_mode'] == 'fight' and key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_DOWN, pygame.K_UP]:
        info = move(info, key)
        info['cpu_state'] = info['solution_list'][info['cpu_step']].state
        play_sound = True
    if info['visu_mode'] != 'fight' and key == pygame.K_RIGHT and info['cpu_step'] < info['search_algo_best_solution']:
        info['cpu_step'] += 1
        info['cpu_state'] = info['solution_list'][info['cpu_step']].state
        play_sound = True
    if info['visu_mode'] != 'fight' and key == pygame.K_LEFT and info['cpu_step'] > 0:
        info['cpu_step'] -= 1
        info['cpu_state'] = info['solution_list'][info['cpu_step']].state
        play_sound = True
    if play_sound is True and info["sound"] is not None:
        info['sound'].play()
    return info


def player_visualization(window, position, info) -> None:
    """
    Prepares and show player's board and text.
    :param window:
    :param int position: Where to show this in the window.
    :param dict info:
    :return None:
    """
    draw_board(window, position, (0, 123, 0), info['player_state'], info)
    content = ["Step: {}".format(info['player_step'])]
    info['player_solved'] = info['player_state'] == info['goal_state']
    write_info(window, position, content, info['player_solved'])


def solution_visualization(window, position, info) -> None:
    """
    Prepares and show computer's board and text.
    :param window:
    :param int position: Where to show this in the window.
    :param dict info:
    :return None:
    """
    draw_board(window, position, (123, 0, 0), info['cpu_state'], info)
    content = ["Move: {:0>{}}/{}".format(info['cpu_step'], len(str(info['search_algo_best_solution'])),
                                         info['search_algo_best_solution']),
               "Search algorithm used: {}".format(info['search_algo']),
               "Solution time complexity: {}".format(info['time_complexity']),
               "Solution space_complexity: {}".format(info['space_complexity'])]
    if info['show_time']:
        content.append("Effective time taken: {}s".format(info['time']))
    info['cpu_solved'] = info['cpu_step'] == info['search_algo_best_solution']
    write_info(window, position, content, info['cpu_solved'])


def draw_board(window, x_offset, color, state, info) -> None:
    """
    Function that draws the board.
    :param window:
    :param int x_offset:
    :param tuple color:
    :param list state:
    :param dict info:
    :return None:
    """
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
def write_info(window, x_position, content, solved) -> None:
    """
    Write text below the board with relevant information.
    :param window:
    :param x_position: Where to write the information
    :param list content: List of sentences that will be written on different lines
    :param bool solved: Boolean that says if puzzle is solved or not
    :return None:
    """
    basic_font = pygame.font.Font('freesansbold.ttf', 20)

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


def move(info, key) -> dict:
    """
    Updates player state according to the key pressed by player.
    :param dict info:
    :param event.key key:
    :return dict info:
    """
    player_state, cpu_step, player_step = info['player_state'], info['cpu_step'], info['player_step']
    board_size = info['board_size']
    x_zero, y_zero = player_state.index(0) % board_size, player_state.index(0) // board_size
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
