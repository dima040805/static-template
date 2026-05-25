---
description: >-
  Из статьи вы узнаете, как подключить Юкассу для юридических лиц и принимать
  платежи от клиентов с помощью кнопок.
---

# ЮKassa для приема платежей

О том, кто может подключить ЮKassa и принимать платежи, подробнее рассказано в документации сервиса по [ссылке](https://yookassa.ru/questions/q66/).

### Добавление магазина в Smartbot Pro

1. Чтобы привязать кассу и начать принимать платежи, перейдите в раздел "Интеграции", выберите ЮKassa и нажмите "Подключить магазин". &#x20;

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F2itprs0kfn4xUjo3RxJL%2Fimage.png?alt=media&#x26;token=94652bc5-bd5b-43b5-ae4f-c3a9a49b79f6" alt=""><figcaption><p>Раздел "Интеграции"</p></figcaption></figure>

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FO5Xdo3LXhHUgZFMaSzcn%2Fimage.png?alt=media&#x26;token=4b56df37-fd4b-4dde-8be1-0b0f02f642f0" alt="" width="563"><figcaption></figcaption></figure>

2. Вас перенаправит на сайт ЮKassa, где нужно будет зарегистрироваться или войти, если у вас уже есть кабинет, а после выдать разрешение на создание платежей.

<img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Flf7BLOZ4aEIa7vTa3UGV%2F2.png?alt=media&#x26;token=1bac610d-9833-44a9-ae04-3a2eef042f44" alt="Страница авторизации" width="563">

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FB0ef13G5Mwy2RIk7Uj87%2Fimage.png?alt=media&#x26;token=b76d6864-8a73-4e03-b8fe-3cc98fbe0b49" alt="" width="563"><figcaption><p>Выдача разрешения</p></figcaption></figure>

3. Далее на открывшейся странице выберите магазин, через который будут проходить платежи.&#x20;

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FYSRKnuhR5wXToRuEkoz4%2Fimage.png?alt=media&#x26;token=263fc329-bf2c-4a1b-baaf-f9b12243c713" alt="" width="563"><figcaption><p>Список магазинов, к которым можно выдать доступ</p></figcaption></figure>

{% note info %}

Для создания тестового магазина есть подробная инструкция в статье ЮKassa по [ссылке](https://yookassa.ru/docs/support/merchant/payments/implement/test-store).&#x20;

Рабочий, не тестовый магазин создается при регистрации в кабинете юридического лица, ИП или самозанятого.

{% endnote %}

4. После этого ваш электронный магазин появится в Smartbot Pro. Вы можете подключить несколько магазинов, а также выбрать тип налогообложения.

### Настройка оплаты в сценарии

С момента подключения магазина в блоке "Отправить сообщение" появится кнопка оплаты.&#x20;

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FRwoayUcIj9QbmaAOJMlr%2Fimage.png?alt=media&#x26;token=00b6273d-9529-461f-9fa2-3c9c69cfc9c6" alt=""><figcaption></figcaption></figure>

Введите название кнопки и выберите из выпадающего списка магазин, куда поступят деньги.&#x20;

Следующим блоком можно настроить благодарность за оплату, либо другие нужные вам опции.&#x20;

В готовом виде получится так:&#x20;

![](https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FKqpNU9ChJb5n7zqcqVVl%2F5.png?alt=media\&token=f73119ca-0b0a-4f7b-8732-32a3ca310fa1)

![](https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FfS6bGPWVbs95sHFp48vY%2F6.png?alt=media\&token=7c220b00-2007-4707-a7b8-a089dd27e556)

![](https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fkci3w0yy4qDCb0gmr9K7%2F7.png?alt=media\&token=e4c76378-fa1c-46df-b937-6bb1348cb5a0)



{% note tip %}

Теперь вы знаете, как подключить электронную кассу и принимать платежи клиентов! 😉

{% endnote %}
