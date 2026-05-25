---
description: Эта функция позволяет запускать бота по API из любого другого сервиса.
---

# Webhook


<p class="yfm-lead">Эта функция позволяет запускать бота по API из любого другого сервиса.</p>

### Зачем это нужно&#x20;

Пример: пользователь попал в бота онлайн-школы.

Бот рассказал про курсы, и клиент зашел на сайт. Там купил один из курсов. Если в обучающей платформе курса настроить интеграции по webhook, после этого бот сам напишет клиенту.

То есть с помощью вебхука другой сервис может запустить нужную цепочку сценария Smartbot Pro.

### **Создание и настройка webhook**

1. **Создаем токен.**&#x20;

Создать новый токен и увидеть список всех токенов проекта можно в разделе «Интеграции».  &#x20;

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FfVkBSyMMxJTby3O99f4p%2Fimage.png?alt=media&#x26;token=48c3d4e1-0f7b-4e41-98db-292c8507a635" alt=""><figcaption></figcaption></figure>

Для запуска бота нужно создать токен с правом выполнения блоков. Нажмите  «Создать токен» и выберите «Уровень доступа — Выполнение блоков».

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FohHva848ktd6UEReEQ1z%2Fimage.png?alt=media&#x26;token=2d8f5b80-0eae-41be-81b4-5a2a3d640181" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FAjhP3H5H7QiLy22d4T96%2Fimage.png?alt=media&#x26;token=ffb52256-0a7e-4a33-91cf-ad4ba1f98c3c" alt=""><figcaption></figcaption></figure>

**2. Создаем событие "Webhook" в сценарии**

В сценарии для запуска цепочки из другого сервиса нужно настроить специальное событие Webhook, которое позволит запустить бота по API.

Переходим в нужный сценарий, в боковом меню выбираем "События" --> "Webhook".&#x20;

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FqFRVHdTE06VVPE1MLss4%2Fimage.png?alt=media&#x26;token=3fe80c5d-36cb-49b6-8a4c-bda710c5cfcb" alt=""><figcaption></figcaption></figure>

**3. Указываем токен**

В  блоке Webhook выбираем созданный токен или создаем новый.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FSLzsTnNOk0sdiahL2R1c%2Fimage.png?alt=media&#x26;token=9b1ffb00-efa0-4f6e-93aa-623b0f44d658" alt=""><figcaption></figcaption></figure>

**4. Выбираем канал**&#x20;

Выберите канал в социальной сети, где сработает бот после того, как его «дернуть» вебхуком.

Если бот работает одновременно в ЛС и в беседе, необходимо также указать нужный ча&#x442;**:**

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FKgRXghhLLT61HH8Zx05U%2Fimage.png?alt=media&#x26;token=1eba9bd4-193d-4ca3-bedb-b2b41d6c2e89" alt=""><figcaption></figcaption></figure>

**6.** **Параметры запроса:** **URL и body.**&#x20;

Скопируйте указанный URL и отправьте на него **POST-запрос** из вашего сервиса.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FED32agwYGiCCrTvN8R11%2Fimage.png?alt=media&#x26;token=81e2afc8-db5e-40f4-abac-0ed4f0bad798" alt=""><figcaption></figcaption></figure>

Скопируйте следующий JSON и вставьте его в **Body** запроса:

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FdLe6tM4cB5uhY4B51adK%2Fimage.png?alt=media&#x26;token=8aabd37f-5680-4a25-94b2-51c1c2ea589a" alt=""><figcaption></figcaption></figure>

{% note info %}

peer\_id — это ID чата, в который будет отправлено сообщение от бота.

{% endnote %}

**Если бот должен сработать в групповом чате**, то peer\_id установится автоматически.&#x20;

**Если бот должен сработать в ЛС**, то peer\_id нужно заполнить самостоятельно в соответствии с подсказкой.&#x20;

![](https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F8suDwqTJH4H4CAZJ5oqw%2Fimage.png?alt=media\&token=8246391c-ce15-4159-acdc-4f58b0f76034)

### **Требования к отправке сообщения через Webhook**

Чтобы пользователь получил сообщение через webhook, должно выполняться два условия:\
— разрешена отправка сообщений в лс \
— пользователь уже общался с ботом (бот не может первым написать пользователю)

### Удаление токена

Если  токен украден злоумышленником, его нужно удалить в разделе «Интеграции».

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F6F8Z1t1kTS8NU7J6alAf%2Fimage.png?alt=media&#x26;token=d74052ac-659c-4cff-832d-c3af076e8ff7" alt=""><figcaption></figcaption></figure>
