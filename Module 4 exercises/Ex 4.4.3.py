"""Условие задачи: напишите программу, которая в зависимости от скорости ветра выдаёт сообщение о его характере:
от 1 до 4 м/с — слабый (1);
от 5 до 10 м/c — умеренный (2);
от 11 до 18 м/c — сильный (3);
больше 19 м/c — ураганный (4)."""

speed = int(input("Введите скорость ветра:"))
if 1 <= speed <= 4:
    print("слабый")
if 5 <= speed <= 10:
    print("умеренный")
if 11 <= speed <= 18:
    print("сильный")
if 19 <= speed:
    print("ураганный")
