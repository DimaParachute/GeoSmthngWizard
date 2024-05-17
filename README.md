# Проект по преддипломной практике "Управление геопространственной базой данных"

## Задача

### Серверная часть.
* python и django/geodjango
* База данных - PostgreSQL/PostGIS
* Для проектирования API необходимо использовать Django Rest Framework, ограничений на использование других пакетов нет
* Создать приложение, в котором будут следующие модели:
    Страна:
        - название
        - координаты
    Город:
        - название
        - описание
        - фотографии
        - координаты
    Столица:
        - название
        - координаты
* Координаты хранить в форматах GeoDjango
* Организовать связь между моделями
* Подключить стандартную django-admin-панель
* endpoint для получения, создания, изменения, удаления данных из всех моделей. Для координат использовать GeoJson
* Добавить фильтры для нахождения всех объектов внутри области, заданной 4-мя координатами (Bbox)

## Развертка проекта

```
$ docker-compose up --build
```