import pygame  # Импорт библиотеки для создания игр и графических приложений
import sys  # Импорт для работы с системными функциями (например, выход из программы)
import json  # Импорт для работы с JSON-файлами (хранение данных)
import os  # Импорт для работы с операционной системой (проверка существования файлов)

# ========== ИНИЦИАЛИЗАЦИЯ PYGAME ==========
pygame.init()  # Запуск всех модулей Pygame (обязательная команда)

# ========== НАСТРОЙКИ ОКНА ==========
WINDOW_WIDTH = 1000  # Ширина окна приложения в пикселях
WINDOW_HEIGHT = 800  # Высота окна приложения в пикселях
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Создание окна с заданными размерами
pygame.display.set_caption("Калькулятор")  # Установка заголовка окна (пустая строка = без названия)

# ========== ОПРЕДЕЛЕНИЕ ЦВЕТОВ В ФОРМАТЕ RGB ==========
WHITE = (255, 255, 255)  # Белый цвет (максимум красного, зеленого, синего)
BLACK = (0, 0, 0)  # Черный цвет (отсутствие всех цветов)
BLUE = (100, 100, 255)  # Голубовато-синий цвет
DARK_BLUE = (50, 50, 200)  # Темно-синий цвет (для эффекта наведения)
GREEN = (100, 255, 100)  # Светло-зеленый цвет
DARK_GREEN = (50, 200, 50)  # Темно-зеленый цвет
RED = (255, 100, 100)  # Светло-красный цвет
DARK_RED = (200, 50, 50)  # Темно-красный цвет
GRAY = (200, 200, 200)  # Светло-серый цвет
DARK_GRAY = (150, 150, 150)  # Темно-серый цвет
PURPLE = (200, 100, 255)  # Фиолетовый цвет
ORANGE = (255, 165, 0)  # Оранжевый цвет
YELLOW = (255, 255, 100)  # Желтый цвет
PINK = (255, 192, 203)  # Розовый цвет
LIGHT_BLUE = (173, 216, 230)  # Голубой цвет

# ========== НАСТРОЙКИ ФАЙЛОВ ==========
SETTINGS_FILE = "settings.json"  # Имя файла для сохранения настроек приложения


# ========== ФУНКЦИЯ ЗАГРУЗКИ НАСТРОЕК ==========
def load_settings():
    """Загружает настройки из файла settings.json"""
    default_settings = {  # Настройки по умолчанию (если файла нет)
        "theme_color": BLUE,  # Цвет темы по умолчанию - синий
        "theme_color_name": "Синий",  # Название цвета для отображения
        "saved_user": None  # Сохраненный пользователь (автовход)
    }

    if os.path.exists(SETTINGS_FILE):  # Проверяем, существует ли файл с настройками
        try:  # Пытаемся прочитать файл
            with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:  # Открываем файл для чтения
                data = json.load(f)  # Загружаем данные из JSON
                if "theme_color" in data:  # Если в файле есть цвет темы
                    data["theme_color"] = tuple(data["theme_color"])  # Преобразуем список в кортеж (для Pygame)
                return data  # Возвращаем загруженные настройки
        except:  # Если произошла ошибка при чтении
            return default_settings  # Возвращаем настройки по умолчанию
    return default_settings  # Если файла нет, возвращаем настройки по умолчанию


# ========== ФУНКЦИЯ СОХРАНЕНИЯ НАСТРОЕК ==========
def save_settings(settings):
    """Сохраняет настройки в файл settings.json"""
    settings_to_save = settings.copy()  # Создаем копию настроек (чтобы не изменять оригинал)
    if "theme_color" in settings_to_save:  # Если в настройках есть цвет
        settings_to_save["theme_color"] = list(
            settings_to_save["theme_color"])  # Преобразуем кортеж в список (JSON не любит кортежи)
    with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:  # Открываем файл для записи
        json.dump(settings_to_save, f, ensure_ascii=False, indent=4)  # Сохраняем настройки в формате JSON


# ========== ЗАГРУЗКА НАСТРОЕК ПРИ ЗАПУСКЕ ==========
settings = load_settings()  # Загружаем настройки из файла
current_theme_color = settings["theme_color"]  # Текущий цвет темы
current_theme_name = settings["theme_color_name"]  # Название текущего цвета
saved_user = settings.get("saved_user")  # Сохраненный пользователь (или None)

# ========== НАСТРОЙКА ШРИФТОВ ==========
font = pygame.font.Font(None, 36)  # Основной шрифт размером 36 пикселей
big_font = pygame.font.Font(None, 72)  # Большой шрифт размером 72 пикселя
small_font = pygame.font.Font(None, 24)  # Маленький шрифт размером 24 пикселя

# ========== ФАЙЛ ДЛЯ ХРАНЕНИЯ ПОЛЬЗОВАТЕЛЕЙ ==========
USERS_FILE = "users.json"  # Имя файла для хранения данных пользователей

# ========== КНОПКИ НА ЭКРАНЕ ПРОФИЛЯ (18 кнопок) ==========
# Первый столбец (кнопки 1-6)
profile_btn1 = pygame.Rect(WINDOW_WIDTH // 2 - 450, 150, 300, 50)  # Кнопка "Калькулятор"
profile_btn2 = pygame.Rect(WINDOW_WIDTH // 2 - 450, 220, 300, 50)  # Кнопка "Перевод из двоичной"
profile_btn3 = pygame.Rect(WINDOW_WIDTH // 2 - 450, 290, 300, 50)  # Кнопка "Мои достижения"
profile_btn4 = pygame.Rect(WINDOW_WIDTH // 2 - 450, 360, 300, 50)  # Кнопка "Настройки профиля"
profile_btn5 = pygame.Rect(WINDOW_WIDTH // 2 - 450, 430, 300, 50)  # Кнопка "Помощь"
profile_btn6 = pygame.Rect(WINDOW_WIDTH // 2 - 450, 500, 300, 50)  # Кнопка "О программе"

# Второй столбец (кнопки 7-12)
profile_btn7 = pygame.Rect(WINDOW_WIDTH // 2 - 130, 150, 620, 50)  # "Моя статистика"
profile_btn8 = pygame.Rect(WINDOW_WIDTH // 2 - 130, 220, 620, 50)  # "Купить подписку"
profile_btn9 = pygame.Rect(WINDOW_WIDTH // 2 - 130, 290, 300, 50)  # "Мои достижения" (дубль)
profile_btn10 = pygame.Rect(WINDOW_WIDTH // 2 - 130, 360, 300, 50)  # "Настройки профиля" (дубль)
profile_btn11 = pygame.Rect(WINDOW_WIDTH // 2 - 130, 430, 300, 50)  # "Помощь" (дубль)
profile_btn12 = pygame.Rect(WINDOW_WIDTH // 2 - 130, 500, 300, 50)  # "О программе" (дубль)

# Третий столбец (кнопки 13-18)
profile_btn14 = pygame.Rect(WINDOW_WIDTH // 2 + 190, 220, 300, 50)  # "Купить подписку" (дубль)
profile_btn15 = pygame.Rect(WINDOW_WIDTH // 2 + 190, 290, 300, 50)  # "Мои достижения" (дубль)
profile_btn16 = pygame.Rect(WINDOW_WIDTH // 2 + 190, 360, 300, 50)  # "Настройки профиля" (дубль)
profile_btn17 = pygame.Rect(WINDOW_WIDTH // 2 + 190, 430, 300, 50)  # "Помощь" (дубль)
profile_btn18 = pygame.Rect(WINDOW_WIDTH // 2 + 190, 500, 300, 50)  # "О программе" (дубль)


# ========== ФУНКЦИИ ДЛЯ РАБОТЫ С ПОЛЬЗОВАТЕЛЯМИ ==========
def load_users():
    """Загружает список пользователей из файла users.json"""
    if os.path.exists(USERS_FILE):  # Проверяем существование файла
        try:  # Пытаемся прочитать
            with open(USERS_FILE, 'r', encoding='utf-8') as f:  # Открываем файл
                return json.load(f)  # Возвращаем словарь пользователей
        except:  # Если ошибка
            return {}  # Возвращаем пустой словарь
    return {}  # Если файла нет, возвращаем пустой словарь


def save_users(users):
    """Сохраняет список пользователей в файл users.json"""
    with open(USERS_FILE, 'w', encoding='utf-8') as f:  # Открываем файл для записи
        json.dump(users, f, ensure_ascii=False, indent=4)  # Сохраняем в JSON


# ========== ЗАГРУЗКА ПОЛЬЗОВАТЕЛЕЙ ==========
users = load_users()  # Загружаем всех зарегистрированных пользователей


# ========== ЗАГРУЗКА ИКОНКИ НАСТРОЕК ==========
def load_settings_icon():
    """Загружает иконку настроек из файла settings_icon.png"""
    icon_size = (50, 50)  # Размер иконки 50x50 пикселей
    if os.path.exists("settings_icon.png"):  # Проверяем, существует ли файл иконки
        try:  # Пытаемся загрузить
            icon = pygame.image.load("settings_icon.png")  # Загружаем изображение
            icon = pygame.transform.scale(icon, icon_size)  # Изменяем размер до 50x50
            return icon  # Возвращаем иконку
        except:  # Если ошибка
            pass  # Игнорируем (иконки не будет)
    return None  # Если иконки нет, возвращаем None


# Загружаем иконку
settings_icon = load_settings_icon()  # Загружаем иконку настроек
settings_icon_rect = settings_icon.get_rect(topleft=(20, 20))  # Прямоугольник для позиционирования (верхний левый угол)

# ========== КНОПКИ В ГЛАВНОМ МЕНЮ ==========
login_btn_rect = pygame.Rect(WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 - 100, 300, 80)  # Кнопка "Вход"
register_btn_rect = pygame.Rect(WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 + 40, 300, 80)  # Кнопка "Регистрация"

# ========== ОБЩИЕ КНОПКИ ДЛЯ РАЗНЫХ ЭКРАНОВ ==========
back_btn_rect = pygame.Rect(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 100, 200, 50)  # Кнопка "Назад"
submit_btn_rect = pygame.Rect(WINDOW_WIDTH // 2 - 170, WINDOW_HEIGHT - 180, 350, 50)  # Кнопка подтверждения
logout_btn_rect = pygame.Rect(WINDOW_WIDTH - 150, WINDOW_HEIGHT - 60, 120, 40)  # Кнопка "Выйти"

# ========== ПОЛЯ ДЛЯ ВВОДА ЛОГИНА И ПАРОЛЯ ==========
login_rect = pygame.Rect(WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 - 70, 300, 50)  # Поле для логина
password_rect = pygame.Rect(WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 + 40, 300, 50)  # Поле для пароля

# ========== НАСТРОЙКА КНОПОК ВЫБОРА ЦВЕТА ==========
btn_width = 180  # Ширина каждой кнопки цвета
btn_height = 50  # Высота каждой кнопки цвета
btn_spacing = 20  # Расстояние между кнопками

# Первый ряд кнопок (3 кнопки)
row1_y = 200  # Y-координата первого ряда
row1_buttons = []  # Список для хранения кнопок первого ряда
for i in range(3):  # Создаем 3 кнопки
    btn_x = WINDOW_WIDTH // 2 - (btn_width * 1.5 + btn_spacing) + i * (btn_width + btn_spacing)  # Расчет X координаты
    btn_rect = pygame.Rect(btn_x, row1_y, btn_width, btn_height)  # Создаем прямоугольник кнопки
    row1_buttons.append(btn_rect)  # Добавляем в список

# Второй ряд кнопок (3 кнопки)
row2_y = row1_y + btn_height + btn_spacing  # Y-координата второго ряда (ниже первого)
row2_buttons = []  # Список для хранения кнопок второго ряда
for i in range(3):  # Создаем 3 кнопки
    btn_x = WINDOW_WIDTH // 2 - (btn_width * 1.5 + btn_spacing) + i * (btn_width + btn_spacing)  # Расчет X
    btn_rect = pygame.Rect(btn_x, row2_y, btn_width, btn_height)  # Создаем прямоугольник
    row2_buttons.append(btn_rect)  # Добавляем в список

# Третий ряд (1 кнопка по центру)
row3_y = row2_y + btn_height + btn_spacing  # Y-координата третьего ряда
row3_btn = pygame.Rect(WINDOW_WIDTH // 2 - btn_width // 2, row3_y, btn_width, btn_height)  # Кнопка по центру

# Список доступных цветов с названиями
color_options = [
    (BLUE, "Синий"),  # Синий цвет
    (GREEN, "Зеленый"),  # Зеленый цвет
    (RED, "Красный"),  # Красный цвет
    (PURPLE, "Фиолетовый"),  # Фиолетовый
    (ORANGE, "Оранжевый"),  # Оранжевый
    (PINK, "Розовый"),  # Розовый
    (LIGHT_BLUE, "Голубой")  # Голубой
]

# Собираем все кнопки в один список для удобства
color_buttons = []  # Каждый элемент: (прямоугольник, цвет, название)
for i in range(3):  # Первый ряд (первые 3 цвета)
    color_buttons.append((row1_buttons[i], color_options[i][0], color_options[i][1]))
for i in range(3):  # Второй ряд (следующие 3 цвета)
    color_buttons.append((row2_buttons[i], color_options[i + 3][0], color_options[i + 3][1]))
color_buttons.append((row3_btn, color_options[6][0], color_options[6][1]))  # Третий ряд (7-й цвет)

# ========== СОСТОЯНИЯ КНОПОК ==========
login_btn_hover = False  # Состояние наведения на кнопку "Вход"
register_btn_hover = False  # Состояние наведения на кнопку "Регистрация"
back_btn_hover = False  # Состояние наведения на кнопку "Назад"
submit_btn_hover = False  # Состояние наведения на кнопку подтверждения
logout_btn_hover = False  # Состояние наведения на кнопку "Выйти"
settings_icon_hover = False  # Состояние наведения на иконку настроек
kal = False  # (Не используется)
color_buttons_hover = [False] * len(color_buttons)  # Список состояний наведения для кнопок цвета
profile_btn_hover = [False] * 18  # Список состояний для 18 кнопок профиля

# ========== ТЕКУЩИЙ ЭКРАН И ПОЛЬЗОВАТЕЛЬ ==========
# Определяем, какой экран показывать при запуске
if saved_user and saved_user in users:  # Если есть сохраненный пользователь и он существует
    current_screen = "profile"  # Сразу показываем профиль
    current_user = saved_user  # Устанавливаем текущего пользователя
else:  # Если нет сохраненного пользователя
    current_screen = "menu"  # Показываем главное меню
    current_user = None  # Пользователь не авторизован

# ========== СОСТОЯНИЯ ПОЛЕЙ ВВОДА ==========
login_active = False  # Активно ли поле ввода логина (для курсора)
login_text = ""  # Текст, введенный в поле логина

password_active = False  # Активно ли поле ввода пароля
password_text = ""  # Текст, введенный в поле пароля


# ========== ФУНКЦИЯ ОТРИСОВКИ ИКОНКИ НАСТРОЕК ==========
def draw_settings_icon():
    """Рисует иконку настроек с эффектом увеличения при наведении"""
    if settings_icon_hover:  # Если мышь наведена на иконку
        scaled_icon = pygame.transform.scale(settings_icon, (55, 55))  # Увеличиваем иконку до 55x55
        icon_x = settings_icon_rect.x - 2.5  # Смещаем по X для центрирования
        icon_y = settings_icon_rect.y - 2.5  # Смещаем по Y для центрирования
        WINDOW.blit(scaled_icon, (icon_x, icon_y))  # Рисуем увеличенную иконку
        # Рисуем подсветку (круг вокруг иконки)
        pygame.draw.circle(WINDOW, (255, 255, 200, 100),
                           (settings_icon_rect.centerx, settings_icon_rect.centery), 30, 2)
    else:  # Если мышь не наведена
        WINDOW.blit(settings_icon, settings_icon_rect)  # Рисуем обычную иконку


# ========== ФУНКЦИЯ ОТРИСОВКИ КНОПКИ ==========
def draw_button(rect, text, is_hovered, normal_color, hover_color):
    """Универсальная функция для рисования кнопки"""
    if is_hovered:  # Если мышь наведена
        color = hover_color  # Используем цвет наведения
    else:  # Если не наведена
        color = normal_color  # Используем обычный цвет

    pygame.draw.rect(WINDOW, color, rect)  # Рисуем заливку кнопки
    pygame.draw.rect(WINDOW, BLACK, rect, 2)  # Рисуем черную рамку толщиной 2 пикселя

    text_surface = font.render(text, True, BLACK)  # Создаем текст черного цвета
    text_rect = text_surface.get_rect(center=rect.center)  # Центрируем текст на кнопке
    WINDOW.blit(text_surface, text_rect)  # Рисуем текст


# ========== ФУНКЦИЯ ОТРИСОВКИ ПОЛЯ ВВОДА ==========
def draw_input_field(rect, text, is_active, label, show_stars=False):
    """Рисует поле для ввода текста с меткой и курсором"""
    label_surface = font.render(label, True, BLACK)  # Создаем текст метки
    WINDOW.blit(label_surface, (rect.x, rect.y - 30))  # Рисуем метку над полем

    if is_active:  # Если поле активно (пользователь вводит)
        color = current_theme_color  # Подсвечиваем цветом темы
    else:  # Если не активно
        color = GRAY  # Серый цвет

    pygame.draw.rect(WINDOW, color, rect)  # Рисуем фон поля
    pygame.draw.rect(WINDOW, BLACK, rect, 2)  # Рисуем рамку

    if show_stars:  # Если нужно скрыть пароль (показывать звездочки)
        display_text = "*" * len(text)  # Заменяем каждый символ на звездочку
    else:  # Если обычный текст
        display_text = text  # Показываем как есть

    text_surface = font.render(display_text, True, BLACK)  # Создаем текст
    WINDOW.blit(text_surface, (rect.x + 10, rect.y + 10))  # Рисуем с отступом 10 пикселей

    # Рисуем мигающий курсор
    if is_active and pygame.time.get_ticks() % 1000 < 500:  # Мигает каждые 500 мс
        cursor_x = rect.x + 10 + text_surface.get_width()  # X позиция курсора (после текста)
        cursor_y = rect.y + 10  # Y позиция курсора
        pygame.draw.line(WINDOW, BLACK, (cursor_x, cursor_y), (cursor_x, cursor_y + 30), 2)  # Рисуем вертикальную линию


# ========== ЭКРАН ГЛАВНОГО МЕНЮ ==========
def draw_menu():
    """Рисует главное меню с кнопками входа и регистрации"""
    WINDOW.fill(WHITE)  # Заливаем фон белым цветом
    title_text = big_font.render("ДОБРО ПОЖАЛОВАТЬ", True, BLACK)  # Заголовок
    title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 150))  # Центрируем заголовок
    WINDOW.blit(title_text, title_rect)  # Рисуем заголовок

    # Рисуем кнопки входа и регистрации
    draw_button(login_btn_rect, "ВХОД", login_btn_hover, current_theme_color, DARK_BLUE)
    draw_button(register_btn_rect, "РЕГИСТРАЦИЯ", register_btn_hover, current_theme_color, DARK_BLUE)

    users_count = len(users)  # Количество зарегистрированных пользователей
    info_text = small_font.render(f"Всего пользователей: {users_count}", True, BLACK)  # Текст статистики
    info_rect = info_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50))  # Внизу экрана
    WINDOW.blit(info_text, info_rect)  # Рисуем статистику

    draw_settings_icon()  # Рисуем иконку настроек


# ========== ЭКРАН ВХОДА ==========
def draw_login_screen():
    """Рисует экран входа с полями логина и пароля"""
    WINDOW.fill(WHITE)  # Белый фон
    title_text = big_font.render("ВХОД", True, BLACK)  # Заголовок
    title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 80))  # Центрируем
    WINDOW.blit(title_text, title_rect)  # Рисуем заголовок

    # Поля ввода
    draw_input_field(login_rect, login_text, login_active, "Логин:", False)
    draw_input_field(password_rect, password_text, password_active, "Пароль:", True)

    # Кнопки
    draw_button(submit_btn_rect, "ВОЙТИ", submit_btn_hover, current_theme_color, DARK_BLUE)
    draw_button(back_btn_rect, "НАЗАД", back_btn_hover, RED, DARK_RED)

    draw_settings_icon()  # Иконка настроек


# ========== ЭКРАН РЕГИСТРАЦИИ ==========
def draw_register_screen():
    """Рисует экран регистрации нового пользователя"""
    WINDOW.fill(WHITE)  # Белый фон
    title_text = big_font.render("РЕГИСТРАЦИЯ", True, BLACK)  # Заголовок
    title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 80))
    WINDOW.blit(title_text, title_rect)

    # Поля ввода (с подсказками)
    draw_input_field(login_rect, login_text, login_active, "Придумайте логин:", False)
    draw_input_field(password_rect, password_text, password_active, "Придумайте пароль:", True)

    # Кнопки
    draw_button(submit_btn_rect, "ЗАРЕГИСТРИРОВАТЬСЯ", submit_btn_hover, current_theme_color, DARK_BLUE)
    draw_button(back_btn_rect, "НАЗАД", back_btn_hover, RED, DARK_RED)

    draw_settings_icon()


# ========== ЭКРАН ПРОФИЛЯ ==========
def draw_profile_screen():
    """Рисует экран профиля пользователя с 18 кнопками"""
    WINDOW.fill(current_theme_color)  # Заливаем фон цветом темы

    # Приветствие пользователя
    welcome_text = big_font.render(f"Приветствую, {current_user}", True, BLACK)
    welcome_rect = welcome_text.get_rect(center=(WINDOW_WIDTH // 2, 60))
    WINDOW.blit(welcome_text, welcome_rect)

    # Список всех кнопок профиля с их текстом
    buttons = [
        (profile_btn1, "Калькулятор", profile_btn_hover[0]),
        # (profile_btn2, "", profile_btn_hover[1]),
        # (profile_btn3, "", profile_btn_hover[2]),
        # (profile_btn4, "", profile_btn_hover[3]),
        # (profile_btn5, "", profile_btn_hover[4]),
        # (profile_btn6, "", profile_btn_hover[5]),
        (profile_btn7, "Перевод из двоичной в десятичную", profile_btn_hover[6]),
        (profile_btn8, "Перевод из десятичной в двоичную", profile_btn_hover[7]),
        # (profile_btn9, "", profile_btn_hover[8]),
        # (profile_btn10, "", profile_btn_hover[9]),
        # (profile_btn11, "", profile_btn_hover[10]),
        # (profile_btn12, "", profile_btn_hover[11]),
        # (profile_btn15, "", profile_btn_hover[14]),
        # (profile_btn16, "", profile_btn_hover[15]),
        # (profile_btn17, "", profile_btn_hover[16]),
        # (profile_btn18, "", profile_btn_hover[17]),
    ]

    # Рисуем каждую кнопку
    for btn_rect, btn_text, is_hover in buttons:
        draw_button(btn_rect, btn_text, is_hover, current_theme_color, DARK_BLUE)

    # Кнопка выхода (внизу справа)
    draw_button(logout_btn_rect, "ВЫЙТИ", logout_btn_hover, RED, DARK_RED)

    draw_settings_icon()  # Иконка настроек


# ========== ЭКРАН НАСТРОЕК ЦВЕТА ==========
def draw_settings_screen():
    """Рисует экран выбора цвета темы (7 цветов в 3 ряда)"""
    WINDOW.fill(WHITE)  # Белый фон

    title_text = big_font.render("НАСТРОЙКИ ЦВЕТА", True, BLACK)
    title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 80))
    WINDOW.blit(title_text, title_rect)

    current_text = font.render(f"Текущий цвет: {current_theme_name}", True, BLACK)
    current_rect = current_text.get_rect(center=(WINDOW_WIDTH // 2, 140))
    WINDOW.blit(current_text, current_rect)

    # Рисуем кнопки выбора цвета
    for i, (btn_rect, color, name) in enumerate(color_buttons):
        is_hovered = color_buttons_hover[i]  # Проверяем наведение

        if is_hovered:  # При наведении показываем цвет кнопки
            pygame.draw.rect(WINDOW, color, btn_rect)
        else:  # Иначе серый цвет
            pygame.draw.rect(WINDOW, GRAY, btn_rect)
        pygame.draw.rect(WINDOW, BLACK, btn_rect, 2)  # Рамка

        text_surface = font.render(name, True, BLACK)  # Название цвета
        text_rect = text_surface.get_rect(center=btn_rect.center)
        WINDOW.blit(text_surface, text_rect)

        # Отметка (зеленый кружок), если этот цвет выбран
        if color == current_theme_color:
            pygame.draw.circle(WINDOW, GREEN, (btn_rect.right - 25, btn_rect.centery), 10)
            pygame.draw.circle(WINDOW, BLACK, (btn_rect.right - 25, btn_rect.centery), 10, 2)

    # Кнопка назад
    back_btn_rect_settings = pygame.Rect(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 100, 200, 50)
    draw_button(back_btn_rect_settings, "НАЗАД", back_btn_hover, RED, DARK_RED)

    draw_settings_icon()  # Иконка настроек

    return back_btn_rect_settings  # Возвращаем прямоугольник кнопки для обработки кликов


# ========== ФУНКЦИЯ ПОКАЗА СООБЩЕНИЙ ==========
def show_message(msg, is_error=True):
    """Показывает всплывающее сообщение на 1.5 секунды"""
    if is_error:  # Если сообщение об ошибке
        color = RED  # Красный цвет
    else:  # Если успех
        color = GREEN  # Зеленый цвет

    text_surface = font.render(msg, True, color)  # Создаем текст
    text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50))  # Внизу экрана

    # Рисуем фон сообщения
    pygame.draw.rect(WINDOW, WHITE, (text_rect.x - 10, text_rect.y - 5,
                                     text_rect.width + 20, text_rect.height + 10))
    pygame.draw.rect(WINDOW, color, (text_rect.x - 10, text_rect.y - 5,
                                     text_rect.width + 20, text_rect.height + 10), 2)  # Рамка
    WINDOW.blit(text_surface, text_rect)  # Рисуем текст
    pygame.display.flip()  # Обновляем экран
    pygame.time.wait(1500)  # Ждем 1.5 секунды


def a1():
    """Экран калькулятора с отдельным игровым циклом"""
    expression = ""
    result = ""

    btn_width = 200
    btn_height = 80
    start_x = 60
    start_y = 180

    calc_buttons = [
        ('7', start_x, start_y), ('8', start_x + btn_width + 10, start_y),
        ('9', start_x + (btn_width + 10) * 2, start_y), ('/', start_x + (btn_width + 10) * 3, start_y),
        ('4', start_x, start_y + btn_height + 10), ('5', start_x + btn_width + 10, start_y + btn_height + 10),
        ('6', start_x + (btn_width + 10) * 2, start_y + btn_height + 10),
        ('*', start_x + (btn_width + 10) * 3, start_y + btn_height + 10),
        ('1', start_x, start_y + (btn_height + 10) * 2),
        ('2', start_x + btn_width + 10, start_y + (btn_height + 10) * 2),
        ('3', start_x + (btn_width + 10) * 2, start_y + (btn_height + 10) * 2),
        ('-', start_x + (btn_width + 10) * 3, start_y + (btn_height + 10) * 2),
        ('0', start_x, start_y + (btn_height + 10) * 3),
        ('.', start_x + btn_width + 10, start_y + (btn_height + 10) * 3),
        ('=', start_x + (btn_width + 10) * 2, start_y + (btn_height + 10) * 3),
        ('+', start_x + (btn_width + 10) * 3, start_y + (btn_height + 10) * 3),
        ('C', start_x, start_y + (btn_height + 10) * 4),
        ('<-', start_x + btn_width + 10, start_y + (btn_height + 10) * 4),
        ('(', start_x + (btn_width + 10) * 2, start_y + (btn_height + 10) * 4),
        (')', start_x + (btn_width + 10) * 3, start_y + (btn_height + 10) * 4)
    ]

    def draw_calc_buttons():
        # Определяем контрастный цвет для текста кнопок
        if sum(current_theme_color) < 382:
            btn_text_color = WHITE
        else:
            btn_text_color = BLACK

        for btn in calc_buttons:
            text, x, y = btn
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if x < mouse_x < x + btn_width and y < mouse_y < y + btn_height:
                color = DARK_BLUE
            else:
                color = current_theme_color
            pygame.draw.rect(WINDOW, color, (x, y, btn_width, btn_height))
            pygame.draw.rect(WINDOW, BLACK, (x, y, btn_width, btn_height), 3)
            btn_font = pygame.font.Font(None, 42)
            text_surface = btn_font.render(text, True, btn_text_color)
            text_rect = text_surface.get_rect(center=(x + btn_width // 2, y + btn_height // 2))
            WINDOW.blit(text_surface, text_rect)

    def draw_calc_display():
        display_rect = pygame.Rect(20, 100, WINDOW_WIDTH - 40, 70)
        light_theme = tuple(min(c + 100, 255) for c in current_theme_color)
        pygame.draw.rect(WINDOW, light_theme, display_rect)
        pygame.draw.rect(WINDOW, BLACK, display_rect, 3)
        # Контрастный цвет для текста на дисплее
        if sum(current_theme_color) < 382:
            display_text_color = BLACK
        else:
            display_text_color = BLACK
        expr_surface = big_font.render(expression, True, display_text_color)
        expr_rect = expr_surface.get_rect(right=WINDOW_WIDTH - 30, centery=display_rect.centery)
        WINDOW.blit(expr_surface, expr_rect)

    def evaluate_expression(expr):
        try:
            allowed_chars = set("0123456789+-*/.()")
            if all(c in allowed_chars for c in expr):
                return str(eval(expr))
            else:
                return "Ошибка"
        except:
            return "Ошибка"

    back_btn = pygame.Rect(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 70, 200, 50)

    running_calc = True
    while running_calc:
        # ФОН ЦВЕТОМ ТЕМЫ
        WINDOW.fill(current_theme_color)

        # КОНТРАСТНЫЙ ЦВЕТ ЗАГОЛОВКА
        if sum(current_theme_color) < 382:
            title_color = BLACK
        else:
            title_color = BLACK

        title_text = big_font.render("КАЛЬКУЛЯТОР", True, title_color)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 50))
        WINDOW.blit(title_text, title_rect)

        draw_calc_display()
        draw_calc_buttons()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        back_hover = back_btn.collidepoint(mouse_x, mouse_y)
        draw_button(back_btn, "ВЫЙТИ", back_hover, RED, DARK_RED)
        draw_settings_icon()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_calc = False
                return False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_btn.collidepoint(event.pos):
                    return True

                for btn in calc_buttons:
                    text, x, y = btn
                    if x < event.pos[0] < x + btn_width and y < event.pos[1] < y + btn_height:
                        if text == 'C':
                            expression = ""
                            result = ""
                        elif text == '<-':
                            expression = expression[:-1]
                        elif text == '=':
                            result = evaluate_expression(expression)
                            expression = result
                        else:
                            expression += text

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
                elif event.key == pygame.K_RETURN:
                    result = evaluate_expression(expression)
                    expression = result
                elif event.key == pygame.K_BACKSPACE:
                    expression = expression[:-1]
                else:
                    char = event.unicode
                    if char in "0123456789+-*/.()":
                        expression += char

        pygame.display.flip()
        clock.tick(60)

    return True


def a2():
    """Экран перевода из десятичной в двоичную систему"""
    decimal_input = ""  # Вводимое десятичное число (строка)
    binary_output = ""  # Результат перевода в двоичную систему

    btn_width = 300
    btn_height = 100
    start_x = 60
    start_y = 220

    # Кнопки: цифры 0-9, стрелка назад, очистка, равно
    calc_buttons = [
        ('7', start_x, start_y),
        ('8', start_x + btn_width + 10, start_y),
        ('9', start_x + (btn_width + 10) * 2, start_y),
        ('4', start_x, start_y + btn_height + 10),
        ('5', start_x + btn_width + 10, start_y + btn_height + 10),
        ('6', start_x + (btn_width + 10) * 2, start_y + btn_height + 10),
        ('1', start_x, start_y + (btn_height + 10) * 2),
        ('2', start_x + btn_width + 10, start_y + (btn_height + 10) * 2),
        ('3', start_x + (btn_width + 10) * 2, start_y + (btn_height + 10) * 2),
        ('0', start_x, start_y + (btn_height + 10) * 3),
        ('<-', start_x + btn_width + 10, start_y + (btn_height + 10) * 3),
        ('C', start_x + (btn_width + 10) * 2, start_y + (btn_height + 10) * 3),

    ]

    def draw_calc_buttons():
        for btn in calc_buttons:
            text, x, y = btn
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if x < mouse_x < x + btn_width and y < mouse_y < y + btn_height:
                color = DARK_BLUE
            else:
                color = current_theme_color
            pygame.draw.rect(WINDOW, color, (x, y, btn_width, btn_height))
            pygame.draw.rect(WINDOW, BLACK, (x, y, btn_width, btn_height), 3)
            btn_font = pygame.font.Font(None, 42)
            # Контрастный цвет текста
            if sum(current_theme_color) < 382:
                text_color = WHITE
            else:
                text_color = BLACK
            text_surface = btn_font.render(text, True, text_color)
            text_rect = text_surface.get_rect(center=(x + btn_width // 2, y + btn_height // 2))
            WINDOW.blit(text_surface, text_rect)

    def draw_calc_display():
        display_rect = pygame.Rect(20, 100, WINDOW_WIDTH - 40, 100)
        light_theme = tuple(min(c + 100, 255) for c in current_theme_color)
        pygame.draw.rect(WINDOW, light_theme, display_rect)
        pygame.draw.rect(WINDOW, BLACK, display_rect, 3)

        # Подпись для десятичного числа
        dec_label = small_font.render("Десятичное:", True, BLACK)
        WINDOW.blit(dec_label, (30, 110))
        dec_surface = big_font.render(decimal_input, True, BLACK)
        WINDOW.blit(dec_surface, (30, 130))

        # Подпись для двоичного числа
        bin_label = small_font.render("Двоичное:", True, BLACK)
        WINDOW.blit(bin_label, (WINDOW_WIDTH - 250, 110))
        bin_surface = big_font.render(binary_output, True, BLACK)
        bin_rect = bin_surface.get_rect(right=WINDOW_WIDTH - 30, centery=145)
        WINDOW.blit(bin_surface, bin_rect)

    def decimal_to_binary(decimal_str):
        """Переводит десятичную строку в двоичную"""
        if not decimal_str:
            return ""
        try:
            n = int(decimal_str)
            if n < 0:
                return "Ошибка"
            return bin(n)[2:]  # bin(10) -> '0b1010', [2:] убирает '0b'
        except ValueError:
            return "Ошибка"

    back_btn = pygame.Rect(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 70, 200, 50)

    running_calc = True
    while running_calc:
        # Фон
        if sum(current_theme_color) < 382:
            bg_color = WHITE
            text_color = BLACK
        else:
            bg_color = current_theme_color
            text_color = WHITE
        WINDOW.fill(bg_color)

        # Заголовок
        title_text = font.render("ПЕРЕВОД ИЗ ДЕСЯТИЧНОЙ В ДВОИЧНУЮ", True, BLACK)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 50))
        WINDOW.blit(title_text, title_rect)

        draw_calc_display()
        draw_calc_buttons()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        back_hover = back_btn.collidepoint(mouse_x, mouse_y)
        draw_button(back_btn, "ВЫЙТИ", back_hover, RED, DARK_RED)
        draw_settings_icon()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_calc = False
                return False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_btn.collidepoint(event.pos):
                    return True

                for btn in calc_buttons:
                    text, x, y = btn
                    if x < event.pos[0] < x + btn_width and y < event.pos[1] < y + btn_height:
                        if text == 'C':
                            decimal_input = ""
                            binary_output = ""
                        elif text == '<-':
                            decimal_input = decimal_input[:-1]
                            binary_output = decimal_to_binary(decimal_input)
                        elif text == '=':
                            binary_output = decimal_to_binary(decimal_input)
                        else:
                            decimal_input += text
                            binary_output = decimal_to_binary(decimal_input)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
                elif event.key == pygame.K_RETURN:
                    binary_output = decimal_to_binary(decimal_input)
                elif event.key == pygame.K_BACKSPACE:
                    decimal_input = decimal_input[:-1]
                    binary_output = decimal_to_binary(decimal_input)
                else:
                    char = event.unicode
                    if char in "0123456789":
                        decimal_input += char
                        binary_output = decimal_to_binary(decimal_input)

        pygame.display.flip()
        clock.tick(60)

    return True


def a3():
    """Экран перевода из двоичной системы в десятичную"""
    binary_input = ""  # Вводимое двоичное число (строка)
    decimal_output = ""  # Результат перевода

    btn_width = 470
    btn_height = 100
    start_x = 20
    start_y = 180

    # Кнопки: цифры 0-1, стрелка назад, очистка, равно
    calc_buttons = [
        ('0', start_x, start_y),
        ('1', start_x + btn_width + 10, start_y),
        ('<-', start_x, start_y + btn_height + 10),
        ('C', start_x + btn_width + 10, start_y + btn_height + 10),
    ]

    def draw_calc_buttons():
        for btn in calc_buttons:
            text, x, y = btn
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if x < mouse_x < x + btn_width and y < mouse_y < y + btn_height:
                color = DARK_BLUE
            else:
                color = current_theme_color
            pygame.draw.rect(WINDOW, color, (x, y, btn_width, btn_height))
            pygame.draw.rect(WINDOW, BLACK, (x, y, btn_width, btn_height), 3)
            btn_font = pygame.font.Font(None, 42)
            # Белый текст для тёмных кнопок
            if sum(current_theme_color) < 382:
                text_color = WHITE
            else:
                text_color = BLACK
            text_surface = btn_font.render(text, True, text_color)
            text_rect = text_surface.get_rect(center=(x + btn_width // 2, y + btn_height // 2))
            WINDOW.blit(text_surface, text_rect)

    def draw_calc_display():
        display_rect = pygame.Rect(20, 100, WINDOW_WIDTH - 40, 70)
        light_theme = tuple(min(c + 100, 255) for c in current_theme_color)
        pygame.draw.rect(WINDOW, light_theme, display_rect)
        pygame.draw.rect(WINDOW, BLACK, display_rect, 3)

        # Показываем двоичное число
        bin_label = small_font.render("Двоичное:", True, BLACK)
        WINDOW.blit(bin_label, (30, 110))
        bin_surface = big_font.render(binary_input, True, BLACK)
        WINDOW.blit(bin_surface, (30, 130))

        # Показываем десятичный результат
        dec_label = small_font.render("Десятичное:", True, BLACK)
        WINDOW.blit(dec_label, (WINDOW_WIDTH - 250, 110))
        dec_surface = big_font.render(decimal_output, True, BLACK)
        dec_rect = dec_surface.get_rect(right=WINDOW_WIDTH - 30, centery=145)
        WINDOW.blit(dec_surface, dec_rect)

    def binary_to_decimal(binary_str):
        """Переводит двоичную строку в десятичное число"""
        if not binary_str:
            return ""
        try:
            # Проверяем, что все символы - 0 или 1
            if all(c in '01' for c in binary_str):
                return str(int(binary_str, 2))
            else:
                return "Ошибка: только 0 и 1"
        except:
            return "Ошибка"

    back_btn = pygame.Rect(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 70, 200, 50)

    running_calc = True
    while running_calc:
        # Фон цветом темы
        if sum(current_theme_color) < 382:
            bg_color = WHITE
            text_color = BLACK
        else:
            bg_color = current_theme_color
        WINDOW.fill(bg_color)

        # Заголовок
        title_text = font.render("ПЕРЕВОД ИЗ ДВОИЧНОЙ В ДЕСЯТИЧНУЮ", True, BLACK)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 50))
        WINDOW.blit(title_text, title_rect)

        draw_calc_display()
        draw_calc_buttons()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        back_hover = back_btn.collidepoint(mouse_x, mouse_y)
        draw_button(back_btn, "ВЫЙТИ", back_hover, RED, DARK_RED)
        draw_settings_icon()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_calc = False
                return False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_btn.collidepoint(event.pos):
                    return True

                for btn in calc_buttons:
                    text, x, y = btn
                    if x < event.pos[0] < x + btn_width and y < event.pos[1] < y + btn_height:
                        if text == 'C':  # Очистка
                            binary_input = ""
                            decimal_output = ""
                        elif text == '<–':  # Удаление символа
                            binary_input = binary_input[:-1]
                            decimal_output = binary_to_decimal(binary_input)
                        elif text == '=':  # Вычисление
                            decimal_output = binary_to_decimal(binary_input)
                        else:  # Цифра 0 или 1
                            binary_input += text
                            decimal_output = binary_to_decimal(binary_input)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
                elif event.key == pygame.K_RETURN:
                    decimal_output = binary_to_decimal(binary_input)
                elif event.key == pygame.K_BACKSPACE:
                    binary_input = binary_input[:-1]
                    decimal_output = binary_to_decimal(binary_input)
                else:
                    char = event.unicode
                    if char in '01':  # Разрешаем только 0 и 1
                        binary_input += char
                        decimal_output = binary_to_decimal(binary_input)

        pygame.display.flip()
        clock.tick(60)

    return True
# ========== ГЛАВНЫЙ ИГРОВОЙ ЦИКЛ ==========
clock = pygame.time.Clock()  # Создаем объект Clock для управления FPS
running = True  # Флаг работы главного цикла

while running:  # Бесконечный цикл, пока running = True
    mouse_pos = pygame.mouse.get_pos()  # Получаем текущую позицию мыши

    # ========== ОБНОВЛЕНИЕ СОСТОЯНИЙ НАВЕДЕНИЯ ==========
    settings_icon_hover = settings_icon_rect.collidepoint(mouse_pos)  # Проверка наведения на иконку настроек

    # В зависимости от текущего экрана обновляем состояния кнопок
    if current_screen == "menu":  # Главное меню
        login_btn_hover = login_btn_rect.collidepoint(mouse_pos)
        register_btn_hover = register_btn_rect.collidepoint(mouse_pos)
        # Сбрасываем остальные кнопки
        back_btn_hover = False
        submit_btn_hover = False
        logout_btn_hover = False

    elif current_screen == "login":  # Экран входа
        login_btn_hover = False
        register_btn_hover = False
        back_btn_hover = back_btn_rect.collidepoint(mouse_pos)
        submit_btn_hover = submit_btn_rect.collidepoint(mouse_pos)
        logout_btn_hover = False

        # Если активны поля ввода, отключаем наведение на кнопки
        if login_active or password_active:
            submit_btn_hover = False
            back_btn_hover = False

    elif current_screen == "register":  # Экран регистрации
        login_btn_hover = False
        register_btn_hover = False
        back_btn_hover = back_btn_rect.collidepoint(mouse_pos)
        submit_btn_hover = submit_btn_rect.collidepoint(mouse_pos)
        logout_btn_hover = False

        if login_active or password_active:
            submit_btn_hover = False
            back_btn_hover = False

    elif current_screen == "profile":  # Экран профиля
        login_btn_hover = False
        register_btn_hover = False
        back_btn_hover = False
        submit_btn_hover = False
        logout_btn_hover = logout_btn_rect.collidepoint(mouse_pos)

        # Обновляем наведение для всех 18 кнопок профиля
        profile_btn_hover[0] = profile_btn1.collidepoint(mouse_pos)
        profile_btn_hover[1] = profile_btn2.collidepoint(mouse_pos)
        profile_btn_hover[2] = profile_btn3.collidepoint(mouse_pos)
        profile_btn_hover[3] = profile_btn4.collidepoint(mouse_pos)
        profile_btn_hover[4] = profile_btn5.collidepoint(mouse_pos)
        profile_btn_hover[5] = profile_btn6.collidepoint(mouse_pos)
        profile_btn_hover[6] = profile_btn7.collidepoint(mouse_pos)
        profile_btn_hover[7] = profile_btn8.collidepoint(mouse_pos)
        profile_btn_hover[8] = profile_btn9.collidepoint(mouse_pos)
        profile_btn_hover[9] = profile_btn10.collidepoint(mouse_pos)
        profile_btn_hover[10] = profile_btn11.collidepoint(mouse_pos)
        profile_btn_hover[11] = profile_btn12.collidepoint(mouse_pos)
        profile_btn_hover[14] = profile_btn15.collidepoint(mouse_pos)
        profile_btn_hover[15] = profile_btn16.collidepoint(mouse_pos)
        profile_btn_hover[16] = profile_btn17.collidepoint(mouse_pos)
        profile_btn_hover[17] = profile_btn18.collidepoint(mouse_pos)

    elif current_screen == "settings":  # Экран настроек
        login_btn_hover = False
        register_btn_hover = False
        back_btn_hover = False
        submit_btn_hover = False
        logout_btn_hover = False

        # Обновляем наведение для кнопок выбора цвета
        for i, (btn_rect, _, _) in enumerate(color_buttons):
            color_buttons_hover[i] = btn_rect.collidepoint(mouse_pos)

    # ========== ОБРАБОТКА СОБЫТИЙ ==========
    for event in pygame.event.get():  # Перебираем все события
        if event.type == pygame.QUIT:  # Если нажали крестик
            if current_user:  # Если пользователь авторизован
                settings["saved_user"] = current_user  # Сохраняем его для автовхода
                save_settings(settings)  # Сохраняем настройки
            running = False  # Завершаем главный цикл

        # ========== ОБРАБОТКА КЛИКОВ МЫШИ ==========
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши

                # Иконка настроек (работает с любого экрана)
                if settings_icon_rect.collidepoint(event.pos):
                    current_screen = "settings"  # Переход к настройкам

                # Обработка кликов в зависимости от экрана
                elif current_screen == "menu":
                    if login_btn_rect.collidepoint(event.pos):  # Кнопка "Вход"
                        login_text = ""  # Очищаем поля
                        password_text = ""
                        login_active = False
                        password_active = False
                        current_screen = "login"  # Переходим на экран входа

                    elif register_btn_rect.collidepoint(event.pos):  # Кнопка "Регистрация"
                        login_text = ""
                        password_text = ""
                        login_active = False
                        password_active = False
                        current_screen = "register"  # Переходим на экран регистрации

                elif current_screen == "settings":
                    # Проверяем клик по кнопкам выбора цвета
                    for i, (btn_rect, color, name) in enumerate(color_buttons):
                        if btn_rect.collidepoint(event.pos):
                            current_theme_color = color  # Меняем цвет темы
                            current_theme_name = name
                            settings["theme_color"] = current_theme_color  # Сохраняем
                            settings["theme_color_name"] = current_theme_name
                            if current_user:
                                settings["saved_user"] = current_user
                            save_settings(settings)  # Сохраняем настройки в файл
                            show_message(f"Цвет изменен на {name}!", False)  # Показываем сообщение
                            # Возвращаемся на предыдущий экран
                            if current_user:
                                current_screen = "profile"
                            else:
                                current_screen = "menu"
                            break  # Выходим из цикла, чтобы не обрабатывать другие кнопки

                    # Проверяем клик по кнопке "Назад" в настройках
                    back_btn_rect_settings = pygame.Rect(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 100, 200, 50)
                    if back_btn_rect_settings.collidepoint(event.pos):
                        if current_user:
                            current_screen = "profile"  # Возврат в профиль
                        else:
                            current_screen = "menu"  # Возврат в меню

                elif current_screen in ["login", "register"]:
                    # Активация полей ввода при клике на них
                    login_active = login_rect.collidepoint(event.pos)
                    password_active = password_rect.collidepoint(event.pos)

                    if current_screen == "login":
                        # Обработка кнопки "ВОЙТИ"
                        if submit_btn_rect.collidepoint(event.pos) and not (login_active or password_active):
                            if login_text and password_text:  # Проверяем, что поля заполнены
                                if login_text in users and users[
                                    login_text] == password_text:  # Проверка логина и пароля
                                    current_user = login_text  # Авторизуем пользователя
                                    settings["saved_user"] = current_user  # Сохраняем для автовхода
                                    save_settings(settings)
                                    show_message(f"Добро пожаловать, {login_text}!", False)
                                    login_text = ""  # Очищаем поля
                                    password_text = ""
                                    current_screen = "profile"  # Переход в профиль
                                else:
                                    show_message("Неверный логин или пароль!", True)  # Ошибка
                            else:
                                show_message("Заполните все поля!", True)  # Ошибка

                        # Кнопка "НАЗАД"
                        elif back_btn_rect.collidepoint(event.pos) and not (login_active or password_active):
                            login_text = ""
                            password_text = ""
                            current_screen = "menu"  # Возврат в меню

                    elif current_screen == "register":
                        # Обработка кнопки "ЗАРЕГИСТРИРОВАТЬСЯ"
                        if submit_btn_rect.collidepoint(event.pos) and not (login_active or password_active):
                            if login_text and password_text:
                                if login_text in users:  # Проверка существования пользователя
                                    show_message("Пользователь уже существует!", True)
                                elif len(login_text) < 3:  # Проверка длины логина
                                    show_message("Логин должен содержать минимум 3 символа!", True)
                                elif len(password_text) < 4:  # Проверка длины пароля
                                    show_message("Пароль должен содержать минимум 4 символа!", True)
                                else:
                                    users[login_text] = password_text  # Сохраняем нового пользователя
                                    save_users(users)  # Сохраняем в файл
                                    current_user = login_text  # Автоматически входим
                                    settings["saved_user"] = current_user
                                    save_settings(settings)
                                    show_message(f"Пользователь {login_text} зарегистрирован!", False)
                                    login_text = ""
                                    password_text = ""
                                    current_screen = "profile"  # Переход в профиль
                            else:
                                show_message("Заполните все поля!", True)

                        # Кнопка "НАЗАД"
                        elif back_btn_rect.collidepoint(event.pos) and not (login_active or password_active):
                            login_text = ""
                            password_text = ""
                            current_screen = "menu"

                elif current_screen == "profile":
                    # Кнопка выхода из профиля
                    if logout_btn_rect.collidepoint(event.pos):
                        current_user = None  # Сбрасываем пользователя
                        settings["saved_user"] = None  # Убираем автовход
                        save_settings(settings)
                        current_screen = "menu"  # Возврат в меню

                    # Обработка кнопок профиля
                    elif profile_btn1.collidepoint(event.pos):
                        current_screen = "a1"
                    elif profile_btn7.collidepoint(event.pos):
                        current_screen = "a3"
                    elif profile_btn8.collidepoint(event.pos):
                        current_screen = "a2"
                    elif profile_btn4.collidepoint(event.pos):
                        print()
                    elif profile_btn5.collidepoint(event.pos):
                        print()
                    elif profile_btn6.collidepoint(event.pos):
                        print()
        # ========== ОБРАБОТКА НАЖАТИЙ КЛАВИШ ==========
        if event.type == pygame.KEYDOWN and current_screen in ["login", "register"]:
            if event.key == pygame.K_RETURN:  # Enter - подтверждение
                login_active = False
                password_active = False

                if current_screen == "login":
                    # Та же логика, что и при клике на кнопку "ВОЙТИ"
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
                    # Та же логика, что и при клике на кнопку регистрации
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

            elif event.key == pygame.K_TAB:  # Tab - переключение между полями
                if login_active:
                    login_active = False
                    password_active = True
                elif password_active:
                    password_active = False
                    login_active = True

            elif login_active:  # Если активно поле логина
                if event.key == pygame.K_BACKSPACE:  # Backspace - удалить символ
                    login_text = login_text[:-1]
                else:  # Добавляем символ
                    if len(login_text) < 20 and event.unicode.isprintable():  # Ограничение 20 символов
                        login_text += event.unicode

            elif password_active:  # Если активно поле пароля
                if event.key == pygame.K_BACKSPACE:
                    password_text = password_text[:-1]
                else:
                    if len(password_text) < 20 and event.unicode.isprintable():
                        password_text += event.unicode

    # ========== ОТРИСОВКА ТЕКУЩЕГО ЭКРАНА ==========
    if current_screen == "menu":
        draw_menu()  # Рисуем главное меню
    elif current_screen == "login":
        draw_login_screen()  # Рисуем экран входа
    elif current_screen == "register":
        draw_register_screen()  # Рисуем экран регистрации
    elif current_screen == "profile":
        draw_profile_screen()  # Рисуем профиль
    elif current_screen == "settings":
        draw_settings_screen()  # Рисуем настройки
    elif current_screen == "a1":
        a1()
        current_screen = "profile"
    elif current_screen == "a2":
        a2()
        current_screen = "profile"
    elif current_screen == "a3":
        a3()
        current_screen = "profile"

    pygame.display.flip()  # Обновляем экран (показываем всё, что нарисовали)
    clock.tick(60)  # Ограничиваем FPS до 60 кадров в секунду

# ========== ЗАВЕРШЕНИЕ РАБОТЫ ==========
pygame.quit()  # Закрываем все модули Pygame
sys.exit()  # Завершаем программу
