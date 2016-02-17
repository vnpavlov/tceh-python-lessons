#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
if sys.version_info[0] < 3:
	input_good=raw_input
else:
	input_good=input

def question_ask(text, answer):
    print ("\n   "+text+"\n")
    #while 
    player_answer=""
    fails=0

    while player_answer!=answer:
        player_answer=input_good(">")
        if player_answer!=answer:
	        print ("Увы, ответ неверный. Попробуйте ещё раз!")
	        fails+=1

    return fails


questions = ["True - True * True - True", "str(int(1/2))*5", '(bool("")==False)*5', "'12345'[::2]*2", "'01010'[0][0][0]", '"Trick"[0:2] is "Tr"']
answers = ["-1", "00000", "5", "135135", "0", "False"]
fails=0

print ("Поучаствуйте в викторине, посвящённой языку Python!\n\nВведите результат выполнения выражения в интерпретаторе Python\n\n")

for question_count in range(len(questions)):
	fails+=question_ask(questions[question_count], answers[question_count])

print (u"\nБлагодарим Вас!\nОшибок: %d" % fails)