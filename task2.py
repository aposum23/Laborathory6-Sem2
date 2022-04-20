#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from jsonschema import validate
from pathlib import Path
import os
from dotenv import load_dotenv


os.environ.setdefault('FILE_NAME', 'json_file.json')
SETTINGS_FILE = 'settings.json'


def add_element():
    name = input('Конечный пункт: ')
    num = input('Номер поезда: ')
    tm = input('Время отправления: ')
    trains = {}
    trains['name'] = name
    trains['num'] = int(num)
    trains['tm'] = tm
    schema = ''
    with open('schema.json', 'r') as f:
        schema = json.loads(f.read())
    validate(instance=trains, schema=schema)
    with open(os.getenv('FILE_NAME'), 'a') as f:
        f.write(json.dumps(trains) + '\n')


def find_train(num):
    with open(os.getenv('FILE_NAME'), 'r') as f:
        trains = f.readlines()
        for dcts in trains:
            dcts = json.loads(dcts)
            if dcts['num'] == int(num):
                print(
                    f'Конечный пункт: {dcts["name"]} \n'
                    f'Номер поезда: {dcts["num"]} \n'
                    f'Время отправления: {(dcts["tm"])}'
                )
                print(f'Datafile name: {os.getenv("FILE_NAME")}')
                return
        print('Поезда с таким номером нет')


if __name__ == '__main__':
    print('LOADING...')
    dotenv_path = os.path.join(os.path.dirname(__file__), 'config.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    print(dotenv_path)
    with open(SETTINGS_FILE, 'r') as f:
        settings = json.loads(f.read())
        if settings['gitignore'] == False:
            path = Path(__file__).resolve()
            print(path.parents[1])
            par_path = path.parents[1]
            with open(str(par_path) + '\\.gitignore', 'a') as gig:
                gig.write('\n' + '*.json' + '\n')
                gig.write('\n' + '*.env' + '\n')
    with open(SETTINGS_FILE, 'w') as f:
        f.write(json.dumps({'gitignore': True}))

    print('Hello!')

    flag = True
    while flag:
        print('1. Добавить новый поезд')
        print('2. Вывести информацию о поезде')
        print('3.Выход из программы')
        com = int(input('введите номер команды: '))
        if com == 1:
            add_element()
        elif com == 2:
            train_num = input('Введите номер поезда: ')
            find_train(train_num)
        elif com == 3:
            flag = False
