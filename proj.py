from time import time
import tkinter

def start():
    print('Введите ваше ФИО:',student = input())
    print('Введите ваш класс:',class = input())

def trMod():

def ktMod():

def sound():

def imd():

def txt():

def dec():

def ans():



export = {
    'taskName': '', #Имя задания (тип)
    'student': '', #Фамилия Имя Отчество
    'class': '11В', #класс подопытного
    'mark': 0.0, #оценка за все подзадания. Дробь, от 0 до 1
    'datetime': time(), #time in seconds, float. Можно получать его так, а можно самому вычислять для получения даты без времени, например.
    'subTasks': [ # массив подзаданий
        {
            'name': '', #имя (подтип).
            'text': '', #текст
            'correctAnswer': '', #правильный ответ
            'answer': '' #ответ, данный учеником
        }#, {...}, ...
    ]
}
