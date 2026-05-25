---
description: >-
  Из этой статьи вы узнаете, как привязать Telegram бота к Business аккаунту,
  чтобы он мог обрабатывать в нём личные сообщения.
---

# Подключение Telegram Business

{% note tip %}

31 марта 2024 года Telegram выпустил шикарное обновление — возможность привязать чат-бота к бизнес аккаунту и вверить общение с клиентами боту не только в режиме бота, но и когда пользователи пишут на привычный всем Telegram аккаунт.

По сути это — аналог WhatsApp Business, который:

* легко подключить
* легко настроить
* легко использовать

Подробнее об этом обновлении вы можете прочитать прямо [на сайте Telegram](https://telegram.org/blog/telegram-business/ru?ln=a).

{% endnote %}

Обратите внимание, что подключение Telegram Business на данный момент доступно только для пользователей Telegram Premium. Позже это может измениться.

## Создание бота и подключение бота к Smartbot&#x20;

Если бот еще не создан, делаем это через BotFather и подключаем созданного бота к Smartbot Pro, согласно [инструкции](https://docs.smartbotpro.ru/nachalo-raboty/kak-podklyuchit-messendzher/podklyuchenie-telegram).&#x20;

## Подключение Telegram Premium

1.  Отправляем боту [@PremiumBot](https://t.me/PremiumBot) команду `/start`

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FpmJwFLwPBuind4vQvFUE%2Fimage.png?alt=media&#x26;token=9abdd76a-e455-4b68-8e27-099f9dd4fb0e" alt=""><figcaption></figcaption></figure>
2. Выбираем срок, на который хотим оплатить Telegram Premium
3. Оплачиваем \
   P.S. Карты РФ к оплате принимаются, но могут быть трудности. Например, если вы используете iPhone, то нужно  оплатить с компьютера. О нюансах оплаты картами РФ много статей в интернетах, нам помогла [вот эта инструкция](https://gogov.ru/news/890389).

## Настройка чат-бота в BotFather

{% note info %}

В боте предварительно нужно включить бизнес-режим для возможности добавления его как ассистента в личных сообщениях

{% endnote %}

1. Переходим в [@BotFather](https://t.me/BotFather)
2.  Нажимаем `/mybots` и выбираем нужного бота

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FMVSBbTxTrrFwrrHnzWuJ%2Fimage.png?alt=media&#x26;token=c8a5fba7-54d7-40e7-b49b-020454235549" alt=""><figcaption></figcaption></figure>
3.  Нажимаем Bot Settings

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FrjLzH6Nc5nDUJX5h4ejk%2Fimage.png?alt=media&#x26;token=b8c8bc7b-c970-40c0-96ce-9ed1fd635592" alt=""><figcaption></figcaption></figure>
4.  Нажимаем Business Mode

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FKVRPzb8A0baRccBGMKu3%2Fimage.png?alt=media&#x26;token=b2c7d74f-fae6-4c7f-9b2d-a4c63b9a6009" alt=""><figcaption></figcaption></figure>
5.  Нажимаем `Turn On`

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fo5zMjPkvJ5SaDygyda0I%2Fimage.png?alt=media&#x26;token=55ec35d0-b670-48cb-bae9-32932a418d8a" alt=""><figcaption></figcaption></figure>
6.  Копируем юзернейм бота и двигаемся дальше

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FRkoLtvqYYAwFhswSyGhY%2Fimage.png?alt=media&#x26;token=176294fc-8ab9-4867-ba15-4bf8d2a9b472" alt=""><figcaption></figcaption></figure>

## Подключение Telegram Business

1. _**Обязательно**_ обновляем Telegram до последней версии (лучше на всех устройствах)
2.  Переходим в настройки аккаунта

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F2RqttDGTEb3Bm2GhWbty%2Fimage.png?alt=media&#x26;token=99145a0e-9ce0-423a-a011-884e56cd320f" alt="" width="338"><figcaption></figcaption></figure>
3. Листаем вниз до Telegram для бизнеса

{% note info %}

Если у вас этот раздел не появился, то рекомендуем ещё раз проверить все обновления, перезагрузить устройство или открыть Telegram на другом устройстве — вероятно, функция пока находится в Beta-режиме Telegram и не всегда отображается сразу.

{% endnote %}

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FVYjUGcYDu4I05qRJcLVX%2Fimage.png?alt=media&#x26;token=c9537e6d-7890-4e92-874d-6e39967922a7" alt="" width="338"><figcaption></figcaption></figure>

4.  Переходим в раздел «Чат-боты»

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FsCZS6QY0LxBpnrpwoPC8%2Fimage.png?alt=media&#x26;token=b7daedd9-4730-4398-93af-d83603584c2d" alt="" width="375"><figcaption></figcaption></figure>
5.  В поле «@имя бота» пишем юзернейм нашего бота

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F3MdgHlfU3ckl8kU7wOLH%2Fimage.png?alt=media&#x26;token=ad5f0d12-37df-4bd0-a836-e4fb44f5a12f" alt="" width="375"><figcaption></figcaption></figure>
6.  Нажимаем «Добавить»

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F8KzMPz071xQPfLdDvepQ%2Fimage.png?alt=media&#x26;token=9b516c09-fc62-49b5-adef-c34b600cb566" alt="" width="375"><figcaption></figcaption></figure>
7.  Нажимаем «Готово»

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FLXhWq9nOk4W1ii5oNLD2%2Fimage.png?alt=media&#x26;token=9fb6015f-6330-419f-9dd8-64c38e630992" alt="" width="375"><figcaption></figcaption></figure>

>
>
> _**Отлично! Идём настраивать логику бизнес-бота в Smartbot Pro**_ 😎<br>

{% note tip %}

_**Отлично! Теперь все сценарии проекта, к которому подключен бот, будет работать в лс бота и в бизнес-аккаунте**_ 😎 \
&#xNAN;_&#x414;алее расскажем, как настроить логику работать бота отдельно для бизнес аккаунта, а также о работе с пользователями и диалогами из этого чата._&#x20;

{% endnote %}

## Работа в Smartbot Pro

### Настройка сценария

Чтобы бот отвечал (или **не** отвечал) на сообщения, который приходят в Business аккаунт Telegram, достаточно настроить нужные значения переменной %realm% («Где сработал бот») в событии или условии, в зависимости от ваших потребностей.

1.  Например, в таком случае бот запустит сценарий только при первом сообщении в бизнес аккаунт:

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FYRsYUlTeKNL96n4nZNth%2Fimage.png?alt=media&#x26;token=821d7d16-a933-43ef-b1b4-cbf74bf145bf" alt="" width="375"><figcaption><p>Настройки реакции на первое сообщение в Telegram бизнес </p></figcaption></figure>
2.  А в этом случае, наоборот, бот будет запускать сценарий во всех сущностях (лс, групповые чаты и комментарии), но именно в бизнес аккаунте работать не будет

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fop4LXyq9z5s67mN4RuRO%2Fimage.png?alt=media&#x26;token=2effa648-027d-4cc8-87b6-5966b1de3eb9" alt="" width="375"><figcaption><p>Как отключить реакцию на первое сообщение в бизнес аккаунте</p></figcaption></figure>

### Раздел «Пользователи»

Чтобы посмотреть данные по пользователю в различных чатах бота (например, при его общении напрямую с ботом и через Telegram Business), вы можете выбрать бизнес аккаунт в меню «Чат» — например, для отслеживания эффективности воронки или для других задач.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FfGDoX7wD4xNzfiUky5oj%2Fimage.png?alt=media&#x26;token=3a14c6df-e22f-4964-b99c-c9aa6461f3b2" alt=""><figcaption><p>Так вы можете видеть значения переменных, сохранённых при общении пользователя с ботом в ЛС бота</p></figcaption></figure>

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FyrKDrSNQh8wEzgEXSS4s%2Fimage.png?alt=media&#x26;token=cbab0657-8d92-45b6-91ab-dac77112803e" alt=""><figcaption><p>А так вы можете видеть значения переменных, сохранённых при общении пользователя с бизнес аккаунтом</p></figcaption></figure>

### Раздел «Чаты»

А вот чаты с пользователями вы в Смартботе не увидите по следующим причинам:

* помимо использования Telegram Business по его прямому назначению — в бизнесе — вы можете подключить бота к своему личному аккаунту, чтобы он был вашим персональным ассистентом, и тогда бот сможет видеть и ваши личные сообщения, которые далеко не каждый готов будет транслировать в проект, где могут работать и другие менеджеры
*   Telegram Business прекрасен тем, что теперь вы можете самостоятельно отслеживать чаты так, как вам удобно. Например, вы можете создать личный аккаунт для технической поддержки и позволить сотрудникам залогиниться в нём, чтобы они также отслеживали переписки с пользователями помимо бота.

    И тогда вы самостоятельно сможете совершенно удобно распределять пользователей по папкам, присваивать им теги (ещё одна удобная фича Telegram Business) и отслеживать, что пишут пользователи, не покидая Telegram, о чём многие так мечтали 🔥

### Раздел «Рассылки»

Ещё один раздел, где пока Telegram Business вы не увидите, но это может измениться с обновлением Telegram, которое, мы надеемся, не заставит себя ждать. Дело в том, что сейчас вы не сможете ничего отправить пользователю, если ни вы, ни ваш собеседник не общались в чате более 24 часов.

В отличие от WhatsApp Business (WABA) или Viber, которые позволяют рассылать сообщения пользователям спустя сутки молчания за отдельную плату, в Telegram такой функционал пока в принципе не реализован. Будем вместе следить за обновлениями.

{% note tip %}

Мы желаем вам приятного, удобного и комфортного пользования чат-ботами с Telegram Business 🙏 Удачи!

{% endnote %}
