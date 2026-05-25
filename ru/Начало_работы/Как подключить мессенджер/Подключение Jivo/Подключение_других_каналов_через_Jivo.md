---
description: >-
  В этой статье рассмотрим, какие каналы мы можем подключить с помощью Jivo к
  Smartbot Pro и с какими сложностями можно столкнуться.
---

# Подключение других каналов через Jivo

На данный момент список каналов, которые можно интегрировать со Smartbot Pro через Jivo такой:

1. WhatsApp\*
2. ВК
3. Телеграмм
4. Instagram\*
5. Viber
6. Facebook\*
7. Одноклассники
8. Aliexpress
9. Авито\*\*

**\***_соцсеть принадлежит компании Meta, признанной экстремистской и запрещенной на территории России_\
_\*\*возможно подключить, начиная с профессиональной версии (это один из тарифов Jivo)_

Ниже рассмотрим процесс подключения каждого из каналов.&#x20;

## WhatsApp&#x20;

1. Для подключения WhatsApp выберете его в списке каналов и нажмите "Добавить".

{% note info %}

После окончания демо-версии WhatsApp можно будет использовать только в профессиональной версии.

{% endnote %}

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FHsbXkH8d34xn1KuFHDz8%2Fimage.png?alt=media&#x26;token=89418a14-e3cc-4ca2-9b74-803074f6486c" alt="" width="563"><figcaption></figcaption></figure>

2. Вы перейдете на страницу выбора провайдера WhatsApp Business API. У каждого из них свои условия цены. Чтобы ознакомиться с ними, перейдите на [сайт Edna](https://edna.ru/whatsapp-business-api/) и [сайт Twilio](https://www.twilio.com/en-us/whatsapp/pricing).

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FqKxb5GgznrYADjHZ5wxl%2Fimage.png?alt=media&#x26;token=e3eb5e95-8dde-49ed-9908-d302e86d81ff" alt="" width="563"><figcaption><p>Страница выбора провайдера</p></figcaption></figure>

3. Далее вам нужно создать аккаунт через выбранного провайдера.&#x20;

* [Инструкция создания аккаунта через Edna](https://www.jivo.ru/help/whatsapp/connect-whatsapp-via-edna.html)
* [Инструкция создания аккаунта через Twilio](https://www.jivo.ru/help/whatsapp/connect-whatsapp-via-twilio.html)

4. Последним шагом подключаем ранее созданный аккаунт к Jivo.

* &#x20;Если выбрали Edna, то для подключения достаточно ввести название канала и номер телефона, который вы использовали для регистрации WhatsApp Business.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fse7RhFOCb99nghkuRMqu%2Fimage.png?alt=media&#x26;token=fe13a754-600b-4c3d-93c1-5807a2353966" alt="" width="317"><figcaption></figcaption></figure>

*   Если вы выбрали Twillo, то кроме названия канала и номера телефона вам нужно ввести:

    * &#x20;SID аккаунта Twillo - скопируйте из [личного кабинета Twilio](https://www.twilio.com/login), раздел Settings (Настройки) > General (Общие). Ваш SID расположен в поле "ACCOUNT SID";
    * авторизационный токен - скопируйте из [личного кабинета Twilio](https://www.twilio.com/login), раздел Settings (Настройки) > General (Общие). Ваш токен расположен в поле "AUTH TOKEN";

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fxx20KGri9tRfhVCho0xm%2Fimage.png?alt=media&#x26;token=5eeb65ee-fd28-4a7f-9150-b0dd5eb956a6" alt="" width="378"><figcaption></figcaption></figure>

    * После подключения канала вы увидите его в списке в Jivo в разделе "Управление" -> "Каналы связи"&#x20;
    * Перейдите в настройки канала WhatsApp, скопируйте Webhook URL, сгенерированный Jivo такого вида:

    `https://joint.jivosite.com/xxxxxxxxxxxxxxx/xxxxxxxxxxx`

    * После этого перейдите в ваш аккаунт Twilio, откройте настройки отправки сообщений (_Develop > Messaging > Senders > WhatsApp senders > Edit sender_) и вставьте скопированный URL в поле _"Webhook URL for incoming messages"_, затем сохраните изменения.

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FH2D9QOYgKR82uAlvlSdq%2Fimage.png?alt=media&#x26;token=cca85c16-9488-43af-9cc3-e6aa1189b486" alt="" width="563"><figcaption></figcaption></figure>

Настройка WhatsApp готова!

## Авито

1. В списке каналов найдите Авито и нажмите "Добавить".&#x20;

{% note info %}

После окончания демо-версии Авито можно будет использовать только в профессиональной версии.

{% endnote %}

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FXO3doCQYay0xo5NKEr3m%2Fimage.png?alt=media&#x26;token=d8fc2319-2614-4e45-976f-1e2000da53fd" alt="" width="563"><figcaption></figcaption></figure>

2. На открывшейся странице нажмите "Подключить".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fwqc77eZMqg3KpurW6YYI%2Fimage.png?alt=media&#x26;token=9cd7b209-799d-4f72-b178-c06715637059" alt="" width="563"><figcaption></figcaption></figure>

3. Авторизуйтесь в Авито или зарегистрируйтесь, если нет аккаунта.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fw4resLR9ieHGhU0D93XO%2Fimage.png?alt=media&#x26;token=a732623c-50ed-4b3e-9104-571b90a00953" alt="" width="563"><figcaption></figcaption></figure>

4. Выдайте Jivo разрешение на работу с сообщениями.

{% note info %}

В Авито есть понятие бизнес-аккаунтов, которые внутри содержат несколько профилей. Поэтому если ваш аккаунт относится к такому, при подключении помните, какой профиль вы выбрали и с какого из них у вас создано объявление.

{% endnote %}

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FYQ0XCE17QsxS5biOoqcC%2Fimage.png?alt=media&#x26;token=b9fec35a-45c4-460a-bab4-1bd3f82d5a96" alt="" width="342"><figcaption></figcaption></figure>

Готово! Интеграция подключена!

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FdSjsAlmsGGonTZSkWf61%2Fimage.png?alt=media&#x26;token=8d78cd61-c58b-4ad0-831c-ca619b9e6c50" alt="" width="512"><figcaption></figcaption></figure>

## Вконтакте

{% note info %}

Чтобы подключить группу ВК к Jivo, убедитесь, что вы являетесь ее администратором!

{% endnote %}

1. В разделе "Управление" -> "Каналы связи" выберете Вконтакте и нажмите "Добавить".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fh7fhew1ULUJWZdPvB05d%2Fimage.png?alt=media&#x26;token=df1d78f0-b577-464e-82c0-18059615aa82" alt="" width="563"><figcaption></figcaption></figure>

2. Нажмите кнопку "Подключить Вконтакте".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F2JpdUM9mRgvGWcGcVhXx%2Fimage.png?alt=media&#x26;token=9e1f2ee4-acd5-4505-ac6b-0ec40c634e80" alt="" width="563"><figcaption></figcaption></figure>

3. Нажмите на кнопку "Войти" и введите данные от вашего аккаунта Вконтакте, если авторизация не произойдёт автоматически.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FZtlhBoNn80ceFsKVO3iP%2Fimage.png?alt=media&#x26;token=6709d8a9-e3d7-4d71-8c79-3608e1853f10" alt="" width="563"><figcaption></figcaption></figure>

4. Выберите группу из списка и нажмите кнопку "Подключить".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fsjmesf280E9Vig1xo79n%2Fimage.png?alt=media&#x26;token=ce381f0c-8ac1-4053-a7da-027757680b82" alt="" width="563"><figcaption></figcaption></figure>

5. На открывшейся странице нужно будет разрешить доступ к аккаунту и группе. После этого ваша группа будет подключена.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F7IwcQK7wlhWjOK3aCsLk%2Fimage.png?alt=media&#x26;token=b54d20ce-7504-4e6a-bb3e-46a3d96511e6" alt="" width="563"><figcaption></figcaption></figure>

6. Последним шагом вам нужно будет разрешить отправку сообщений сообщества в настройках группы. Для этого перейдите в раздел "Управление".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FUZSDROIG0mBmpFTP1Ob8%2Fimage.png?alt=media&#x26;token=62141543-100b-4d13-ad30-99cdc6cb0e37" alt="" width="563"><figcaption></figcaption></figure>

7. На открывшейся странице выберите раздел "Сообщения" и сообщения сообщества должны быть включены.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fh2itdJwQ81wZg19RbxWw%2Fimage.png?alt=media&#x26;token=18f4cbbc-a286-4245-84be-d29acd8e1693" alt="" width="563"><figcaption></figcaption></figure>

Чтобы кнопка "Вконтакте" появилась в чате Jivo на мобильной версии вашего сайта, [включите Вконтакте в настройках омниканальности](https://www.jivo.ru/help/integrations/nastroika-omnikanalnosti.html).

{% note tip %}

Настройка Вконтакте завершена!

{% endnote %}

## Telegram

Для того, чтобы подключить Telegram Bot к Jivo, вы должны создать бота (если не знаешь как, смотри инструкцию по [ссылке](https://docs.smartbotpro.ru/nachalo-raboty/kak-podklyuchit-messendzher/podklyuchenie-telegram)) или использовать уже имеющегося.

{% note info %}

Важно: ваш бот не должен быть подключен в другие сервисы. Иначе корректного выполнения сценариев от него можно не ждать!

{% endnote %}

1. В разделе "Управление" -> "Каналы связи" найдите Telegram и нажмите "Добавить".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Firsrfdo50bYsTX8upFHZ%2Fimage.png?alt=media&#x26;token=6c5fc5b9-732b-482a-a34e-a0838aa45ae9" alt="" width="563"><figcaption></figcaption></figure>

2. Нажмите кнопку "Подключить Telegram".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FnitHAvRoFJ5H3oH7stwD%2Fimage.png?alt=media&#x26;token=1c4edc30-8e01-4759-9225-68fe7956b286" alt="" width="563"><figcaption></figcaption></figure>

3. Вставьте полученный ранее от BotFather ключ API в поле "Токен" и нажмите "Подключить Telegram".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FPnoaZE6C0zY5Fngbxi9c%2Fimage.png?alt=media&#x26;token=9a7e60d1-d697-4d8a-bdc3-a17123c92cb8" alt="" width="389"><figcaption></figcaption></figure>

4. После подключения откроется окно настроек канала.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F61PRZ9KIwysbtAuWVFem%2Fimage.png?alt=media&#x26;token=f86b3570-c162-4ee6-aba9-eddc553bc583" alt="" width="563"><figcaption></figcaption></figure>

Чтобы кнопка "Telegram" появилась в чате Jivo на вашем сайте, [включите Telegram в настройках омниканальности](https://www.jivo.ru/help/integrations/nastroika-omnikanalnosti.html).

{% note tip %}

На этом все, настройка Telegram завершена!

{% endnote %}

## Instagram*

Прежде чем подключать Instagram необходимо выполнить несколько требований:

* Ваша учетная запись Instagram должна быть подключена к странице Facebook.
* Вам необходимо настроить [бизнес-аккаунт Instagram](https://www.facebook.com/business/help/502981923235522) и подтвердить его.
* Выдать доступ к сообщениям в Instagram в настройках приложения

1. В приложении Jivo в разделе "Управление" -> "Каналы связи" найдите Instagram и нажмите на его иконку или на кнопку "Добавить".

{% note info %}

На этом этапе рекомендуем включить VPN для успешного подключения.

{% endnote %}

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FGCjriG9dGFpjW4rX2Io6%2Fimage.png?alt=media&#x26;token=2c9f3252-c5b5-46fe-916c-94c80538b7b4" alt="" width="563"><figcaption></figcaption></figure>

2. Следуйте всем инструкциям во всплывающем окне. Внимательно прочитайте и проверьте все руководства, предоставленные для каждого шага.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FuXmauFxl67VeophUNYw7%2Fimage.png?alt=media&#x26;token=52fe8a4e-9edf-4d92-802a-9b5a4221c2fb" alt="" width="563"><figcaption><p>Перевод аккаунта Inst на профессиональный</p></figcaption></figure>

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F5WPZzObU89zUuJDs5zuF%2Fimage.png?alt=media&#x26;token=62a6a312-322d-4e30-bb4f-c5aa26e16756" alt="" width="563"><figcaption><p>Подключение страницы Facebook</p></figcaption></figure>

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FPMPzs2Wb3H2CwLiKnOG0%2Fimage.png?alt=media&#x26;token=9f1c4a7e-e6c3-4b6e-a8ad-aeef4cbb1902" alt="" width="563"><figcaption><p>Выдача доступа к сообщениям</p></figcaption></figure>

3. После того, как проверите все этапы, вам нужно будет войти в свой аккаунт Facebook.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FXhu0CDsYooh0tFAGs8dy%2Fimage.png?alt=media&#x26;token=feccff93-a93b-4d68-98b9-b824608d01a7" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FP7K6qr2Pefzrbu9mzbrk%2Fimage.png?alt=media&#x26;token=e3f329fd-2f7d-498d-8315-94688c226ec8" alt="" width="558"><figcaption><p>Введите пароль и нажмите "Продолжить"</p></figcaption></figure>

4. Нажмите "Продолжить как (ваш аккаунт Facebook)".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FBfYjz5LfZX4eoKxb9tH9%2Fimage.png?alt=media&#x26;token=cbeba672-4c1e-4891-88ba-4edf989c8fcd" alt="" width="497"><figcaption></figcaption></figure>

5. Выберите учетную запись Instagram, которую вы хотите подключить:

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FUCG0WBmWAcHoljTUHqAJ%2Fimage.png?alt=media&#x26;token=74e6364b-66ec-45a7-9322-9cab6710ed42" alt="" width="513"><figcaption></figcaption></figure>

6. Вам также необходимо подключить страницу Facebook, подключенную к этой учетной записи:

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FR8Dj8MhUEBHJ2zDQms5Q%2Fimage.png?alt=media&#x26;token=fdfaac98-a182-422b-92da-639e208f92ba" alt="" width="506"><figcaption></figcaption></figure>

7. Вы попадете на страницу выдачи разрешений. Вам необходимо выдать только то, что указано на скриншоте (доступ к профилю и постам Инстаграм аккаунта, связанных с этой страницей, и управление и доступ к сообщениям Инстаграм аккаунта) и нажать кнопку "Done":

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FThTfZNfAfVqNs7xl5qZd%2Fimage.png?alt=media&#x26;token=8f4a1447-d5f5-4021-acb9-1af02d8c4b36" alt="" width="513"><figcaption></figcaption></figure>

8. На странице с сообщением об успешном подключении нажмите "Ок".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F3p871Tz1VK1swJRdyPYy%2Fimage.png?alt=media&#x26;token=ef4d3b36-0d39-492f-9f23-e900b6631d2f" alt="" width="507"><figcaption></figcaption></figure>

Готово! Instagram подключен к Jivo!

## Viber

Процесс подключения Viber аналогичный с Telegram - создать бота, используя его токен, подключить к Jivo. Если его нет, создать нового возможно будет только платно. Что для этого нужно сделать, можно узнать, например, по этой [ссылке](https://kb.pact.im/article/46345).&#x20;

1. Чтобы подключить уже имеющегося бота, зайдите в кабинет Jivo, найдите в списке каналов Viber и нажмите "Добавить".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Ff8Fu8j4zVOjjtJceJrRT%2Fimage.png?alt=media&#x26;token=024498b3-d37c-454e-bcf0-55463a4a4492" alt="" width="563"><figcaption></figcaption></figure>

2. Затем вставьте полученный ключ API в поле и нажмите "Подключить Viber". Найти ключ от своего бота вы можете в [панели администратора](https://partners.viber.com/).

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fo0W22zJdPM6TjPE7riyc%2Fimage.png?alt=media&#x26;token=8c05d567-ecfa-4588-96dd-42888b959f56" alt="" width="446"><figcaption></figcaption></figure>

Чтобы кнопка "Viber" появилась в чате Jivo на мобильной версии вашего сайта, [включите Viber в настройках омниканальности](https://www.jivo.ru/help/integrations/nastroika-omnikanalnosti.html).

Настройка Viber завершена!

## Facebook*

1. В списке каналов найдите Facebook и нажмите кнопку "Добавить".

{% note info %}

На этом этапе рекомендуем включить VPN для успешного подключения.

{% endnote %}

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FWLaAxYneorkMimflDRje%2Fimage.png?alt=media&#x26;token=1d057f73-e52e-4e09-94b5-7b19dee5d3e2" alt="" width="563"><figcaption></figcaption></figure>

2. В открывшемся окне нажмите "Add FaceBook Messenger".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FpJoMOc0IWG1Yjn5h4qFZ%2Fimage.png?alt=media&#x26;token=546fc3b4-5ce3-43fa-8806-a7d7cc42d82c" alt="" width="563"><figcaption></figcaption></figure>

2. Авторизуйтесь в Facebook. Обратите внимание, что это должна быть учетная запись администратора.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fk1AeamnmUxsYHyk47zzv%2Fimage.png?alt=media&#x26;token=cbc52fa9-b6c8-4a24-a67a-9afd82b556bb" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FROgeXhXqtTqV1qSB31Yv%2Fimage.png?alt=media&#x26;token=799aa7b1-4c29-4592-a4d5-5ffa2e3bcdaa" alt=""><figcaption></figcaption></figure>

3. Выберите страницу для интеграции:

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FmmGeG3YIshr78Mf9JHSq%2Fimage.png?alt=media&#x26;token=766e6eef-d49c-4fed-82f9-52d3b35f8f5f" alt=""><figcaption></figcaption></figure>

Готово! Подключение Facebook к Jivo завершено!

## Одноклассники

Для того чтобы подключить Одноклассники к приложению Jivo, сначала нужно получить токен для BotAPI.

1. Откройте вашу группу и перейдите в ее настройки.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FR5vIxazxO1WOnI8ZyvpC%2Fimage.png?alt=media&#x26;token=dc338cc7-e398-4914-af59-3148366f7fa2" alt="" width="563"><figcaption></figcaption></figure>

2. В разделе "Сообщения" включите сообщения для участников группы и нажмите кнопку "Получить ключ доступа".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FZ6h7bjoGXIFqDKf59Vg0%2Fimage.png?alt=media&#x26;token=a00d2cb1-d3a9-416d-8ecc-0502af38b876" alt="" width="563"><figcaption></figcaption></figure>

3. Скопируйте ключ доступа. Обратите внимание, что ключ доступа может получить только администратор группы.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FfzEPWyviKQaVkBKORT35%2Fimage.png?alt=media&#x26;token=6bd7529f-13c3-487a-bd9d-7b1768f0674a" alt="" width="563"><figcaption></figcaption></figure>

Теперь перейдем к приложению Jivo:

1. В списке каналов найдите Одноклассники и нажмите кнопку "Добавить".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F75c8Aj2zdaizHGmcHYpG%2Fimage.png?alt=media&#x26;token=56ffbdfd-4df5-448c-98ce-e611709770ae" alt="" width="563"><figcaption></figcaption></figure>

2. Нажмите на кнопку "Подключить".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fp6XqLde34WBBQNj8uZKH%2Fimage.png?alt=media&#x26;token=42011ff0-fe6b-4900-a82f-b271bc748629" alt="" width="563"><figcaption></figcaption></figure>

3. На открывшейся странице введите название группы и ключ доступа, полученный раннее, и нажмите "Подключить ОК к Jivo".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FzlEjPao0pPFj3siQGKWc%2Fimage.png?alt=media&#x26;token=dc65fb00-adeb-4f69-95d5-49862beedff5" alt="" width="563"><figcaption></figcaption></figure>

{% note tip %}

Готово! Одноклассники подключены к Jivo!

{% endnote %}

## AliExpress

Для того, чтобы подключить интеграцию необходимо быть зарегистрированным продавцом (пройти регистрацию можно по [этой ссылке](https://seller.aliexpress.ru/registration?utm_medium=any\&utm_source=integpartner\&utm_campaign=jivo)) и получить API-токен.

1. Перейдите на страницу [API-токенов](https://seller.aliexpress.ru/token-management/active?) и нажмите кнопку "Создать токен".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F0fx62sAmgdctbPjMWczB%2Fimage.png?alt=media&#x26;token=a86e6112-bfe4-4f5a-b4cf-8a9c71efaa22" alt="" width="563"><figcaption></figcaption></figure>

2. Созданный токен сразу появится в списке активных. Нажмите него, чтобы скопировать, т.к. токен пригодится при подключении к Jivo.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FOWPrlbVAg9B3PcxZvzhk%2Fimage.png?alt=media&#x26;token=593d5227-635f-404a-ad20-835991fd1468" alt="" width="515"><figcaption></figcaption></figure>

3. В разделе "Управление" -> "Каналы связи" найдите AliExpress и нажмите на кнопку "Добавить".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FV0pyTq5B127x80jVQgA0%2Fimage.png?alt=media&#x26;token=e15cb7d7-2a5a-41e7-8a4c-8816cc947e42" alt="" width="563"><figcaption></figcaption></figure>

4. В открывшемся окне нажмите "Продолжить".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FvlghTReIGv7rHXPja1ux%2Fimage.png?alt=media&#x26;token=aca99453-50c0-4c4a-9766-24772c67def8" alt="" width="563"><figcaption></figcaption></figure>

5. Введите название канала и токен, полученный раннее, в соответствующие поля и нажмите "Подключить".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F7Z6O1EJfCroHEU3vnERH%2Fimage.png?alt=media&#x26;token=36be913b-0f4f-4986-8da8-8113abc62e16" alt="" width="563"><figcaption></figcaption></figure>

{% note tip %}

Теперь в списке подключенных каналов покажется AliExpress. На этом все, интеграция подключена!

{% endnote %}

{% note info %}

**Если в процессе подключения или работы с каналом у вас возникли какие-то вопросы, обращайтесь в нашу поддержку, мы постараемся ответить на ваши вопросы!**

{% endnote %}

В следующей статье разберемся, как привязать аккаунт Jivo, чтобы работать с неопубликованной версией сценария и отладочными сообщениями!
