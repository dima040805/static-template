---
description: >-
  В этой статье разберем, как оплачивать цифровые товары с помощью Telegram
  Stars.
---

# Прием оплаты с помощью Telegram Stars

6 июня 2024 года Telegram анонсировал обновление для ботов, согласно которому рассчитываться за **цифровые товары** можно только в валюте Telegram Stars (подробнее в документации Telegram [по ссылке](https://telegram.org/blog/telegram-stars/ru?ln=a)). Если принимать оплату за них в рублях или другой валюте, Telegram будет блокировать таких ботов. Пользователи сообщают, что первые блокировки уже были замечены.&#x20;

В связи с этим в Smartbot Pro также была добавлена возможность принимать оплаты в Telegram Stars! 🥳

### Подключение Telegram Stars к проекту &#x20;

Чтобы подключить оплату в Telegram Stars к своему боту, зайдите в раздел "Интеграции", далее в "Telegram Payments" и нажмите кнопку "Добавить".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FQ0yiU5tBRFMh82na6B2N%2Fimage.png?alt=media&#x26;token=cdb797f9-4c1a-4da8-b18c-e3257d109ce9" alt=""><figcaption><p>Раздел "Интеграции"</p></figcaption></figure>

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FJk8wS1ToS0SxmOEQ3Eh5%2Fimage.png?alt=media&#x26;token=3d871ebe-51f9-4833-845a-231b11df57c4" alt=""><figcaption><p>Telegram Payments</p></figcaption></figure>

Выберите тип "Цифровые товары" и укажите бота, в котором будет производиться оплата Telegram Stars.

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fpb7qaHEQegtd2GzuIqO9%2Fimage.png?alt=media&#x26;token=429fd9ca-0645-4dc1-9108-45f1188b4113" alt=""><figcaption></figcaption></figure>

### Настройка оплаты в Telegram в сценарии

Теперь, чтобы в сценарии настроить оплату с помощью Telegram Stars:

1. Создайте или используйте готовый блок "[Отправить сообщение"](../deistviya/otpravit-soobshenie)
2. Добавьте кнопку с типом "Создать платеж"\
   Или "Оплатить заказ Shopback", если это оплата товара с [витрины в Тelegram](../../instrumenty/magaziny-v-telegram).&#x20;
3. Выберите способ оплаты "Telegram Payments"&#x20;
4. Нужная платежная система - "Telegram Stars".

{% note info %}

Для того, чтобы указать цену товара в "звездах", в настройках магазина просто написать текстом "TG Stars" не получится, т.к. поле имеет лимит по кол-ву символов. Можно использовать эмодзи звезды (⭐️) для обозначения валюты Telegram Stars.

{% endnote %}

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FLwBX2rYZWnUu1BeOdquL%2Fimage.png?alt=media&#x26;token=ded212db-f165-4eae-b7d7-bc5a826c5897" alt="" width="375"><figcaption></figcaption></figure>

{% note warning %}

Обратите внимание, что оплата будет работать **только для того бота**, которого вы указали при настройке интеграции! Если запустите такой блок в другом боте, в отладке будет ошибка:

![](https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FvZF08tUFXFrI2IDtiBUK%2Fimage.png?alt=media\&token=bbe05115-2ce4-49b0-af75-c7ac458ea5ae)

{% endnote %}

{% note tip %}

Поздравляем! Вы успешно настроили оплаты с Telegram Stars для оплаты цифровых товаров! По всем вопросам обращайтесь в нашу тех. поддержку - они подскажут и помогут справится со всеми трудностями!&#x20;

{% endnote %}

### FAQ

1. Как я могу вывести звезды, полученные моим ботом?

Вывод Telegram Stars на данный момент не реализован, но вывод планируется в Toncoin при помощи платформы Fragment, пока ничего подробнее от Telegram нет (упоминание об этом в [официальной документации Telegram](https://telegram.org/blog/telegram-stars/ru#integratsiya-s-magazinami-prilozhenii)).

2. Пользователь оплатил товар "звездами". Где я могу увидеть, куда они начислились?

Для этого откройте диалог с ботом, к которому у вас подключена оплата "звездами" и нажмите на шапку. Открыв ее, нажмите на карандаш (на macOS это может быть кнопка "Изм.").

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FQs7iniMApMO6N4iEPCjQ%2Fimage.png?alt=media&#x26;token=aa5a4b29-7bb8-419e-93a1-fad2e76f3cee" alt="" width="563"><figcaption></figcaption></figure>

У вас откроются настройки профиля вашего бота и тут вы сможете найти "Баланс".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FIsPVh0569RW9mYYgLQjq%2Fimage.png?alt=media&#x26;token=64a09d50-f446-4104-b434-ad7c1f80be21" alt="" width="352"><figcaption></figcaption></figure>

Внутри него можете найти всю необходимую информацию о зачислениях и списаниях - когда, от кого и сколько "звезд".

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2Fi2S1yZRygXEVbQsKSgMR%2Fimage.png?alt=media&#x26;token=3fe61032-f4a2-4234-9cf3-2d690b6acab3" alt="" width="563"><figcaption></figcaption></figure>

{% note info %}

На момент написания документации не на всех устройствах есть возможность просмотра баланса Telegram Stars в боте. Поэтому рекомендуем обновить Telegram до последней версии и смотреть на разных устройствах, если обновление приложения не помогает!

{% endnote %}
