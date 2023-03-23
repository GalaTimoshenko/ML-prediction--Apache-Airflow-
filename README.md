# ML-prediction--Apache-Airflow-
## Make ML prediction -> load it to server so everyone can run it
Как я поняла, что не хочу быть Data Engineer, а хочу больше на ML Engineer сконцентрироваться a.k.a мой опыт работы с DAGs, Apache Airflow, загрузки модели на сервер, контейнеризация. 
### Задача:
#### а) обучить модель, запустить расчет локально 
#### б) запустить модель на сервер Apache Airflow
### Решение:
#### а) написать код: 
  -pipeline.py (состоит из ф-й filter_data-удалить ненужные колонки из данных, remove_outliers-удалить аномальные значения, create_features - сгенерить фичи, pipeline - запуск конвейера работы с данными - преобразование данных, расчет ML моделей LogisticRegression, RandomForestClassifier, SVC, выбор лучшей модели, формирование pickle файла),
  -predict.py (),
  -hw_dag.py 
 #### б) запустить расчеты локально в PyCharm
 ![Screenshot from 2023-03-23 15-35-45](https://user-images.githubusercontent.com/104129537/227206478-a55e192c-5cfa-4acb-bd7b-ddff83296cb1.png)
####  в) запустить расчеты на сервер Apache Airflow
![Screenshot from 2023-03-22 17-02-30](https://user-images.githubusercontent.com/104129537/227206997-34eeeb92-e85c-4891-a7f5-cc3ce6deace3.png)
![Screenshot from 2023-03-22 16-54-18](https://user-images.githubusercontent.com/104129537/227207125-2d414887-f9ab-4276-9aa2-16eb91d673fa.png)


## Проблемы, с которыми я столкнулась
### 1) broken DAG
![Screenshot_from_2023-03-02_15-57-32](https://user-images.githubusercontent.com/104129537/227208166-198246c0-08eb-4724-83e2-92f343480858.png)

### Решение Проблемы. 
запуск на расчет модели predict, pipeline и hw_dag уже не из PyCharm консоли, а из термин окна (сис-ма Linux Ubuntu), ВАЖНО! чтобы было нужное окружение (1-ое это окружение, где лежит Pycharm проект, второе, где развернут AIrflow) 
![Screenshot from 2023-03-23 15-51-26](https://user-images.githubusercontent.com/104129537/227209965-3b1c07c4-d014-4ba9-92ac-2d2e88299a5e.png)

### 2) Unit файл потерял Airflow, failed to load env 
![Screenshot from 2023-03-20 16-18-03](https://user-images.githubusercontent.com/104129537/227212870-c919a6a2-4ed6-481d-bf9a-f809a6da32c1.png)
![Screenshot_from_2023-03-20_16-25-19](https://user-images.githubusercontent.com/104129537/227213019-2678672e-da67-4c00-955f-358a38a5e8b4.png)

### Решение Проблемы. 
прописала нужный файл для airflow-webserver.service, airflow-scheduler.service, нужный путь узнается командной which airflow, строчка в ExecStart была неверно заполнена.
![Screenshot from 2023-03-20 17-33-16](https://user-images.githubusercontent.com/104129537/227213933-91487aff-1235-4a7d-b777-38fb0d0146db.png)


## Послесловие
Airflow  даже на убунту - это какой-то танец с бубном. 
Бубен кстати тоже был
![ds](https://user-images.githubusercontent.com/104129537/227214264-3b062823-25fd-4653-b2c9-023e2cd61f1f.jpg)

всем добра, любви и солнышка!


