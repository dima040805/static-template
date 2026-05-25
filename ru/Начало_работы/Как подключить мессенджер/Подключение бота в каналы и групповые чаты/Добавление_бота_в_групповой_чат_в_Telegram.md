# Добавление бота в групповой чат в Telegram

Для того, чтобы добавить бота в групповой чат, необходимо:&#x20;

1. **Убедиться, что бота можно добавлять в групповые чаты**&#x20;

Для этого перейдите в BotFather и выберите настройки вашего бота: Bot Settings -> Allow groups?

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2F7H7JBpn5XpYmDHxZdRHU%2Fimage.png?alt=media&#x26;token=491e65c6-641c-4ddc-a8e7-4fcdaa85e5f0" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://lh3.googleusercontent.com/-4EdDmvgPzt9l4Zc1TaR5x9T8TPupj7KpvCC2iDOov-CQ-hVjR7NdlaR10JefveNmTEB-TzH1s7avY8yRKTjv3lZVSFANmJHKXI_rFIZFsemsVkX9ZHoJJYp7GWghWQTskUVg1ztzrn3eHuZfYfQtkSCzgrKvIHV1A-fEv8hfs6eBsVHGWaJKbRaIg" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://4058588211-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvTd8XmFMqkqZga7zhLuk%2Fuploads%2FaISBiCXXwK7mTp3HgFqj%2Fimage.png?alt=media&#x26;token=56c39bd4-7de0-4d69-b038-144db1741118" alt="" width="563"><figcaption></figcaption></figure>

2\. **Проверить состояние настройки “Режим конфиденциальности”**&#x20;

Обратите внимание на настройку “Режим конфиденциальности” (Group Privacy).&#x20;

<figure><img src="https://lh6.googleusercontent.com/P68SQT2VQnUlHWjllrWkP518JEd9E3HMakGP_dFUKh_vBPkspVRCuUqgQzR_-iXFcm8cwvrwodwRL-RqzR0jWXk2B2Y7XgBZjXQWRlG37n0Q7vG3ZHGs-h-fsebgy13Iic_11AZbK07WQunoHTm8RfttaUl90Bw40w5wOOH6I3KFCgNJpQlp1rh5kQ" alt="" width="563"><figcaption></figcaption></figure>

По умолчанию режим конфиденциальности включен, и бот в беседе будет реагировать только на некоторые сообщения, а именно:&#x20;

* Сообщения, начинающиеся с '/' Собственные сообщения бота Служебные сообщения (люди добавлены или удалены из группы и т.д.)&#x20;
* Сообщения из каналов, в которых он состоит&#x20;

Подробнее об этой особенности можно прочесть [здесь](https://core.telegram.org/bots#privacy-mode).

{% note info %}

Если необходимо, чтобы бот реагировал на все сообщения, отключите режим конфиденциальности: в состоянии “Privacy mode is enabled” нажмите кнопку “Turn off”.

{% endnote %}

<figure><img src="https://lh3.googleusercontent.com/YZOxdnXRrg7oxzjLAUg3BJSxZa2_3DbOdFU1xmEnfkybl9jxbu-48izCB_16HIQUsuqJW9sO7dqbX_jnyEfuFELGiwr2x_NupPs_ugbrThdCRakBKWFeKtd41EUYEX1nqHIYTbB8cphSv782ggUVHarMx5ehIb5f9M4uxOTF2mE_XSQ40JVUt3mFrA" alt="" width="563"><figcaption></figcaption></figure>

3\. **Бот должен быть в групповом чате админом**&#x20;

Сделайте бота участником и повысьте его права:

{% note info %}

Чтобы бот отвечал на запросы админов корректно, настройка анонимности должна быть выключена.

{% endnote %}

<figure><img src="https://lh4.googleusercontent.com/F-jAt04MmXIBf_rif11hTCYIhI_Gq7MRrQpEe8IDZ6I_s_tWySrOJMbzRv4a8NdecMU-SY4Q6NxzXqrycfIPgzRqR1keuJZK9xp440q2AOBrZ07PHSeFevwsU3EhK4oXyiyP6QgTO4gCeyXWC_vzd23HkBcTM26V1XgT8NO3vnUOAdm9v3XeBEZqiQ" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://lh4.googleusercontent.com/9wHdKp3io7yZrt1aH9BFwqv3X-7FzQClD059cylVwqPtPMn9ql4PcQnSK8DdbNjheHmY4vvTFdaKjPCaZOKzIuOjmXs6gBCF_rL8ub28JJwwmVLjvbywUKzf69N64Ect1QHdqtZXbpPRIAPvO0gmL7gLEXL7I_RfmH2Y3ElHGaHmfqj4RDNnGcCwOA" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://lh6.googleusercontent.com/rYo-lLWgEhBz05Qgp-_ylMsyQy4zPZ3RH8s82vcDcIiPiiI9_1jW3vquZnpbbgIvY3mojAJ-UndHR0T0G8e6sOugYBHWxvFKcLs4nly0tZbk0v4t4SLxxefroE5LgIa9LQZqiXD-avzwKD2C_nOWOLGTx3l90mlBU3q3se3wKaPzXmSm7yEvwQ1lAA" alt="" width="563"><figcaption></figcaption></figure>

{% note tip %}

Отлично! Теперь ваш бот работает в групповом чате!

{% endnote %}

<figure><img src="https://lh5.googleusercontent.com/xXZmXtE7TGlXq4AMgK1aShJCo0TxaFofzjvEMrBqPMN_3VUu--wtMPtBfLGaUNpyqteSy2QBYyRt5a4sW99J7CaIXlRvSqhlhInzIx_w0Ub5zgyYH3m6aGRVBB5o1_nDzKuwIDxVpwXiC71Fgy7DPphEhZiMoI-6wYncT8Him20t8dYfSvp3Hf4btg" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://lh4.googleusercontent.com/joGSt1p4URoLwDcElM4F9Wu15JmbKd43c1TWU4FFsr0tp1clvAloTWBqvLk-sYMSwnu6rMqgwAkfEecLy9H7FrWdZXezmao7yqyaSwSvlJ74IaU7QivRYoabIEI-UoYWaPsiODgDcuJ3jWk-rEEWFRpNf0nQwJ-Cl7WyEsPPZ_xXRs-ZF0AgsuexZg" alt="" width="563"><figcaption></figcaption></figure>
