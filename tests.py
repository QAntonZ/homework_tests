import pytest
from createfolderyandex import create_folder
from http.client import responses
import requests
import json


from основы_языка_программирования import check_age, check_triangle, fio

age_params = (
    (4, 'Доступ запрещён'),
    (17, 'Доступ запрещён'),
    (22, 'Доступ разрешён')
)

@pytest.mark.parametrize(
    'x,expected',
    age_params
)
def test_age(x,expected):
    assert check_age(x) == expected


triangle_params = (
    (10, 10, 10, 'Равносторонний треугольник'),
    (10, 10, 14, 'Равнобедренный треугольник'),
    (10, 11, 12, 'Разносторонний треугольник'),
    (10, 20, 30,'Треугольник не существует'),
    (0, 10, 10,'Треугольник не существует'),
)

@pytest.mark.parametrize(
    'x, y, z, expected',
    triangle_params
)
def test_triangle(x, y, z,expected):
    assert check_triangle(x, y, z) == expected


fio_params = (
    (['Гагарин', 'Юрий', 'Алексеевич'], 'ГЮА'),
    (['Бисмарк', 'Отто', 'фон'], "БОф")
)

@pytest.mark.parametrize(
    'x,expected',
    fio_params
)
def test_fio(x,expected):
    assert fio(x) == expected

create_folder_params = (
    ("at_MKOsUlxPf7IlnW7kXOP3oyId37LWk", "https://cloud-api.yandex.net/v1/disk/resources", 201),
    ("at_MKOsUlxPf7IlnW7kXOP3oyId37LWk", "https://cloud-api.yandex.net/v1/disk/resources", 409)
)

@pytest.mark.parametrize(
    'key, url, expected',
    create_folder_params
)
def test_crate_folder(key, url, expected):
    assert create_folder(key, url) == expected