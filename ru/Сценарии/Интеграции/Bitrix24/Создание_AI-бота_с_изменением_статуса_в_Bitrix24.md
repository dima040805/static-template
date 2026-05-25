---
description: >-
  Из этой статьи вы узнаете, как настроить интеграцию с Bitrix24 с помощью
  готового шаблона
---

# Создание AI-бота с изменением статуса в Bitrix24

### Добавление шаблона

1.  Для того чтобы добавить шаблон в разделе “Сценарии”, нажмите на кнопку “Использовать шаблон”.

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FUpkXXfUZoJ0OG2xqLlQ4%2Fimage.png?alt=media&#x26;token=05b0ac66-f6a0-46ab-a031-1590cc0e580a" alt=""><figcaption></figcaption></figure>

    <figure><img src="https://img.notionusercontent.com/s3/prod-files-secure%2F233fe1fe-7932-4fbf-bb40-67d177e20dc4%2F4e06414f-4acd-4303-add5-93bb5f76aa26%2Fimage.png/size/w=2000?exp=1759315585&#x26;sig=KpcT75CySBqmrITLFiLWFGS095TavG4P-Ko5AlD_imc&#x26;id=2cb9dfd0-7161-47c5-83a0-f75101258a43&#x26;table=block&#x26;userId=611a2099-ca7e-45f7-820f-80aaea4f6cd1" alt=""><figcaption></figcaption></figure>
2.  В открывшемся окошке введите в поисковой строке название шаблона.

    ```
    AI-бот с изменением статуса в Bitrix24
    ```

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FAZ0kP2IatlAMPnL34ROl%2Fimage.png?alt=media&#x26;token=a005a77b-07cc-41ac-8c0f-12fdb445c2ce" alt=""><figcaption></figcaption></figure>
3. Нажмите “Использовать”

### Настройка статусов сделок

1. Откройте раздел CRM в Битрикс24.
2.  Выберите статусы сделок, которые запустят нужные процессы в CRM. В данном шаблоне берется за основу две реакции: пользователь оставляет номер телефона или хочет связаться с оператором.

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FlHHGLZyTDYvTsmzpAoSM%2Fimage.png?alt=media&#x26;token=b427e70a-8b6b-48ba-8232-f0f1df0c004a" alt=""><figcaption></figcaption></figure>
3.  Откройте сценарий Smartbot → Переменные → Глобальные.

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F32tEpab44d60rDiBYFul%2Fimage.png?alt=media&#x26;token=734f2b54-88b0-46e9-aa59-ae3c08fb16e6" alt=""><figcaption></figcaption></figure>
4. Укажите требуемые статусы сделок в Глобальных переменных:

* `%[Bitrix24] Позвонить%` - статус сделки, когда пользователь оставляет свой номер телефона в боте
*   `%[Bitrix24] Оператор%` - статус сделки, когда пользователь просит помощи сотрудника, вместо ИИ.

    <figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FLePCQhTiHGVDblFdLEfU%2Fimage.png?alt=media&#x26;token=71bc2cb1-8f5c-4e5b-844e-20a772e68fa1" alt=""><figcaption></figcaption></figure>

1. Настройка шаблона завершена. Вам остается только подключить нужного бота для этого сценария.

#### Тестирование

Теперь, если пользователь напишет боту свой номер телефона (или попросит помощи оператора), бот ответит пользователю, а сделка перейдет в нужный статус.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Ft4MpeSfmDAieC4ZD2BOt%2Fimage.png?alt=media&#x26;token=127e791e-e326-487c-839e-4a8e6047b071" alt=""><figcaption></figcaption></figure>

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FbCMRqWKNxyBZpCBFcomZ%2Fimage.png?alt=media&#x26;token=2aad48cf-c17c-4278-9372-f903f30e3851" alt=""><figcaption></figcaption></figure>

А если у вас остались вопросы по подключению – вы можете обратиться к нашей команде сборки под ключ, оставив заявку [в нашем боте](https://t.me/BusinessAISmartBot?start=bitrix24).
