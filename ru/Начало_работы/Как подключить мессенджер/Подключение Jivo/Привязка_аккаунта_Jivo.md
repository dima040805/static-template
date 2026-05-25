---
description: >-
  В этой статье рассмотрим, как привязать аккаунт Jivo к Smartbot Pro и какие
  есть особенности.
---

# Привязка аккаунта Jivo

Для тестирования сценария необходимо привязать свой аккаунт социальной сети.&#x20;

{% note info %}

**Важно**: привязать аккаунт не получится, если у вас пусто на балансе и закончился пробный период

{% endnote %}

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F6NsxOY9fBS3J5idPKaUM%2Fimage.png?alt=media&#x26;token=2af0aa7e-e104-4058-a255-1ef4e3f27a8e" alt=""><figcaption></figcaption></figure>

\
Т.к. Jivo - платформа для подключения разных типов каналов, есть особенность при привязке аккаунта.&#x20;

Если в Jivo у вас подключены разные типы каналов (Telegram, Instagram, Вконтакте, Авито), то, как только вы получили команду для привязки аккаунта Jivo (как ее получить - смотрите в статье "[Привязка аккаунта социальной сети](https://docs.smartbotpro.ru/nachalo-raboty/kak-podklyuchit-messendzher/privyazka-akkaunta-v-socialnoi-seti)"), для проверки работы поочередно отправляйте команду в каждый из типов каналов.&#x20;

{% note info %}

Почему так? В каждой соц. сети/мессенджере один и тот же человек будет новым пользователем для бота. Он же с помощью команды для привязки аккаунта сможет отличить ваш аккаунт в выбранной для теста соц. сети или мессенджере.&#x20;

{% endnote %}

**Рассмотрим пример** - в моем кабинете Jivo подключены несколько каналов: Telegram Bot, Вконтакте, Авито. Аккаунт Jivo в Smartbot Pro еще не привязан, хочу протестировать неопубликованную версию сценария с отладкой в каждом из каналов.

Для этого я получаю команду для привязки (или токен) по нажатию на кнопку "Привязать" напротив Jivo либо через сценарий, когда нажимаю "Тестировать", либо через настройки профиля.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FxNHoJwntIpM8iFHPoKXX%2Fimage.png?alt=media&#x26;token=bfc58136-29e4-4746-ad75-eee805942b98" alt="" width="563"><figcaption><p>Получение токена через сценарий</p></figcaption></figure>

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FrPiDt3emq0esuMVEJZRc%2Fimage.png?alt=media&#x26;token=83aa2058-38d4-4320-bcc8-79973d10ab99" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FENmvNKMzuiyXXJhOHzL3%2Fimage.png?alt=media&#x26;token=51fe9db3-2049-41c9-abf8-bf14240cde03" alt=""><figcaption></figcaption></figure>

> Получение токена через настройки профиля



Для начала хочу протестировать Вконтакте, поэтому токен для привязки отправляю туда.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fee9s49cIaeEHplUL65ns%2Fimage.png?alt=media&#x26;token=6af815fa-6823-4dc7-8a6c-7db245c9f87f" alt=""><figcaption><p>Привязка аккаунта Jivo в Вк</p></figcaption></figure>

Теперь во Вконтакте я могу проверять сценарий, как администратор - работать с неопубликованной версией сценария, запускать сценарий с конкретного блока и видеть отладку!

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F2w8fdgbtNEyihkDjKHZ6%2Fimage.png?alt=media&#x26;token=ff467872-9ca0-445a-ba80-3feeb6aaa8bf" alt=""><figcaption><p>Привязка аккаунта и после запуск теста с блока</p></figcaption></figure>

Вконтакте протестирован, в работе сценария нет сомнений, теперь хочу посмотреть Telegram Bot. Для этого я захожу в настройки профиля, отвязываю аккаунт Jivo, заново получаю токен по кнопке "Привязать" и отправляю его уже в бота.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FHnjizsgscE4z9UcYbIvm%2Fimage.png?alt=media&#x26;token=f5e6f499-0c94-47ac-a42a-e1153e8e6b70" alt=""><figcaption><p>Привязка аккаунта Jivo в Telegram и после запуск теста с блока</p></figcaption></figure>

После окончания тестирования выполняются те же действия:

1. Отвязать аккаунт Jivo в настройках профиля
2. Получить токен для привязки
3. Отправить в другой **тип** канала

{% note tip %}

На этом все! Мы успешно разобрались, как подключать аккаунт, чтобы иметь возможность тестировать сценарии в Jivo в полном объеме!&#x20;

{% endnote %}
