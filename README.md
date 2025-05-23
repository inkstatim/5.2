# Автотесты Sauce Demo на Playwright

тесты для сайта Sauce Demo с использованием Python и Playwright.

## Требования

- Python 3.10+
- Playwright

## Установка

1. Клонируйте репозиторий
2. Установите зависимости:
```
pip install -r requirements.txt
```
3. Установите браузеры Playwright:
```
playwright install
```

## Запуск тестов

Все тесты::
```
pytest
```

Конкретный тест:
```
pytest tests/test_order_flow.py
pytest tests/test_logout.py
```

## Структура проекта

- `conftest.py`
- `pages/` 
  - `base_page.py`
  - `login_page.py` 
  - `products_page.py`
  - `cart_page.py` 
  - `checkout_info_page.py`
  - `checkout_overview_page.py`
  - `checkout_complete_page.py` 
- `tests/` 
  - `test_order_flow.py`
  - `test_logout.py`

