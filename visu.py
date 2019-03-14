import pygame


def visualization(solution_list, board_size):
    pygame.init()

    HEIGHT = 960
    WIDTH = 640
    BOARD_WIDTH = WIDTH
    TILE_SIZE = BOARD_WIDTH // board_size
    window = pygame.display.set_mode((HEIGHT, WIDTH))

    pygame.display.set_caption("N_puzzle")
    step = 0

    show_visu = True
    while show_visu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                show_visu = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and step < len(solution_list) - 1:
                step += 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and step > 0:
                step -= 1

        draw_board(window, solution_list[step].state, TILE_SIZE,
                   board_size)  # change when actual solution_list and use state
        print(solution_list[step].heuristic)
        pygame.display.flip()
        continue


def draw_board(window, state, TILE_SIZE, board_size):
    for index, item in enumerate(state):
        draw_tile(window, item, index, board_size, TILE_SIZE)


def draw_tile(window, tile_number, position, board_size, tile_size):
    BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
    x_position = position % board_size
    y_position = position // board_size
    tile_x_position = x_position * tile_size
    tile_y_position = y_position * tile_size

    if tile_number > 0:
        content = BASICFONT.render(str(tile_number), True, (255, 255, 255))
    else:
        content = BASICFONT.render(str(''), True, (0, 0, 0))

    pygame.draw.rect(window, (123, 0, 0), (tile_x_position, tile_y_position, tile_size, tile_size))
    pygame.draw.rect(window, (255, 255, 255), (tile_x_position, tile_y_position, tile_size, tile_size), 3)
    text_position = content.get_rect()
    text_position.center = tile_x_position + int(tile_size / 2), tile_y_position + int(tile_size / 2)
    print(x_position, y_position, tile_x_position, tile_y_position, text_position.center)

    window.blit(content, text_position)


if __name__ == "__main__":
    visualization([1, 2, 3, 0, 4, 5, 6, 7, 8], 3)
