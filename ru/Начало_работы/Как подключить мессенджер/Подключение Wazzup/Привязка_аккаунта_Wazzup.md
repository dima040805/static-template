---
description: >-
  В этой статье рассмотрим, как привязать аккаунт Wazzup к Smartbot Pro и какие
  есть особенности.
---

# Привязка аккаунта Wazzup

{% note info %}

**Важно**: привязать аккаунт не получится, если у вас пусто на балансе и закончился пробный период

{% endnote %}

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F9SQnhfuEj7eoqz2YBhxb%2Fimage.png?alt=media&#x26;token=42186dec-7fff-4a0e-ba34-0d5f889f546e" alt=""><figcaption></figcaption></figure>

Для тестирования сценария необходимо привязать свой аккаунт социальной сети.&#x20;

\
Т.к. Wazzup - платформа для подключения разных типов каналов, есть особенность при привязке аккаунта.&#x20;

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FQzOw9vj4g4a4aEBF2hDr%2Fimage.png?alt=media&#x26;token=5d2e98e8-96b1-4994-b49f-833d3ca6f96c" alt=""><figcaption></figcaption></figure>

Если в Wazzup у вас подключены разные типы каналов (Telegram, Instagram, WhatsApp, Вконтакте), то, как только вы получили команду для привязки аккаунта Wazzup (как ее получить - смотрите в статье "[Привязка аккаунта социальной сети](https://docs.smartbotpro.ru/nachalo-raboty/kak-podklyuchit-messendzher/privyazka-akkaunta-v-socialnoi-seti)"), для проверки работы поочередно отправляйте команду в каждый из типов каналов.&#x20;

{% note info %}

Почему так? В каждой соц. сети/мессенджере один и тот же человек (в данном случае - вы, как админ проекта) будет восприниматься ботом как разные пользователи. С помощью команды для привязки аккаунта бот сможет отличить ваш аккаунт в выбранной для теста соц. сети или мессенджере, и "отметить как админа.&#x20;

{% endnote %}

**Рассмотрим пример** - в моем кабинете Wazzup подключены несколько каналов: WhatsApp, Telegram Bot и Вконтакте. Аккаунт Wazzup в Smartbot Pro еще не привязан, но я хочу протестировать неопубликованную версию сценария с отладкой в каждом из каналов.

Сначала нужно получить токен для привязки аккаунта, для этого я нажимаю на кнопку "Привязать", это можно сделать из 2х мест: \
а) напротив Wazzup в настройках через сценарий, когда нажимаю "Тестировать" с конкретного блока\
б) через настройки профиля

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F9zTNsqfwizOYP8GxOaN4%2Fimage.png?alt=media&#x26;token=fab7afb1-08ff-4069-a97f-6490127e4804" alt="" width="563"><figcaption><p>Получение токена через сценарий</p></figcaption></figure>

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FGKAcpJtuTymh11NLAHxM%2Fimage.png?alt=media&#x26;token=04030396-a964-42f4-aeed-7f3c5c29e874" alt="" width="563"><figcaption><p>Получение токена через настройки профиля</p></figcaption></figure>

Для начала хочу протестировать WhatsApp, поэтому токен для привязки отправляю туда.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fk4170CCeGF1liDTPSCgJ%2Fimage.png?alt=media&#x26;token=34a12392-3478-4d79-9c50-a68640e57a14" alt="" width="563"><figcaption></figcaption></figure>

Теперь в WhatsApp я могу проверять сценарий, как администратор - работать с неопубликованной версией сценария, запускать сценарий с конкретного блока и видеть отладку!

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FHlIOQC0krBrT4gOA0O9R%2Fimage.png?alt=media&#x26;token=7abfa064-c992-4a2d-9bbc-d3aa40c06428" alt="" width="563"><figcaption></figcaption></figure>

WhatsApp протестирован, в работе сценария нет сомнений, теперь хочу посмотреть Вконтакте. Для этого я захожу в настройки профиля, отвязываю аккаунт Wazzup. \
\
заново получаю токен по кнопке "Привязать" и отправляю его уже в группу Вконтакте.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FsWG1RtNUvLTLwlPJ3DEU%2Fimage.png?alt=media&#x26;token=e804b4bd-d9ac-4e2f-8e90-f9dccccf6762" alt="" width="563"><figcaption><p>Привязка аккаунта в вк и после запуск с конкретного блока</p></figcaption></figure>

После окончания тестирования выполняются те же действия:

1. Отвязать аккаунт Wazzup в настройках профиля
2. Получить токен для привязки
3. Отправить в другой **тип** канала

{% note tip %}

На этом все! Мы успешно разобрались, как подключать аккаунт, чтобы иметь возможность тестировать сценарии в Wazzup в полном объеме!&#x20;

{% endnote %}
