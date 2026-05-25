---
description: >-
  В этой статье разберем, как подключить новую платежную интеграцию в свой
  проект
---

# Cloud Payments для приема платежей

Для подключения интеграции выбираем Cloud Payments в разделе "Интеграции" и нажимаем  "Перейти" -> попадаем в окно для добавления сайта

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FXrk3WgbEUYl9NOu86UEj%2Fimage.png?alt=media&#x26;token=5611e9d8-2412-4dfd-b86e-c521124b8af7" alt=""><figcaption></figcaption></figure>

Далее у нас открывается инструкция для подключения интеграции, и для следующих шагов нам нужно переместиться в ваш кабинет Cloud Payments. Там нам нужно зайти в раздел "Сайты" и нажать "Создать сайт":

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FiRVCsUAeulyH8CCA8WYG%2Fimage.png?alt=media&#x26;token=8fd3e672-aaba-4fa0-b322-4f4ae576b02c" alt=""><figcaption></figcaption></figure>

При создании нужно будет заполнить несколько полей:

*

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F55mwnrf1wVDrHCmkQZz6%2Fimage.png?alt=media&#x26;token=bdd7c4bd-b48c-4969-87c4-3011e573525a" alt="" width="563"><figcaption></figcaption></figure>
* Название - таким будет название платежной формы для вашего клиента
* URL - тут укажите ваш сайт, если он есть\
  Если его нет, то пропустите это поле, туда автоматически проставится сайт Cloud Payments

Также проставить галку "Не проверять доступность сайта"&#x20;

Сайт создан и теперь нам нужно получить ключи для создания связки со Smartbot Pro. Для этого заходим внутрь только что созданного сайта и видим 2 поля - Public ID и Пароль для API.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fqtz7v9zFmt4kLmxZjvxd%2Fimage.png?alt=media&#x26;token=8d5ad266-fc11-4c4a-87c1-79c6d9be6927" alt=""><figcaption></figcaption></figure>

Их нужно скопировать и вставить в соответствующие поля в Smartbot Pro:

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FzAahvdXXAKNHOra1D22e%2Fimage.png?alt=media&#x26;token=f59695d7-5b46-4227-9b49-a7450d2b90b6" alt=""><figcaption></figcaption></figure>

Теперь для настройки уведомлений, о том что платеж прошел или нет, нужно:

* в Smartbot скопировать ссылку из 3-го пункта инструкции
* внутри созданного вами сайта в разделе "Уведомления" включить тумблер напротив уведомлений "Pay - о принятом платеже"&#x20;
* в появившееся поле вставить ссылку
* в кабинете Cloud Payments нажать "Сохранить уведомления", а в Smartbot - кнопку "Подключить"

Поздравляю! Платежная интеграция подключена!
