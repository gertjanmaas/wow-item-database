# WoW Item Database

Example project for docker workshop.

![](img/screenshot.png)

## Project setup

### Microservice

The microservice is written in Python and serves two functions:

1. Serving the API ( `GET /items` )
1. Serving the frontend ( `frontend/index.html` )

The frontend consists of a simple HTML page with some Bootstrap CSS and JQuery logic. It uses `fetch` to get the items from the API and sorts it by whatever the dropdown is set too.

### Database

The database required for this is a plain postgres database. For connection with the database the microservice needs to be injected with the following environment variables:

| Environment Variable | Explanation | Default value |
|----------------------|-------------|---------------|
| `DB_USER` | The username for the Postgres database | `postgres` |
| `DB_PASS` | The password for the Postgres database | `postgres` |
| `DB_HOST` | The host for the Postgres database | `localhost` |
| `DB_PORT` | The port for the Postgres database | 5432 |
| `DB_NAME` | The name for the Postgres database | `postgres` |

