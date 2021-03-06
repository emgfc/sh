# sh: Flask + SQLAlchemy URL shortener

![Preview](./scrn.jpg)

Доступная функциональность:

* Генерация сокращенной ссылки, сопоставляемой с оригинальной ссылкой;
* Создание временных (до десяти минут) сокращенных ссылок;
* Создание одноразовых сокращенных ссылок.

Взаимодействие с фронтом идет по REST (эндпоинт `/links/`). Пример передаваемого и возвращаемого объекта:

```json
{
	"src": "https://example.com",
	"is_one_off": false,
	"expiring": true,
	"short": "aaabbcc",
	"deleted_at": "2036-10-07T01:02:03.265042"
}
```

Описание полей:

* `src` — исходная ссылка;
* `is_one_off` — флаг, определяющий одноразовость ссылки;
* `expiring` — флаг, определяющий необходимость удаления ссылки через десять минут.
* `short` (генерируется на сервере) — сокращение для ссылки;
* `deleted_at` (генерируется на сервере) — время удаления ссылки (если постоянная, то `null`).

