import csv
import os
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class QuizQuestion:
    def __init__(self, category, question, answer, description) -> None:
        self.category = category
        self.question = question
        self.answer = answer
        self.description = description



class QuizGame:
    question_list = []
    def __init__(self, file_path) -> None:
        self.load_from_csv(file_path)

    def append(self, category, question, answer, description):
        self.question_list.append(QuizQuestion(category, question, answer, description))
    
    def load_from_csv(self, file_path):
        file = open(file_path, mode='r')
        reader = csv.reader(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            self.append(row[0], row[1], row[2], row[3])

    def get_answer(self):
        answer = ""
        while answer not in ['true', 'false', 't', 'f']:
            answer = input("True(t) or False(f): ").lower()
        if answer in ['true', 't']:
            return 'True'
        if answer in ['false', 'f']:
            return 'False'


    
    def play(self):
        os.system('clear')
        print("Hello and welcome to QuizGame!")
        for counter in range(0,100):
            print(f"Question {counter+1}.")
            print("~"*30)
            question = self.question_list.pop(random.randint(0, len(self.question_list)-1))
            print(f"Category: {question.category}")
            print(f"Question: {question.question}")
            ans = self.get_answer()
            if ans == question.answer:
                print(bcolors.OKGREEN + 'Correct!' + question.description + bcolors.ENDC)
                input()
            else:
                print(bcolors.FAIL + 'Wrong! ' + question.description + bcolors.ENDC)
                # print("Game over.")
                input()
                # break
            os.system('clear')
        os.system('clear')
         
    
