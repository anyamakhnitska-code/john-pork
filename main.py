import pygame
import sys
import os
import subprocess
import time

# ---------- АВТОШЛЯХ ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------- НАЛАШТУВАННЯ ----------
WIDTH, HEIGHT = 720, 1080 
FPS = 60
GREEN_BTN_POS = (420, 850)
RED_BTN_POS = (120, 850)

# ---------- ІНІЦІАЛІЗАЦІЯ ----------
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("John Pork is calling...")
clock = pygame.time.Clock()

# ---------- ЗАВАНТАЖЕННЯ ----------
try:
    bg = pygame.image.load(os.path.join(BASE_DIR, "img", "john pork.jpg"))
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
    pick_up = pygame.image.load(os.path.join(BASE_DIR, "img", "pick up.png")).convert_alpha()
    decline = pygame.image.load(os.path.join(BASE_DIR, "img", "decline.png")).convert_alpha()
except Exception as e:
    print(f"Помилка: {e}")

font_title = pygame.font.SysFont("Arial", 48, bold=True)
font_hacker = pygame.font.SysFont("Consolas", 30, bold=True)

sound_path = os.path.join(BASE_DIR, "sounds", "call_sound.mp3")
if os.path.exists(sound_path):
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play(-1)

# ---------- ФУНКЦІЇ ----------

def launch_video():
    """Найбільш сумісний спосіб запуску відео для Windows 10/11"""
    video_path = os.path.join(BASE_DIR, "singing.mp4")
    
    # Використовуємо 'start', щоб Windows сама відкрила файл у програмі за замовчуванням
    # (Медіапрогравач, який на скріншоті)
    try:
        os.startfile(video_path)
    except:
        # Якщо startfile не спрацював, пробуємо через shell команду
        subprocess.Popen(f'start "" "{video_path}"', shell=True)

def draw_hacked_ui():
    """Екран, що показує злам у самому вікні програми"""
    screen.fill((0, 0, 0)) # Чорний фон
    
    # Малюємо червону рамку «УВАГА»
    pygame.draw.rect(screen, (255, 0, 0), (20, 20, WIDTH-40, HEIGHT-40), 5)
    
    lines = [
        "!!! WARNING: SYSTEM COMPROMISED !!!",
        "-----------------------------------",
        "CONNECTION ESTABLISHED: PORK_SERVER",
        "ENCRYPTING FILES...",
        "",
        "YOU HAVE BEEN HACKED BY JOHN PORK",
        "",
        "PAY 1,000,000 PORK-COINS TO UNLOCK",
        "OR YOUR PC WILL BE TURNED INTO BACON",
        "-----------------------------------",
        "IP: [HIDDEN]",
        "STATUS: SPREADING VIRUS..."
    ]
    
    y = 250
    for line in lines:
        color = (255, 0, 0) if "WARNING" in line or "HACKED" in line else (0, 255, 0)
        text = font_hacker.render(line, True, color)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, y))
        y += 50
    
    pygame.display.update()

# ---------- ГОЛОВНИЙ ЦИКЛ ----------
running = True
hacked_mode = False

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not hacked_mode:
            mx, my = pygame.mouse.get_pos()
            pick_rect = pick_up.get_rect(topleft=GREEN_BTN_POS)
            
            if pick_rect.collidepoint(mx, my):
                pygame.mixer.music.stop()
                hacked_mode = True
                # Спочатку малюємо екран зламу, щоб він вже був там, коли відео відкриється
                draw_hacked_ui()
                launch_video()
            
            decline_rect = decline.get_rect(topleft=RED_BTN_POS)
            if decline_rect.collidepoint(mx, my):
                running = False

    if not hacked_mode:
        screen.blit(bg, (0, 0))
        title = font_title.render("John Pork is calling...", True, (255, 255, 255))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
        screen.blit(decline, RED_BTN_POS)
        screen.blit(pick_up, GREEN_BTN_POS)
        pygame.display.update()
    else:
        # Постійно відображаємо екран зламу
        draw_hacked_ui()

pygame.quit()
sys.exit()
