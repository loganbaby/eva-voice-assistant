# Голосовой ассистент "Ева"
Искусственный интеллект, разрабатывающийся в целях автоматизации и облегчении повседневных задач. Главное его отличие от конкурентов - это новый режим обучения, который подразумевает под собой обычный разговор. Так голосового ассистента можно научить всему, что ты захочешь

## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Deploy и CI/CD](#deploy-и-ci/cd)
- [Contributing](#contributing)
- [We are looking for](#we-are-looking-for)
- [To do](#to-do)
- [Команда проекта](#команда-проекта)

## Технологии
- [Python3](https://www.python.org/downloads/release/python-3100/)
- [C++ 11](https://en.cppreference.com/w/cpp/17)
- [Qt 5.12.12](https://www.qt.io/offline-installers)
- [SpeachRecognition](https://pypi.org/project/SpeechRecognition/)

## Использование

Установите необходимые зависимости, чтобы запустить приложение:

Чтобы быстро установить необходимые зависимости, воспользуйтесь _requirements.txt_:
```sh
$ pip install -r requirements.txt
```

Для того, чтобы собрать простенькое графическое окружение для Евы, потребуется установить [Qt 5.12.12](https://www.qt.io/offline-installers), перейти в директорию _ui_ и затем запустить сборку проекта с помощью CMake:
```sh
$ cmake CMakeLists.txt
```
**ВНИМАНИЕ!** Если ваш сборщик будет ругаться на сборку проекта, то откройте файл _CMakeLists.txt_ и найдите строку:
```sh
set(CMAKE_PREFIX_PATH "")
```
Здесь нужно установить свой путь к установленному Qt фреймворку и компилятору
<br><br><hr>

Далее, сохраняем файл с названием _ui.exe_

Отлично! Окружение готово. Теперь перейдите в главную директорию проекта и запустите Еву:
```sh
$ python main.py
```

## User-Bot Eva
Изначально, Ева является не только голосовым ассистентом, но и _юзер-ботом_ для **_Telegram_**

Это обозначает, что в проекте есть 2 конфигурации программы. Запуск первой мы разобрали выше, сейчас мы запустим Еву в режиме **_User-Bot_**

Для этого, создаём приложение в [_Telegram App_](https://my.telegram.org/apps), как показано на картинке ниже:

![Image](https://github.com/loganbaby/eva-voice-assistant/blob/main/res/images/tg_app.png)

Копируем **_APP_ID_** и **_APP_HASH_**, вставляем в **_config/config.py_**

Запускаем:

```sh
$ python user_bot.py
```

## Разработка

### Требования
Для установки и запуска проекта, необходим [Python3](https://www.python.org/downloads/release/python-3100/) и [Qt 5.12.12](https://www.qt.io/offline-installers)

### Установка зависимостей
Для быстрой установки зависимостей, выполните _requirements.txt_:
```sh
$ pip install -r requirements.txt
```

## Deploy и CI/CD
Просто откройте приложение в консоли, как было описано выше. Окромя, ничего не надо!

## Contributing
Помочь в разработке проекта может каждый желающий! Делайте форки, используйте issues для составления грамотных баг-репортов.

Также можно обращаться ко мне в Telegram или во ВКонтакте за любой помощью и подсказками. Сделаем проект лучше!

- **_e-mail_** - shifo3456@gmail.com
- **_VK_** - [Дмитрий Котов](https://vk.com/logbaby)
- **_Telegram_** - [logbaby](https://t.me/logbaby)

## We are looking for
Для разработки проекта требуются следующие люди:
- Человек, озвучивающий "Еву"
- **_Python_** разработчики для создания и улучшения эвристик интеллекта
- **_Front-end_** разработчики

## FAQ 
- _Как запустить режим тренировки?_
- Очень просто. Безусловно, функция находится в активной разработке, но на данный момент ей всё же можно воспользоваться. Вам нужно сказать ассистенту "Давай потренируемся"

### Зачем вы разработали этот проект?
Чтобы был.

## To do
- [ ] Написать синтезатор речи
- [ ] Озвучить голосового ассистента
- [ ] Пересмотреть механику тренировки ИИ
- [x] Сделать скелет для юзер-бота
- [x] Улучшить эвристики для написания модулей юзер-бота

## Команда проекта

- [Дмитрий Котов](https://t.me/logbaby) — Owner // C++, Python developer 