# Обрезка ссылок с помощью Битли

Позволяет обрезать сслки с помощью Битли.
В командную строку обязательным аргументом подаётся ссылка на сайт.
Если это не обрезанная сылка то программа, сделав запрос на битли выдаст обрезаннуюссылку.
Если это короткая ссылка то программа выдаст колличество переходов по этой ссылке(в данный момент не работает).
В случае если текст не является ссылкой выведется сообщение 'Неправильная ссылка'.

### Как установить

Для работы программы необходимо указать ключ от сайта bitly.com. Вкладка API в настройках. Access token.
Ключи для сайта должны быть прописаны в файле .env. Файл должен находится в одной дирректории с программой
Записан ключ должен быть следующим образом: BITLY_TOKEN={Ваш ключ}

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).