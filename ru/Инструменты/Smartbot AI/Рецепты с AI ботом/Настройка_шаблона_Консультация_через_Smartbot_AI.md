---
description: В этой статье мы разберём, как настроить шаблон Smartbot AI под свои задачи.
---

# Настройка шаблона "Консультация через Smartbot AI"


<p class="yfm-lead">В этой статье мы разберём, как настроить шаблон Smartbot AI под свои задачи.</p>

## Выбор шаблона

[Выбираем шаблон](https://docs.smartbotpro.ru/scenarii/osnovy/shablony-scenariev) "Продажи с помощью Smartbot AI"

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FonWrZEkEyZ1L7grGkm10%2Fimage.png?alt=media&#x26;token=92bd6329-713f-4520-868f-bce3e46e4c3b" alt="" width="563"><figcaption></figcaption></figure>

## Стартовое сообщение

В большинстве случаев пользователи запускают бота с помощью команды /start (в Telegram) или по нажатию кнопки "Начать" (в ВК).

Чтобы Smartbot AI не генерировал ответы на запуск бота, можно установить для них единое ответное сообщение, а также добавить другие варианты сообщений пользователей, на которые ваш бот будет отвечать приветствием (например, "Привет", "Здравствуйте" или "Алоха").

Ответ от бота настроен в личных сообщениях с помощью проверки переменной %realm%(Где сработал бот). Подробнее про переменную описано [тут](../../../scenarii/peremennye/gde-srabotal-bot-realm).

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fpm72YCtBsbOchW0LQ52Y%2Fimage.png?alt=media&#x26;token=672c8c23-b98a-48a6-bfd4-882551060138" alt=""><figcaption><p>Варианты приветственных сообщений пользователя</p></figcaption></figure>

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FpQzbJXucTDnyX8vH2Wzm%2Fimage.png?alt=media&#x26;token=fe236fd9-7836-4989-a565-4156c3746687" alt=""><figcaption><p>Ответ от бота</p></figcaption></figure>

## Проверка сообщений

Чтобы бот не упускал ни одного вопроса, мы устанавливаем реакцию на каждое сообщение пользователя (вы можете самостоятельно добавить этот блок через "События" -> "Нет подходящего сценария"). Также с проверкой переменной %realm%, чтобы бот сработал в личных сообщениях с ботом.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FmReuUVWvmRu98Igudl7y%2Fimage.png?alt=media&#x26;token=0b84bde9-1598-45f8-ab1b-ede257248df5" alt=""><figcaption></figcaption></figure>

### Создание лида

Если ваша цель — получать номера телефонов пользователей для отдела продаж, то сразу после реакции на любое сообщение пользователя вы можете проверять, прислал ли он телефон или нет. Для этого в шаблоне установлен шаг "Обработать сообщение".

В этом шаге мы отключили галочку "Ждать сообщение от пользователя" и установили проверку сообщения по номеру телефона.

А также, чтобы передать телефон пользователя в заявке, настроили сохранение его в соответствующую переменную.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F5OgVfMQNArJre7JJzJ8D%2Fimage.png?alt=media&#x26;token=90329be8-59c6-41f8-837b-ed91096a27d0" alt=""><figcaption></figcaption></figure>

Далее можно сохранить заявку в соответствии с настроенным рабочим процессом. Например:

* добавить новую строку в Google таблицу

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fv5mBZCiFr9POZCVve7eh%2Fimage.png?alt=media&#x26;token=b5c80db2-48c3-47da-98e1-b8fa13289765" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FuLfiG1LVs4VD5hqBj3k6%2Fimage.png?alt=media&#x26;token=6d0333a5-c5a0-4bf1-9918-abd0270da5d5" alt=""><figcaption></figcaption></figure>

* отправить уведомление в личные сообщения администратору и/или в рабочий групповой чат

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F4jkoRzYRsVCsJAlzomph%2Fimage.png?alt=media&#x26;token=33c336c7-848a-40b5-9886-1f7b10b09ac6" alt=""><figcaption></figcaption></figure>

{% note info %}

В шаблоне уже заготовлен вывод истории переписки пользователя с чат-ботом в удобном формате

{% endnote %}

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FzZocbrVz2DsRo72bX9Mg%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-12-01%20%D0%B2%2019.50.03.png?alt=media&#x26;token=0849458a-ad49-4d5b-9dc3-0402b3165f57" alt="" width="375"><figcaption></figcaption></figure>

* [создать сделку в AmoCRM](https://docs.smartbotpro.ru/scenarii/integracii/amocrm) и тд.

## Генерация ответа от Smartbot AI

Если бот не идентифицировал номер телефона в сообщении пользователя, то он перейдёт к блоку "Общение с Smartbot AI". Для этого он соединён стрелкой с выходом по ошибке из блока сохранения телефона пользователя.

А также, для обработки каждого сообщения пользователя отдельно, в нём установлена галочка "Выйти из режима AI после первого сообщения AI бота".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F8GxrlHKjCL3UTXJOdGQ1%2Fimage.png?alt=media&#x26;token=03dc7cca-c01d-46ff-bf7f-c768528eb93f" alt=""><figcaption></figcaption></figure>

ИИ сегодня безусловно творит чудеса, но всё же ещё не идеален. Вы можете настроить ответ пользователю на случай, если при генерации ответа произойдёт ошибка.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FSFWDk90HWkduW64ukeTy%2Fimage.png?alt=media&#x26;token=a115e2c2-dc65-48f5-a094-fb7e53eb4c14" alt=""><figcaption></figcaption></figure>

### Сохранение истории чата

Чтобы знать, какие вопросы задают ваши пользователи и какие ответы они получают от AI, можно сохранять историю их общения в Google таблицу.

{% note tip %}

Сообщения пользователей сохраняются в специальную переменную %message\_text%

А сгенерированные сообщения от Smartbot AI — в %ai\_message\_text%

{% endnote %}

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FFQEpZNSLoL1AdE4gOerB%2Fimage.png?alt=media&#x26;token=61e15a6c-3334-4ffa-8012-b7c3225d5ff5" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FHMsRSOJo1v1WFkIiX600%2Fimage.png?alt=media&#x26;token=c882939f-773d-42ee-bc06-7e5e4e78c877" alt=""><figcaption></figcaption></figure>

Также, чтобы вы могли работать с последними сообщениями пользователя и ответами на них от Smartbot AI (например, передавать их в заявке для отдела продаж), в шаблоне уже настроено автоматическое сохранение переписки пользователя с AI в переменную %История переписки%.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F1UjDm052M00xHqrQ7Rcg%2Fimage.png?alt=media&#x26;token=176c5d19-698d-4181-9c94-751841830942" alt=""><figcaption></figcaption></figure>

И автоматическая очистка наиболее старых данных из истории для освобождения места и успешного сохранения последних сообщений.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FUlkNrZnPr3Sm8XF0fdoF%2Fimage.png?alt=media&#x26;token=26391b4f-1858-4d5b-9cf8-8bdb8aff2159" alt=""><figcaption></figcaption></figure>

Этой настройки достаточно, чтобы протестировать и при необходимости обучить вашего ИИ-консультанта и привлечь его к обработке заявок от ваших клиентов.

Желаем успехов во внедрении Smartbot AI в ваш бизнес!
