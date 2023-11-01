import requests
import json
import time
import os
import webbrowser
import pyautogui
from rich import print


def get_vacancy_data(page=0, job_title='', area=1):
    params = {
        'text': f'NAME:{job_title}',
        'area': area,
        'page': page,
        'per_page': 100,
        'schedule': 'remote'
    }

    response = requests.get('https://api.hh.ru/vacancies', params)
    data = response.content.decode()
    response.close()
    return data

job_titles = ['Python Developer']
regions = [113]

for region in regions:
    for job_title in job_titles:
        for page in range(0, 20):
            print(f"Запрос вакансий: Регион: {region}, Должность: {job_title}, Страница: {page}")
            vacancy_data = json.loads(get_vacancy_data(page, job_title, region))
            next_file_name = 'C:\\Temp\\hh\\{}.json'.format(len(os.listdir("C:\\Temp\\hh")))
            with open(next_file_name, mode='w', encoding='utf8') as file:
                file.write(json.dumps(vacancy_data, ensure_ascii=False))

            if (vacancy_data['pages'] - page) <= 1:
                break
            print(f"Сохранено в файл: {next_file_name}")
            time.sleep(0.25)

print('======================== Получил список вакансий ========================')

for file_name in os.listdir('C:\\Temp\\hh'):
    with open('C:\\Temp\\hh\\{}'.format(file_name), encoding='utf8') as file:
        json_text = file.read()

    vacancy_data = json.loads(json_text)

    for vacancy in vacancy_data['items']:
        employer_name = vacancy['employer']['name']
        if employer_name not in ["Инсофт", "Yandex", "INSOFT", "ЭР-Телеком"]:
            response_url = vacancy['apply_alternate_url']
            webbrowser.open(response_url)
            time.sleep(4)
            pyautogui.hotkey('ctrl', 'w')
            print(f"Открыта страница отклика для вакансии от работодателя: {employer_name}")
            time.sleep(0.5)

print('Отклики закончил')
