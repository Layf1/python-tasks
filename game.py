# ================================================
# ИГРА «ПОДЗЕМЕЛЬЕ: ОСТРЫЕ ПИКИ»
# Автор: Веселов Павел
# Дата: сентябрь 2026
import random

# --- Заголовок ------------------------------------
title = "ОСТРЫЕ ПИКИ"
frame = "=" * 17
print(frame)         
print(" " + title + " ")
print(frame)
print()

# --- Знакомство с героем --------------------------
print("Как зовут героя?")
hero_name = input()
print(f"Добро пожаловать, {hero_name}!")
print("Ты входишь в подземелье. Здесь веет холодом и смертью.")
print()

# --- Настройка героя -------------------------------
print("Настройка героя.")
print("Здоровье, сила, ловкость, интеллект — по одному числу в строке:")

while True:
    try:
        health = int(input())
        strength = int(input())
        agility = int(input())
        intellect = int(input())

        # Проверка правил через raise
        if health <= 0:
            raise ValueError(f"Здоровье должно быть положительным, а введено {health}")
        if strength < 0 or agility < 0 or intellect < 0:
            raise ValueError("Характеристики не могут быть отрицательными")
        
        break  # Ввод успешен
    except ValueError as e:
        print(f"Ошибка: {e}. Введите все четыре числа заново:")

stamina = (health + agility * 1.5) // 5

print()

# --- Расчёт урона ----------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2

# --- Потолки характеристик -------------------------
max_health = health
max_stamina = stamina

# --- Формуляр героя --------------------------------
print("Характеристики героя:")
print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Интеллект: {intellect}")
print(f"Выносливость: {stamina}")
print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")


def hero_hit(strike_n):
    """Урон героя в удар номер strike_n.
    Возвращает пару (hit, crit).
    Читает глобальные правила damage и crit_damage.
    """
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False


def fight(enemy, hero_health, bonus=0):
    """Бой с врагом до гибели одного из двоих.
    bonus — надбавка к урону героя, по умолчанию 0: без эликсира
    бой идёт как прежде. Печатает строки раундов.
    Возвращает (rounds, won, hero_health, loot).
    Бонус прибавляется к урону удара после определения крита.
    """
    enemy_hp = 45.0
    rounds = []
    round_n = 0
    
    print(f"You descend the stairs. Out of the darkness comes {enemy}!")
    
    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n)
        hit = hit + bonus  # Прибавление бонуса эликсира
        enemy_hp -= hit
        
        line = f"Round {round_n}: hero deals {hit:.1f}"
        if crit:
            line += " critical!"
            
        if enemy_hp <= 0:
            line += " Enemy falls."
            rounds.append([round_n, hit, 0])
            print(line)
            break
        else:
            blow = random.randint(2, 6)
            hero_health -= blow
            line += f" {enemy} health: {enemy_hp:.1f}. {enemy.capitalize()} hits for {blow}."
            rounds.append([round_n, hit, blow])
            print(line)
            
    won = enemy_hp <= 0
    if won:
        loot = 25
    else:
        loot = 0
        
    return rounds, won, hero_health, loot


def buy(price, gold, quantity=1):
    """Покупает quantity штук товара ценой price за золото gold.
    quantity по умолчанию 1. Возвращает (gold_left, ok): остаток
    золота и признак успешной покупки. Ничего не печатает.
    """
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False


def print_leaderboard(log):
    """Печатает топ-3 раундов по урону героя и рекорд врага.
    Возвращает None: контракт функции — печать, а не данные.
    """
    if not log:
        print("You haven't fought yet.")
        return
        
    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
    print("Leaderboard (hero damage):")
    for i in range(len(top)):
        print(f"{i + 1}. Round {top[i][0]}: {top[i][1]:.1f}")
        
    worst = max(log, key=lambda r: r[2])
    print(f"Strongest enemy hit: {worst[2]} (round {worst[0]}).")


def print_run_summary(log):
    """Печатает итог забега: суммарный и средний урон героя.
    Возвращает None. Безопасна на пустом журнале.
    """
    rounds = len(log)
    if rounds > 0:
        total = sum(r[1] for r in log)
        print(f"Damage: {total:.1f} across {rounds} rounds, average {total / rounds:.1f}.")
    else:
        print("No battles this run.")


# --- Главные переменные игры -----------------------
running = True
actions = 0
outcome = "прерывание"
menu_last = 9
enemies = ["ghoul", "skeleton", "spider", "bat"]
log = []  # Журнал боя: таблица (список списков)
gold_total = 0
ability_bonus = 0

# --- Главный цикл игры -----------------------------
try:
    while running:
        print("\nЧто делаешь?")
        print("1 - осмотреться")
        print("2 - идти вперёд")
        print("3 - отдохнуть")
        print("4 - проверить снаряжение")
        print("5 - попытаться кого-нибудь позвать")
        print("6 - тренировка")
        print("7 - descend deeper")
        print("8 - leaderboard")
        print("9 - shop")
        print("0 - выйти из подземелья")

        while True:
            choice = input()
            try:
                menu_number = int(choice)
                if 0 <= menu_number <= menu_last:
                    break
                print("Такого пункта нет. Введи номер пункта из меню:")
            except ValueError:
                print("Введите число — номер пункта из меню:")

        actions += 1

        # --- Выбор действия --------------------------------
        match choice:
            case "0":
                print("Вы поднимаетесь обратно к свету. Подземелье остаётся позади.")
                outcome = "выход"
                running = False

            case "1":
                print("Вы осмотрелись. Комната пуста, лишь слышен гул ветра в глубине туннеля.")

            case "2":
                stamina = stamina - 3
                print("Вы осторожно идёте вперёд. Пол скрипит под ногами.")

            case "3":
                strength = strength + 2
                damage = base_attack + strength * 1.5
                crit_damage = damage * 2
                print("Вы решили отдохнуть, вы восстановили ваши силы.")

            case "4":
                print("Вы решили ещё раз проверить всё ли вы взяли с собой, всё на месте.")

            case "5":
                print("Вы решили позвать кого-нибудь, вы слышите лишь эхо своего голоса.")   

            case "6":
                strikes = 4
                crit_count = 0
                total_damage = 0.0

                print("Вы подходите к тренировочному чучелу.")
                print("Оно явно здесь стоит давно")
                print("Чучело стоит посреди комнаты, вы явно не первый кто его обнаружил")
                print(f"Наносите {strikes} ударов.")

                for i in range(1, strikes + 1):
                    hit_damage, crit = hero_hit(i)
                    hit_damage = hit_damage + ability_bonus
                    if crit:
                        print(f"Удар {i}: {hit_damage:.1f} — критический!")
                        crit_count += 1
                    else:
                        print(f"Удар {i}: {hit_damage:.1f} урона")
                    
                    total_damage += hit_damage

                print()
                print(f"Итог: {strikes} ударов, {crit_count} критических.")
                print(f"Общий урон: {total_damage:.1f}")
                print(f"Средний урон: {total_damage / strikes:.1f}")
                
                stamina = stamina - 2

            case "7":
                if not enemies:
                    print("You descend the stairs. But the dungeon is empty.")
                else:
                    enemy = random.choice(enemies)
                    rounds, won, health, loot = fight(enemy, health, bonus=ability_bonus)
                    
                    for r in rounds:
                        log.append(r)
                        
                    if won:
                        gold_total += loot
                        enemies.remove(enemy)
                        print(f"{enemy.capitalize()} defeated! {len(enemies)} enemies left in the dungeon. Loot: {loot} gold.")
                        print(f"Battle: {len(rounds)} rounds.")

            case "8":
                print_leaderboard(log)

            case "9":
                print("Shop:")
                print("1 - potion (+10 health): 10 gold")
                print("2 - torch oil (+5 stamina): 15 gold")
                print("3 - war elixir (+2 damage for the run): 40 gold")
                print("Item number (0 not buying):")
                
                item = input()
                prices = (10, 15, 40)
                names = ("potion", "torch oil", "war elixir")
                
                if item in ("1", "2", "3"):
                    idx = int(item) - 1
                    price = prices[idx]
                    name = names[idx]
                    
                    print("Quantity (Enter for one):")
                    qty_line = input()
                    
                    if qty_line == "":
                        qty = 1
                        gold_total, ok = buy(price, gold_total)
                    else:
                        qty = int(qty_line)
                        gold_total, ok = buy(price, gold_total, quantity=qty)
                        
                    if ok:
                        if item == "1":
                            health = min(health + 10 * qty, max_health)
                        elif item == "2":
                            stamina = min(stamina + 5 * qty, max_stamina)
                        else:
                            ability_bonus += 2 * qty
                        print(f"Bought {qty} {name} for {price * qty} gold. Gold left: {gold_total}.")
                    else:
                        print(f"Not enough gold: need {price * qty}, have {gold_total}.")
                elif item != "0":
                    print("No such item in the shop.")

        print(f"Health: {health} | Stamina: {stamina} | Enemies left: {len(enemies)} | Gold: {gold_total}")
                
        if stamina <= 0:
            print("Вы обессилели и не можете продолжать путь.")
            outcome = "гибель"
            running = False
            
except KeyboardInterrupt:
    print()
    print("Игрок прервал сеанс.")

finally:
    # --- Прощание------------------------------------
    print()
    frame_bye = "=" * 12
    print(frame_bye)
    print("  ПРОЩАЙ  ")
    print(frame_bye)

    if outcome == "гибель":
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Сеанс прерван, {hero_name}. Действий совершено: {actions}.")

    print_run_summary(log)