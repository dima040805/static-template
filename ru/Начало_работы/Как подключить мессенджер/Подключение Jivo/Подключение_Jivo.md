---
description: >-
  В этой статье расскажем, как интегрировать Jivo и Smartbot Pro. После
  интеграции бот сможет отвечать в мини-чате поддержки на вашем сайте, а также в
  любом другом канале, подключенным к вашему Jivo.
---

# Подключение Jivo

### Шаг 1

Заходим в раздел "Каналы" и нажимаем на лого JivoChat.&#x20;

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FRcvF0JNzd6l32OrKnrRr%2Fimage.png?alt=media&#x26;token=553c5f45-df14-4fe1-8d5d-00bce2d837d7" alt=""><figcaption></figcaption></figure>

### Шаг 2

Скопируйте токен и пройдите по ссылке во втором пункте инструкции, чтобы попасть на страницу создания интеграции (в кабинете Jivo это будет называться словом "Расширения").&#x20;

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fc44vd6o1ojHWkDDQ1Gi8%2Fimage.png?alt=media&#x26;token=e0e0d95d-9c29-4662-a33d-4b47819155cf" alt=""><figcaption></figcaption></figure>

{% note info %}

Обратите внимание, что если у вас еще не создан кабинет в Jivo, то ссылка отправит вас на страницу регистрации, поэтому сначала рекомендуем создать кабинет и войти в него, а затем приступить к интеграции со Smartbot!

{% endnote %}

### Шаг 3

Перейдя в Jivo, вы увидите несколько полей, которые нужно заполнить:

* Имя бота - это будет имя вашего расширения
* Должность бота (необязательное поле)&#x20;
* Токен бота -  сюда вставляется токен, скопированный на странице Smartbot&#x20;
* Подключить для следующих каналов - тут нужно выбрать, для каких уже подключенных в Jivo каналов, будет работать интеграция (по дефолту выбраны все каналы)

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FIwQsWyX9EgO2F6176SJ5%2Fimage.png?alt=media&#x26;token=46f06d08-4257-40dc-b938-245d54b746af" alt="" width="563"><figcaption></figcaption></figure>

После заполнения нажмите на кнопку "Сохранить" внизу страницы и вернитесь в Smartbot. Там также нажмите кнопку "Создать", иначе интеграция создана не будет.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FIedLrAQkaxOYJ7OiMFSC%2Fimage.png?alt=media&#x26;token=3356803a-2930-4934-b53f-aefbfef03f43" alt=""><figcaption></figcaption></figure>

## FAQ

**Вопрос:** \
**"После подключения Jivo настроил сценарий, проверил, что он включен, подключил бота в Jivo, но бот не отвечает. Почему?"**

Когда вы настраивали расширение, вы могли указать только каналы, которые были подключены к Jivo на тот момент. Если после вы подключили еще каналы, то даже если было выбрано поле "Все каналы", они автоматически подтягиваться не будут и нужно самостоятельно добавить их в расширение.&#x20;

Для этого перейдите в раздел Управление → Расширения → Подключенные (выберите нужную интеграцию в списке) → Опции&#x20;

<figure><img src="https://lh6.googleusercontent.com/j46OyAHnLRxsYfHiupombI2p3QJKx5JQh6pYJc3UWI_pvcjiqLPWRmvwAbf7zhGgfHg95TY-wbcPByyNE6tQHsK3Yhzcx5Dpsp6WFlUwPTaXKi4hA2f_ApcK_VVbvRIjhPE-yKq3LTkaUUl-GdFeJe0BnABEP5Uk0hYVx4dutBaO3vpNolHRHtIFFMz4ag" alt=""><figcaption></figcaption></figure>

Укажите нужный вам канал в селекторе и нажмите “Сохранить”&#x20;

<figure><img src="https://lh3.googleusercontent.com/y6UzzjUcn9Pf69gYm-iXr9JbwcvOrMco4LyhQ_OuE08kvuEmg01FsK-dasWQreyFVWx4Npr3xrblr0UMf-NIa7T-MWQgCRcavoAUQwkXe3JBMXc5e2_JPxNovXGnrijjb8u3dYH59PBdHPHOLa1mUNX212ODAYKoaxQfANICqD9MoYcxQWEqSBCUGu9-Ag" alt=""><figcaption></figcaption></figure>

{% note tip %}

Мы завершили подключение Jivo к Smartbot Pro!

{% endnote %}

Подключение других каналов через Jivo, например, ВКонтакте, Авито и других,  мы рассмотрим в следующей статье!
