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

# --- Формуляр героя --------------------------------
print("Характеристики героя:")
print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Интеллект: {intellect}")
print(f"Выносливость: {stamina}")
print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")

# --- Меню действий ---------------------------------
running = True
actions = 0
outcome = "прерывание"
menu_last = 8
enemies = ["ghoul", "skeleton", "spider", "bat"]
log = []  # Журнал боя: список списков [[раунд, урон_героя, урон_врага], ...]

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
                    if i % 3 == 0:
                        hit_damage = crit_damage
                        print(f"Удар {i}: {hit_damage:.1f} — критический!")
                        crit_count += 1
                    else:
                        hit_damage = damage
                        print(f"Удар {i}: {hit_damage:.1f} урона")
                    
                    total_damage += hit_damage

                print()
                print(f"Итог: {strikes} ударов, {crit_count} критических.")
                print(f"Общий урон: {total_damage:.1f}")
                print(f"Средний урон: {total_damage / strikes:.1f}")
                
                stamina = stamina - 2

            case "7":
                if not enemies:
                    print("The dungeon is empty.")
                else:
                    enemy = random.choice(enemies)
                    enemy_hp = 45
                    round_n = 0
                    
                    print(f"You descend the stairs. A {enemy} emerges from the darkness!")
                    
                    # Бой циклом while
                    while enemy_hp > 0 and health > 0:
                        round_n += 1
                        
                        if round_n % 3 == 0:
                            hit_damage = crit_damage
                            crit_str = " — critical!"
                        else:
                            hit_damage = damage
                            crit_str = ""
                            
                        enemy_hp -= hit_damage
                        
                        # Ответный урон врага
                        enemy_strike = random.randint(2, 6)
                        
                        if enemy_hp <= 0:
                            line = f"Round {round_n}: you deal {hit_damage:.1f} damage{crit_str} Enemy falls."
                            log.append([round_n, hit_damage, 0])
                            print(line)
                            break
                        else:
                            health -= enemy_strike
                            line = f"Round {round_n}: you deal {hit_damage:.1f} damage{crit_str}. {enemy} health: {enemy_hp:.1f}. {enemy} hits back for {enemy_strike}."
                            log.append([round_n, hit_damage, enemy_strike])
                            print(line)

                    # Итог боя
                    if enemy_hp <= 0:
                        enemies.remove(enemy)
                        print(f"The {enemy} is defeated! {len(enemies)} enemies left in the dungeon.")
                        print(f"Battle: {round_n} rounds.")

            case "8":
                if not log:
                    print("You haven't fought yet.")
                else:
                    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
                    print("Leaderboard (hero damage):")
                    for i in range(len(top)):
                        print(f"{i + 1}. Round {top[i][0]}: {top[i][1]:.1f}")

                    worst = max(log, key=lambda r: r[2])
                    print(f"Strongest enemy hit: {worst[2]} (round {worst[0]}).")

        print(f"Здоровье: {health} | Запас сил: {stamina} | Врагов осталось: {len(enemies)}")
                
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

    # Вывод итогов по урону с использованием агрегаторов (sum, len)
    rounds = len(log)
    if rounds > 0:
        total = sum(r[1] for r in log)
        print(f"Damage: {total:.1f} across {rounds} rounds, average {total / rounds:.1f}.")
    else:
        print("No battles this run.")