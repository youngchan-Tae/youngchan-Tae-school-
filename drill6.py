from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024



def handle_events():
    global running
    global x, y
    global mouse_x, mouse_y
    global frame
    global mx, my
    count = 0


    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, KPU_HEIGHT - 1 - event.y
            mouse.clip_draw(0, 0, 100, 100, mx, my)
            update_canvas()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
mx, my = 0, 0
frame = 0
hide_cursor()

while running:
    clear_canvas_now()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    mouse.clip_draw(0, 0, 100, 100, mx, my)
    update_canvas()
    handle_events()

close_canvas()
