import os
import logging
import sys
import dill
import pandas as pd
import json
from datetime import datetime
from sklearn.pipeline import Pipeline

# 1 ШАГ - прописать пути
path = os.path.expanduser('~/PycharmProjects/33homework')
os.environ['PROJECT_PATH'] = path
sys.path.insert(0, path)
#path = os.environ.get('PROJECT_PATH', '.')

# 2ШАГ - функция загружает обученную модель
def get_latest_model() -> Pipeline:
    latest_model = sorted(os.listdir(f'{path}/data/models'))[-1]     #имя файла последней версии модели
    with open(f'{path}/data/models/{latest_model}', 'rb') as file:   #открываем файл последней версии модели для чтения в бинарном режиме
        model = dill.load(file)                                      #загружаем объект модели из файла с помощью модуля dill
    return model

# 3ШАГ - функция делает предсказания для всех объектов в папке data/test (тестовые данные)
def get_predicts() -> pd.DataFrame:

    preds = {'car_id':[], 'pred':[]}                                 # создаем словарь, который будет содержать предсказания для каждой тестовой машины
    test_car = os.listdir(f'{path}/data/test')                      # получаем список имен файлов с тестовыми данными
    model = get_latest_model()                                      # получаем последнюю версию модели
    for car_id in test_car:                                         # перебираем все тестовые машины
        with open(f'{path}/data/test/{car_id}', 'rb') as file:      # открываем файл с тестовыми данными для чтения в бинарном режиме
            car = json.load(file)                                   #  загружаем данные из файла в формате JSON
        df = pd.DataFrame(car, index=[0])                       # создаем df из загруженных данных
        y = model.predict(df)                                   # делаем предсказание
        preds['car_id'].append(car_id.split('.')[0])            # добавляем предсказание в словарь
        preds['pred'].append(y[0])
    return pd.DataFrame(preds)                                      # преобразуем словарь с предсказаниями в df и возвращаем


# 3ШАГ - функция объединяет предсказания в один Dataframe и сохраняет их в csv-формате в папку data/predictions.
def predict() ->None:
    predictions = get_predicts()                                        # получаем предсказания для всех машин в тестовом наборе
    preds_filename = f'{path}/data/predictions/preds_{datetime.now().strftime("%Y%m%d%H%M")}.csv' # генерируем имя файла для сохранения предсказаний, включая дату и время
    predictions.to_csv(preds_filename, index=False)                     # записываем предсказания в CSV - файл
    logging.info(f'Model is saved as {preds_filename}')                         #выводим сообщение о том, что предсказания сохранены в файле

if __name__ == '__main__':
    predict()