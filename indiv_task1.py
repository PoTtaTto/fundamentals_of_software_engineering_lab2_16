#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Standard
import sys
from random import randint
import json


def add_train(trains):
    """
    Добавляет информацию о поезде в список trains.

    Args:
    - trains (list): Список поездов.

    """
    train_num = int(input('Введите номер поезда: '))
    destination = input('Введите пункт назначения: ')
    start_time = input('Введите время выезда: ')
    trains.append({'num': train_num, 'destination': destination, 'start_time': start_time})
    if len(trains) > 1:
        trains.sort(key=lambda item: item['start_time'])


def save_trains(file_name, trains):
    """
    Сохраняет список поездов в файл в формате JSON.

    Args:
    - file_name (str): Имя файла.
    - trains (list): Список поездов.

    """
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(trains, fout, ensure_ascii=False, indent=4)


def load_trains(file_name):
    """
    Загружает список поездов из файла в формате JSON.

    Args:
    - file_name (str): Имя файла.

    Returns:
    - trains (list): Список поездов.

    """
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


def list_trains(trains):
    """
    Выводит список поездов на экран.

    Args:
    - trains (list): Список поездов.

    """
    line = f'+-{"-" * 15}-+-{"-" * 30}-+-{"-" * 25}-+'
    print(line)
    header = f"| {'№ поезда':^15} | {'Пункт назначения':^30} | {'Время отъезда':^25} |"
    print(header)
    print(line)
    for train in trains:
        num = train.get('num', randint(1000, 10000))
        destination = train.get('destination', 'None')
        start_time = train.get('start_time', 'None')
        recording = f"| {num:^15} | {destination:^30} | {start_time:^25} |"
        print(recording)
    print(line)


def select_train(trains, cmd_parts):
    """
    Выводит информацию о поездах, направляющихся в указанный пункт.

    Args:
    - trains (list): Список поездов.
    - cmd_parts (list): Список команды и параметра.

    """
    cmd_destination = cmd_parts[1]
    select_trains = [train for train in trains if train['destination'].strip() == cmd_destination]
    if len(select_trains) >= 1:
        for train in select_trains:
            print(f'{train["num"]:^15}: {train["start_time"]:^25}')
    else:
        print('Нет поездов едущих в данное место!', file=sys.stderr)


def show_help():
    """
    Выводит список доступных команд на экран.

    """
    print("Список команд:\n")
    print("add - добавить поезд;")
    print("list - вывести список поездов;")
    print("select <пункт назначения> - запросить поезда с пунктом назначения;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


if __name__ == '__main__':
    trains = []
    while True:
        cmd = input('>>> ')
        cmd_parts = cmd.split(maxsplit=1)
        match cmd_parts[0]:
            case 'add':
                add_train(trains)
            case 'list':
                list_trains(trains)
            case 'select':
                select_train(trains, cmd_parts)
            case 'help':
                show_help()
            case 'exit':
                break
            case 'save':
                if len(cmd_parts) == 2:
                    save_trains(cmd_parts[1], trains)
                else:
                    print("Использование: save <имя файла>", file=sys.stderr)
            case 'load':
                if len(cmd_parts) == 2:
                    trains = load_trains(cmd_parts[1])
                else:
                    print("Использование: load <имя файла>", file=sys.stderr)
            case _:
                print(f'Неизвестная команда {cmd}', file=sys.stderr)
