---
description: Из этой статьи вы узнаете, как подключить amoCRM к вашему чат-боту.
---

# amoCRM


<p class="yfm-lead">Из этой статьи вы узнаете, как подключить amoCRM к вашему чат-боту.</p>
Для пользователей amoCRM мы создали публичный виджет в amoМаркете, с помощью которого можно установить приложение Smartbot Pro и создавать сделки в amoCRM прямо из бота 🔥.&#x20;

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FjrNi9ObfvEf9xhcCOQ1R%2Fimage.png?alt=media&#x26;token=5b384a1b-e2a8-4a14-8053-13c29bd7c7c4" alt="" width="563"><figcaption></figcaption></figure>

Интеграция чат-бота с amoCRM позволит

1. Получить контакт клиента
2. Создать сделку в нужной воронке с актуальным статусом
3. Прикрепить к сделке контактные данные клиента - это может быть имя, фамилия, телефон, email. \
   Созданные контакты будут также доступны разделе "Списки" -> "Контакты" вашей CRM&#x20;
4. Назначить сделке ответственного менеджера
5. Добавить к сделке дополнительные поля в формате Ключ: Значение.&#x20;
6. Обновить или дополнить данные контакта\
   Например, если сделка была создана без телефона, а в последующей для этого пользователя сделке поле "Телефон" будет заполнено, то данные контакта обновятся как в списке контактов, так и во всех сделках с этим контактом.&#x20;

**Настройка интеграции Smartbot <--> amoCRM состоит из пары этапов:**

1. Подключение аккаунта amoCRM в вашем проекте  Smartbot Pro;&#x20;
2. Установка приложения Smartbot Pro с помощью виджета в amoCRM;

После создания интеграции вы сможете отправлять заявки в amo с помощью блока "Создать сделку" и изменять сделки, используя блок "Изменить сделку", в нужном месте любого сценария. О каждом из блоков расскажем в отдельных статьях!

## Подключение amoCRM к Smartbot Pro

{% note info %}

Для подключения Smartbot Pro к amoCRM вам понадобится аккаунт в amoCRM с оплаченной подпиской или действующим триалом.&#x20;

{% endnote %}

1. Зайдите в раздел "Интеграции" в главном меню проекта и выберите amoCRM&#x20;

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FVfpuox8p4tN4ZdQYiXXy%2Fimage.png?alt=media&#x26;token=44db490f-2b88-4e0f-bf57-f04d9ac5f251" alt="" width="563"><figcaption></figcaption></figure>

2. Введите название вашего аккаунта в amoCRM. Его можно получить из адреса в браузере. Пример ссылки: `https://`**`smartbotproru`**`.amocrm.ru/` , где `smartbotproru` - название аккаунта&#x20;

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FX1qGSWlVQaNqPBntQPnq%2Fimage.png?alt=media&#x26;token=91556a54-001a-4eca-9559-5c33ef25be94" alt="" width="563"><figcaption></figcaption></figure>

3. Нажмите кнопку "Добавить аккаунт" - появится инструкция с последующими шагами.&#x20;

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FO9t6t3KWceBOmgDMMPMp%2Fimage.png?alt=media&#x26;token=b28bdaa3-71bd-403b-a63c-952faebf6503" alt="" width="563"><figcaption></figcaption></figure>

Далее разберем каждый пункт настройки интеграции в amoCRM более подробно.

## Установка Smartbot Pro в amoCRM&#x20;

1. Перейдите по ссылке из пункта 1 и введите в поиске Smartbot Pro&#x20;

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FZEMmfuL5TEO5G7NydQhL%2Fimage.png?alt=media&#x26;token=4136aeae-61d4-45aa-a87a-5be5f0657e08" alt="" width="563"><figcaption></figcaption></figure>

2. В виджете Smartbot Pro в [amoМаркете](https://smartbotpro.amocrm.ru/amo-market/) проставьте галочку "Согласен на передачу персональных данных из amoCRM в Smartbot Pro" и нажмите кнопку **“Установить”**

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FM5ETybkoF8dLcZSHe4xF%2Fimage.png?alt=media&#x26;token=8dc88c8e-35ca-4439-be95-22d1326d23d7" alt="" width="563"><figcaption></figcaption></figure>

3. В поле “Кодовое слово” вставьте кодовое слово (скопируйте его в разделе "Интеграции") и нажмите **"Сохранить"**

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FDznh7BW3dtHLMOw5nazJ%2Fimage.png?alt=media&#x26;token=c6a4df89-a1bb-4f5c-904c-e4574273af63" alt="" width="563"><figcaption></figcaption></figure>

4. После этого вернитесь на страницу интеграции с amo в Smartbot Pro и обновите страницу - добавленная интеграция появится на странице.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F7aUfRZrVJe3kQcSKJKhD%2Fimage.png?alt=media&#x26;token=5f122642-fd0e-4074-85be-1c0597078107" alt="" width="563"><figcaption></figcaption></figure>

{% note info %}

Обратите внимание, что интеграция может не сразу появиться на странице. В таком случае нужно подождать пару минут и повторить шаги подключения. Наберитесь терпения 🙏. Может потребоваться до 5 попыток подключения.

{% endnote %}

## Удаление интеграции

Для удаления интеграции из Smartbot Pro перейдите в ваш аккаунт в amoCRM, в разделе amoMarket зайдите в "Установленные", найдите Smartbot Pro и нажмите “Отключить”. После отключения интеграция пропадет из списка установленных.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F8vXt8F1XJStdB14fEIJW%2Fimage.png?alt=media&#x26;token=ee54b3fc-9790-4475-905f-7625a5c2f058" alt="" width="563"><figcaption></figcaption></figure>

{% note tip %}

Теперь вы знаете, как подключить интеграцию amoCRM! В следующих статьях подробно разберем, как работать со сделками!

{% endnote %}
