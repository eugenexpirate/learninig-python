from bs4 import BeautifulSoup
import requests
import csv


quiz_url = "https://opentdb.com/browse.php?page="

api = requests.get(quiz_url)
soup = BeautifulSoup(api.text, 'lxml')


categories = soup.find_all("h2", style="font-family:lato;font-weight:bold;")

category_quantity = [16, 30, 42, 52, 64, 73, 84, 100]
category_text = []
category_counter = 0
for cat in categories:
    category_text.append(cat.get_text())


questions = []
for li in soup.find('table').find_all('li'):
    questions.append(li.get_text())

full_answers = []
answers = []
for p in soup.find('table').find_all('p', style="margin-left: 40px;"):
    full_answers.append(p.get_text())
    if p.strong.get_text().strip() == 'True':
        answers.append(True)
    else:
        answers.append(False)

with open("quiz.csv", mode="w") as quiz_file:
    writer = csv.writer(quiz_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i in range(0, 100):
        cat = ''
        for j in range(0, len(category_quantity)):
            if i <= category_quantity[j]:
                cat = category_text[j]
                break
        writer.writerow([cat, questions[i], answers[i], full_answers[i]])
    



