---
description: >-
  В этой статье мы узнаем, как настроить сценарий так, чтобы он работал только в
  личных сообщениях или в беседе
---

# Где сработал бот — %realm%

## Специальная переменная %realm%

Smartbot Pro предоставляет возможность определить, где пишет пользователь, с помощью специальной переменной %realm%.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Ff52OfumXDWf1etntRmOC%2Fimage.png?alt=media&#x26;token=33459f4d-8da3-4ef3-b0b5-a1e9be4118d7" alt=""><figcaption></figcaption></figure>

Эта переменная может принимать следующие значения:

* bot — если пользователь пишет в ЛС
* chat — если какое-либо событие произошло в групповом чате, в котором бот имеет доступ к сообщениям (помимо сообщений пользователя, бот также может видеть фиксировать, какие пользователи присоединились или покинули чат, и не только)
* comments — если пользователь написал в комментариях

## Только в лс

Чтобы бот отреагировал на действие пользователя, нужно выбрать нужный блок в разделе «События»:

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FmyH3ypvyECU8hFsWdoBs%2Fimage.png?alt=media&#x26;token=79ec98ef-74a9-4f55-a440-9ec634ffadc1" alt="" width="275"><figcaption></figcaption></figure>

Допустим, мы хотим, чтобы бот реагировал на первое событие пользователя только в лс (то есть, чтобы не спамил, когда к групповому чату присоединяется новый человек).

Для этого мы:

1. Выбираем событие «Первое сообщение и старт бота».
2. В нём нажимаем на кнопку «+ Условие на переменную».

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FUEXUn2sIzjzgk1NezFME%2Fimage.png?alt=media&#x26;token=65e011af-4f38-4d4f-9e88-2c3dba122ca7" alt="" width="322"><figcaption></figcaption></figure>

3. В названии переменной пишем «где»:

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FVylaWOyLvzlxyfuqFQ0D%2Fimage.png?alt=media&#x26;token=555d6b87-3e75-4ba9-a927-8141f00a1eec" alt="" width="321"><figcaption></figcaption></figure>

4. Выбираем нужную переменную.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FpfdGaVVCLDgehmIM0hdM%2Fimage.png?alt=media&#x26;token=43694b03-4187-4c2d-9284-89f059fcbcdf" alt="" width="320"><figcaption></figcaption></figure>

5. Убеждаемся, что выбран вариант «ЛС».
6. Создаём блок приветствия, соединяем его с созданным событием и публикуем сценарий.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FmL8CKEKzDIjovfN6ylA2%2Fimage.png?alt=media&#x26;token=cb1e2e69-fa7e-4c69-b550-630930e60c58" alt=""><figcaption></figcaption></figure>

## Только в групповых чатах

Чтобы бот реагировал на действие пользователей только в групповом чате, нужно выбрать подходящий блок в разделе «События» — например, реакцию на конкретное сообщение. Допустим, мы хотим, чтобы бот отвечал на приветствия пользователей.

Для этого мы:

1. Выбираем событие «Сообщение от пользователя».

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FMYni51tPaCizRJxO3vX5%2Fimage.png?alt=media&#x26;token=e620571d-a6c9-427c-8627-54756238f3d2" alt="" width="271"><figcaption></figcaption></figure>

2. В поле «Введите сообщение» пишем «Привет» и нажимаем кнопку «+ Условие на переменную».

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FbyHwpfRV1atu6nDqRAm4%2Fimage.png?alt=media&#x26;token=2db3747f-07ea-4609-96fd-a14d09b6dba5" alt=""><figcaption></figcaption></figure>

3. В названии переменной пишем «где» и выбираем переменную %realm%.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F5FJdk45hFN9do6WfO6ik%2Fimage.png?alt=media&#x26;token=2c5f3ff5-63e7-4cf3-bbdc-70c9d72f7540" alt=""><figcaption></figcaption></figure>

4. Выбираем вариант «Беседа».

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FJDBY4Kbgg5ZIgRxOdPTD%2Fimage.png?alt=media&#x26;token=213c019c-c125-4278-bada-d22741a19522" alt=""><figcaption></figcaption></figure>

5. Создаём нужное сообщение, соединяем с созданным событием и публикуем сценарий.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FmwB1WnbwRGqiSvtJDSC6%2Fimage.png?alt=media&#x26;token=a913a528-56a8-4ced-9700-89d2bac899a8" alt=""><figcaption></figcaption></figure>

## Только в бизнес аккаунте Telegram

По аналогии с настройкой чат-бота таким образом, чтобы он отвечал только в ЛС бота или в групповых чатах, можно настроить и так, чтобы он отвечал только в ЛС бизнес аккаунта.

Для этого нам достаточно передать переменной %realm% значение «Бизнес аккаунт», после чего бот будет работать только в этом режиме.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FCVgnfiNJdOukijZljyA0%2Fimage.png?alt=media&#x26;token=b30c4085-70ee-40b8-ac1a-9a42c21d5668" alt=""><figcaption></figcaption></figure>

Подробнее о Telegram Business вы можете прочитать в [этой статье](https://docs.smartbotpro.ru/nachalo-raboty/kak-podklyuchit-messendzher/podklyuchenie-telegram/podklyuchenie-telegram-business).

{% note info %}

Готово! Теперь вы можете настраивать ботов так, чтобы они работали там, где вам нужно :)

{% endnote %}
