import pygame
import sys
import json
import os

# Инициализация Pygame
pygame.init()

# Настройки окна
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 100, 255)
DARK_BLUE = (50, 50, 200)
GREEN = (100, 255, 100)
DARK_GREEN = (50, 200, 50)
RED = (255, 100, 100)
DARK_RED = (200, 50, 50)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)
PURPLE = (200, 100, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 100)
PINK = (255, 192, 203)
LIGHT_BLUE = (173, 216, 230)

# Файл для сохранения настроек
SETTINGS_FILE = "settings.json"


# Загрузка настроек
def load_settings():
    # Загружает настройки из файла
    default_settings = {
        "theme_color": BLUE,  # Цвет темы по умолчанию
        "theme_color_name": "Синий",
        "saved_user": None  # Сохраненный пользователь
    }

    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Преобразуем цвет из списка в кортеж
                if "theme_color" in data:
                    data["theme_color"] = tuple(data["theme_color"])
                return data
        except:
            return default_settings
    return default_settings


def save_settings(settings):
    """Сохраняет настройки в файл"""
    settings_to_save = settings.copy()
    # Преобразуем цвет из кортежа в список для JSON
    if "theme_color" in settings_to_save:
        settings_to_save["theme_color"] = list(settings_to_save["theme_color"])
    with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(settings_to_save, f, ensure_ascii=False, indent=4)


# Загружаем настройки
settings = load_settings()
current_theme_color = settings["theme_color"]
current_theme_name = settings["theme_color_name"]
saved_user = settings.get("saved_user")  # Сохраненный пользователь

# Шрифты
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)
small_font = pygame.font.Font(None, 24)

# Файл для сохранения пользователей
USERS_FILE = "users.json"

profile_btn1 = pygame.Rect(WINDOW_WIDTH // 2 - 450, 150, 300, 50)
profile_btn2 = pygame.Rect(WINDOW_WIDTH // 2 - 450, 220, 300, 50)
profile_btn3 = pygame.Rect(WINDOW_WIDTH // 2 - 450, 290, 300, 50)
profile_btn4 = pygame.Rect(WINDOW_WIDTH // 2 - 450, 360, 300, 50)
profile_btn5 = pygame.Rect(WINDOW_WIDTH // 2 - 450, 430, 300, 50)
profile_btn6 = pygame.Rect(WINDOW_WIDTH // 2 - 450, 500, 300, 50)

profile_btn7 = pygame.Rect(WINDOW_WIDTH // 2 - 130, 150, 300, 50)
profile_btn8 = pygame.Rect(WINDOW_WIDTH // 2 -130, 220, 300, 50)
profile_btn9 = pygame.Rect(WINDOW_WIDTH // 2 - 130, 290, 300, 50)
profile_btn10 = pygame.Rect(WINDOW_WIDTH // 2 - 130, 360, 300, 50)
profile_btn11 = pygame.Rect(WINDOW_WIDTH // 2 - 130, 430, 300, 50)
profile_btn12 = pygame.Rect(WINDOW_WIDTH // 2 - 130, 500, 300, 50)

profile_btn13 = pygame.Rect(WINDOW_WIDTH // 2 + 190, 150, 300, 50)
profile_btn14 = pygame.Rect(WINDOW_WIDTH // 2 + 190, 220, 300, 50)
profile_btn15 = pygame.Rect(WINDOW_WIDTH // 2 + 190, 290, 300, 50)
profile_btn16 = pygame.Rect(WINDOW_WIDTH // 2 + 190, 360, 300, 50)
profile_btn17 = pygame.Rect(WINDOW_WIDTH // 2 + 190, 430, 300, 50)
profile_btn18 = pygame.Rect(WINDOW_WIDTH // 2 + 190, 500, 300, 50)

def load_users():
    """Загружает пользователей из файла"""
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}


def save_users(users):
    """Сохраняет пользователей в файл"""
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


# Загружаем пользователей
users = load_users()

# Загрузка иконки настроек
def load_settings_icon():
    """Загружает иконку настроек из файла"""
    icon_size = (50, 50)

    # Пытаемся загрузить иконку из файла
    if os.path.exists("settings_icon.png"):
        try:
            icon = pygame.image.load("settings_icon.png")
            icon = pygame.transform.scale(icon, icon_size)
            return icon
        except:
            pass


# Загружаем иконку
settings_icon = load_settings_icon()
settings_icon_rect = settings_icon.get_rect(topleft=(20, 20))


# ========== КНОПКИ В ГЛАВНОМ МЕНЮ ==========
login_btn_rect = pygame.Rect(WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 - 100, 300, 80)
register_btn_rect = pygame.Rect(WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 + 40, 300, 80)

# Кнопки на других экранах
back_btn_rect = pygame.Rect(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 100, 200, 50)
submit_btn_rect = pygame.Rect(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 180, 200, 50)
logout_btn_rect = pygame.Rect(WINDOW_WIDTH - 150, WINDOW_HEIGHT - 60, 120, 40)
kal = pygame.Rect(250, 100, 200, 50)

# ========== ПОЛЯ ДЛЯ ВВОДА ==========
login_rect = pygame.Rect(WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 - 70, 300, 50)
password_rect = pygame.Rect(WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 + 40, 300, 50)

# ========== КНОПКИ ВЫБОРА ЦВЕТА (2 РЯДА ПО 3 КНОПКИ + 1 ПО ЦЕНТРУ) ==========
# Размеры кнопок
btn_width = 180
btn_height = 50
btn_spacing = 20

# Первый ряд (3 кнопки)
row1_y = 200
row1_buttons = []
for i in range(3):
    btn_x = WINDOW_WIDTH // 2 - (btn_width * 1.5 + btn_spacing) + i * (btn_width + btn_spacing)
    btn_rect = pygame.Rect(btn_x, row1_y, btn_width, btn_height)
    row1_buttons.append(btn_rect)

# Второй ряд (3 кнопки)
row2_y = row1_y + btn_height + btn_spacing
row2_buttons = []
for i in range(3):
    btn_x = WINDOW_WIDTH // 2 - (btn_width * 1.5 + btn_spacing) + i * (btn_width + btn_spacing)
    btn_rect = pygame.Rect(btn_x, row2_y, btn_width, btn_height)
    row2_buttons.append(btn_rect)

# Третий ряд (1 кнопка по центру)
row3_y = row2_y + btn_height + btn_spacing
row3_btn = pygame.Rect(WINDOW_WIDTH // 2 - btn_width // 2, row3_y, btn_width, btn_height)

# Собираем все кнопки в список с цветами
color_options = [
    (BLUE, "Синий"),
    (GREEN, "Зеленый"),
    (RED, "Красный"),
    (PURPLE, "Фиолетовый"),
    (ORANGE, "Оранжевый"),
    (PINK, "Розовый"),
    (LIGHT_BLUE, "Голубой")
]

# Создаем список кнопок в порядке: 1 ряд, 2 ряд, 3 ряд
color_buttons = []
for i in range(3):
    color_buttons.append((row1_buttons[i], color_options[i][0], color_options[i][1]))
for i in range(3):
    color_buttons.append((row2_buttons[i], color_options[i + 3][0], color_options[i + 3][1]))
color_buttons.append((row3_btn, color_options[6][0], color_options[6][1]))

# Состояния кнопок
login_btn_hover = False
register_btn_hover = False
back_btn_hover = False
submit_btn_hover = False
logout_btn_hover = False
settings_icon_hover = False
kal = False
color_buttons_hover = [False] * len(color_buttons)
profile_btn_hover = [False] * 18
# Текущий экран
if saved_user and saved_user in users:
    current_screen = "profile"
    current_user = saved_user
else:
    current_screen = "menu"
    current_user = None

# Поля для ввода
login_active = False
login_text = ""

password_active = False
password_text = ""


def draw_settings_icon():
    """Рисует иконку настроек с эффектом наведения"""
    if settings_icon_hover:
        scaled_icon = pygame.transform.scale(settings_icon, (55, 55))
        icon_x = settings_icon_rect.x - 2.5
        icon_y = settings_icon_rect.y - 2.5
        WINDOW.blit(scaled_icon, (icon_x, icon_y))
        pygame.draw.circle(WINDOW, (255, 255, 200, 100),
                           (settings_icon_rect.centerx, settings_icon_rect.centery), 30, 2)
    else:
        WINDOW.blit(settings_icon, settings_icon_rect)


def draw_button(rect, text, is_hovered, normal_color, hover_color):
    """Функция для отрисовки кнопки"""
    if is_hovered:
        color = hover_color
    else:
        color = normal_color

    pygame.draw.rect(WINDOW, color, rect)
    pygame.draw.rect(WINDOW, BLACK, rect, 2)

    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=rect.center)
    WINDOW.blit(text_surface, text_rect)


def draw_input_field(rect, text, is_active, label, show_stars=False):
    """Рисует поле для ввода текста"""
    label_surface = font.render(label, True, BLACK)
    WINDOW.blit(label_surface, (rect.x, rect.y - 30))

    if is_active:
        color = current_theme_color
    else:
        color = GRAY

    pygame.draw.rect(WINDOW, color, rect)
    pygame.draw.rect(WINDOW, BLACK, rect, 2)

    if show_stars:
        display_text = "*" * len(text)
    else:
        display_text = text

    text_surface = font.render(display_text, True, BLACK)
    WINDOW.blit(text_surface, (rect.x + 10, rect.y + 10))

    if is_active and pygame.time.get_ticks() % 1000 < 500:
        cursor_x = rect.x + 10 + text_surface.get_width()
        cursor_y = rect.y + 10
        pygame.draw.line(WINDOW, BLACK, (cursor_x, cursor_y), (cursor_x, cursor_y + 30), 2)


def draw_menu():
    """Рисует главное меню"""
    WINDOW.fill(WHITE)
    title_text = big_font.render("ДОБРО ПОЖАЛОВАТЬ", True, BLACK)
    title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 150))
    WINDOW.blit(title_text, title_rect)

    draw_button(login_btn_rect, "ВХОД", login_btn_hover, current_theme_color, DARK_BLUE)
    draw_button(register_btn_rect, "РЕГИСТРАЦИЯ", register_btn_hover, current_theme_color, DARK_BLUE)

    users_count = len(users)
    info_text = small_font.render(f"Всего пользователей: {users_count}", True, BLACK)
    info_rect = info_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50))
    WINDOW.blit(info_text, info_rect)

    draw_settings_icon()


def draw_login_screen():
    """Рисует экран входа"""
    WINDOW.fill(WHITE)
    title_text = big_font.render("ВХОД", True, BLACK)
    title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 80))
    WINDOW.blit(title_text, title_rect)

    draw_input_field(login_rect, login_text, login_active, "Логин:", False)
    draw_input_field(password_rect, password_text, password_active, "Пароль:", True)

    draw_button(submit_btn_rect, "ВОЙТИ", submit_btn_hover, current_theme_color, DARK_BLUE)
    draw_button(back_btn_rect, "НАЗАД", back_btn_hover, RED, DARK_RED)

    draw_settings_icon()


def draw_register_screen():
    """Рисует экран регистрации"""
    WINDOW.fill(WHITE)
    title_text = big_font.render("РЕГИСТРАЦИЯ", True, BLACK)
    title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 80))
    WINDOW.blit(title_text, title_rect)

    draw_input_field(login_rect, login_text, login_active, "Придумайте логин:", False)
    draw_input_field(password_rect, password_text, password_active, "Придумайте пароль:", True)

    draw_button(submit_btn_rect, "ЗАРЕГИСТРИРОВАТЬСЯ", submit_btn_hover, current_theme_color, DARK_BLUE)
    draw_button(back_btn_rect, "НАЗАД", back_btn_hover, RED, DARK_RED)

    draw_settings_icon()


def draw_profile_screen():
    """Рисует экран профиля с множеством кнопок"""
    WINDOW.fill(current_theme_color)

    # Приветствие
    welcome_text = big_font.render(f"Привет, {current_user}!", True, BLACK)
    welcome_rect = welcome_text.get_rect(center=(WINDOW_WIDTH // 2, 60))
    WINDOW.blit(welcome_text, welcome_rect)

    # Кнопки профиля
    buttons = [
        (profile_btn1, "МОЯ СТАТИСТИКА", profile_btn_hover[0]),
        (profile_btn2, "КУПИТЬ ПОДПИСКУ", profile_btn_hover[1]),
        (profile_btn3, "МОИ ДОСТИЖЕНИЯ", profile_btn_hover[2]),
        (profile_btn4, "НАСТРОЙКИ ПРОФИЛЯ", profile_btn_hover[3]),
        (profile_btn5, "ПОМОЩЬ", profile_btn_hover[4]),
        (profile_btn6, "О ПРОГРАММЕ", profile_btn_hover[5]),
        (profile_btn7, "МОЯ СТАТИСТИКА", profile_btn_hover[6]),
        (profile_btn8, "КУПИТЬ ПОДПИСКУ", profile_btn_hover[7]),
        (profile_btn9, "МОИ ДОСТИЖЕНИЯ", profile_btn_hover[8]),
        (profile_btn10, "НАСТРОЙКИ ПРОФИЛЯ", profile_btn_hover[9]),
        (profile_btn11, "ПОМОЩЬ", profile_btn_hover[10]),
        (profile_btn12, "О ПРОГРАММЕ", profile_btn_hover[11]),
        (profile_btn13, "МОЯ СТАТИСТИКА", profile_btn_hover[12]),
        (profile_btn14, "КУПИТЬ ПОДПИСКУ", profile_btn_hover[13]),
        (profile_btn15, "МОИ ДОСТИЖЕНИЯ", profile_btn_hover[14]),
        (profile_btn16, "НАСТРОЙКИ ПРОФИЛЯ", profile_btn_hover[15]),
        (profile_btn17, "ПОМОЩЬ", profile_btn_hover[16]),
        (profile_btn18, "О ПРОГРАММЕ", profile_btn_hover[17]),
    ]

    for btn_rect, btn_text, is_hover in buttons:
        draw_button(btn_rect, btn_text, is_hover, current_theme_color, DARK_BLUE)

    # Кнопка выхода (внизу справа)
    draw_button(logout_btn_rect, "ВЫЙТИ", logout_btn_hover, RED, DARK_RED)

    # Иконка настроек
    draw_settings_icon()


def draw_settings_screen():
    """Рисует экран настроек для выбора цвета с кнопками в 2 ряда по 3 + 1 по центру"""
    WINDOW.fill(WHITE)

    title_text = big_font.render("НАСТРОЙКИ ЦВЕТА", True, BLACK)
    title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 80))
    WINDOW.blit(title_text, title_rect)

    current_text = font.render(f"Текущий цвет: {current_theme_name}", True, BLACK)
    current_rect = current_text.get_rect(center=(WINDOW_WIDTH // 2, 140))
    WINDOW.blit(current_text, current_rect)

    # Рисуем кнопки выбора цвета
    for i, (btn_rect, color, name) in enumerate(color_buttons):
        is_hovered = color_buttons_hover[i]

        if is_hovered:
            pygame.draw.rect(WINDOW, color, btn_rect)
        else:
            pygame.draw.rect(WINDOW, GRAY, btn_rect)
        pygame.draw.rect(WINDOW, BLACK, btn_rect, 2)

        text_surface = font.render(name, True, BLACK)
        text_rect = text_surface.get_rect(center=btn_rect.center)
        WINDOW.blit(text_surface, text_rect)

        # Отметка, если цвет выбран
        if color == current_theme_color:
            pygame.draw.circle(WINDOW, GREEN, (btn_rect.right - 25, btn_rect.centery), 10)
            pygame.draw.circle(WINDOW, BLACK, (btn_rect.right - 25, btn_rect.centery), 10, 2)

    # Кнопка назад
    back_btn_rect_settings = pygame.Rect(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 100, 200, 50)
    draw_button(back_btn_rect_settings, "НАЗАД", back_btn_hover, RED, DARK_RED)

    draw_settings_icon()

    return back_btn_rect_settings


def show_message(msg, is_error=True):
    """Показывает сообщение на экране"""
    if is_error:
        color = RED
    else:
        color = GREEN

    text_surface = font.render(msg, True, color)
    text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50))

    pygame.draw.rect(WINDOW, WHITE, (text_rect.x - 10, text_rect.y - 5,
                                     text_rect.width + 20, text_rect.height + 10))
    pygame.draw.rect(WINDOW, color, (text_rect.x - 10, text_rect.y - 5,
                                     text_rect.width + 20, text_rect.height + 10), 2)
    WINDOW.blit(text_surface, text_rect)
    pygame.display.flip()
    pygame.time.wait(1500)


# Главный игровой цикл
clock = pygame.time.Clock()
running = True

while running:
    mouse_pos = pygame.mouse.get_pos()

    # Обновление состояния наведения для иконки настроек
    settings_icon_hover = settings_icon_rect.collidepoint(mouse_pos)

    # Обновление состояний наведения в зависимости от экрана
    if current_screen == "menu":
        login_btn_hover = login_btn_rect.collidepoint(mouse_pos)
        register_btn_hover = register_btn_rect.collidepoint(mouse_pos)
        back_btn_hover = False
        submit_btn_hover = False
        logout_btn_hover = False

    elif current_screen == "login":
        login_btn_hover = False
        register_btn_hover = False
        back_btn_hover = back_btn_rect.collidepoint(mouse_pos)
        submit_btn_hover = submit_btn_rect.collidepoint(mouse_pos)
        logout_btn_hover = False

        if login_active or password_active:
            submit_btn_hover = False
            back_btn_hover = False

    elif current_screen == "register":
        login_btn_hover = False
        register_btn_hover = False
        back_btn_hover = back_btn_rect.collidepoint(mouse_pos)
        submit_btn_hover = submit_btn_rect.collidepoint(mouse_pos)
        logout_btn_hover = False

        if login_active or password_active:
            submit_btn_hover = False
            back_btn_hover = False

    elif current_screen == "profile":
        login_btn_hover = False
        register_btn_hover = False
        back_btn_hover = False
        submit_btn_hover = False
        logout_btn_hover = logout_btn_rect.collidepoint(mouse_pos)

    elif current_screen == "settings":
        login_btn_hover = False
        register_btn_hover = False
        back_btn_hover = False
        submit_btn_hover = False
        logout_btn_hover = False

        # Обновляем наведение для кнопок цвета
        for i, (btn_rect, _, _) in enumerate(color_buttons):
            color_buttons_hover[i] = btn_rect.collidepoint(mouse_pos)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if current_user:
                settings["saved_user"] = current_user
                save_settings(settings)
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if settings_icon_rect.collidepoint(event.pos):
                    current_screen = "settings"

                elif current_screen == "menu":
                    if login_btn_rect.collidepoint(event.pos):
                        login_text = ""
                        password_text = ""
                        login_active = False
                        password_active = False
                        current_screen = "login"

                    elif register_btn_rect.collidepoint(event.pos):
                        login_text = ""
                        password_text = ""
                        login_active = False
                        password_active = False
                        current_screen = "register"

                elif current_screen == "settings":
                    # Проверяем клик по кнопкам цвета
                    for i, (btn_rect, color, name) in enumerate(color_buttons):
                        if btn_rect.collidepoint(event.pos):
                            current_theme_color = color
                            current_theme_name = name
                            settings["theme_color"] = current_theme_color
                            settings["theme_color_name"] = current_theme_name
                            if current_user:
                                settings["saved_user"] = current_user
                            save_settings(settings)
                            show_message(f"Цвет изменен на {name}!", False)
                            if current_user:
                                current_screen = "profile"
                            else:
                                current_screen = "menu"
                            break

                    # Проверяем клик по кнопке назад
                    back_btn_rect_settings = pygame.Rect(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 100, 200, 50)
                    if back_btn_rect_settings.collidepoint(event.pos):
                        if current_user:
                            current_screen = "profile"
                        else:
                            current_screen = "menu"

                elif current_screen in ["login", "register"]:
                    login_active = login_rect.collidepoint(event.pos)
                    password_active = password_rect.collidepoint(event.pos)

                    if current_screen == "login":
                        if submit_btn_rect.collidepoint(event.pos) and not (login_active or password_active):
                            if login_text and password_text:
                                if login_text in users and users[login_text] == password_text:
                                    current_user = login_text
                                    settings["saved_user"] = current_user
                                    save_settings(settings)
                                    show_message(f"Добро пожаловать, {login_text}!", False)
                                    login_text = ""
                                    password_text = ""
                                    current_screen = "profile"
                                else:
                                    show_message("Неверный логин или пароль!", True)
                            else:
                                show_message("Заполните все поля!", True)

                        elif back_btn_rect.collidepoint(event.pos) and not (login_active or password_active):
                            login_text = ""
                            password_text = ""
                            current_screen = "menu"

                    elif current_screen == "register":
                        if submit_btn_rect.collidepoint(event.pos) and not (login_active or password_active):
                            if login_text and password_text:
                                if login_text in users:
                                    show_message("Пользователь уже существует!", True)
                                elif len(login_text) < 3:
                                    show_message("Логин должен содержать минимум 3 символа!", True)
                                elif len(password_text) < 4:
                                    show_message("Пароль должен содержать минимум 4 символа!", True)
                                else:
                                    users[login_text] = password_text
                                    save_users(users)
                                    current_user = login_text
                                    settings["saved_user"] = current_user
                                    save_settings(settings)
                                    show_message(f"Пользователь {login_text} зарегистрирован!", False)
                                    login_text = ""
                                    password_text = ""
                                    current_screen = "profile"
                            else:
                                show_message("Заполните все поля!", True)

                        elif back_btn_rect.collidepoint(event.pos) and not (login_active or password_active):
                            login_text = ""
                            password_text = ""
                            current_screen = "menu"

                elif current_screen == "profile":
                    if logout_btn_rect.collidepoint(event.pos):
                        current_user = None
                        settings["saved_user"] = None
                        save_settings(settings)
                        current_screen = "menu"

                        # Обновляем наведение для всех кнопок профиля
                        profile_btn_hover[0] = profile_btn1.collidepoint(mouse_pos)
                        profile_btn_hover[1] = profile_btn2.collidepoint(mouse_pos)
                        profile_btn_hover[2] = profile_btn3.collidepoint(mouse_pos)
                        profile_btn_hover[3] = profile_btn4.collidepoint(mouse_pos)
                        profile_btn_hover[4] = profile_btn5.collidepoint(mouse_pos)
                        profile_btn_hover[5] = profile_btn6.collidepoint(mouse_pos)

        if event.type == pygame.KEYDOWN and current_screen in ["login", "register"]:
            if event.key == pygame.K_RETURN:
                login_active = False
                password_active = False

                if current_screen == "login":
                    if login_text and password_text:
                        if login_text in users and users[login_text] == password_text:
                            current_user = login_text
                            settings["saved_user"] = current_user
                            save_settings(settings)
                            show_message(f"Добро пожаловать, {login_text}!", False)
                            login_text = ""
                            password_text = ""
                            current_screen = "profile"
                        else:
                            show_message("Неверный логин или пароль!", True)
                    else:
                        show_message("Заполните все поля!", True)

                elif current_screen == "register":
                    if login_text and password_text:
                        if login_text in users:
                            show_message("Пользователь уже существует!", True)
                        elif len(login_text) < 3:
                            show_message("Логин должен содержать минимум 3 символа!", True)
                        elif len(password_text) < 4:
                            show_message("Пароль должен содержать минимум 4 символа!", True)
                        else:
                            users[login_text] = password_text
                            save_users(users)
                            current_user = login_text
                            settings["saved_user"] = current_user
                            save_settings(settings)
                            show_message(f"Пользователь {login_text} зарегистрирован!", False)
                            login_text = ""
                            password_text = ""
                            current_screen = "profile"
                    else:
                        show_message("Заполните все поля!", True)

            elif event.key == pygame.K_TAB:
                if login_active:
                    login_active = False
                    password_active = True
                elif password_active:
                    password_active = False
                    login_active = True

            elif login_active:
                if event.key == pygame.K_BACKSPACE:
                    login_text = login_text[:-1]
                else:
                    if len(login_text) < 20 and event.unicode.isprintable():
                        login_text += event.unicode

            elif password_active:
                if event.key == pygame.K_BACKSPACE:
                    password_text = password_text[:-1]
                else:
                    if len(password_text) < 20 and event.unicode.isprintable():
                        password_text += event.unicode

    if current_screen == "menu":
        draw_menu()
    elif current_screen == "login":
        draw_login_screen()
    elif current_screen == "register":
        draw_register_screen()
    elif current_screen == "profile":
        draw_profile_screen()
    elif current_screen == "settings":
        draw_settings_screen()


    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()
