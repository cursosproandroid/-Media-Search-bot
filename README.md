## [Media Search bot](https://github.com/cursosproandroid/Media-Search-bot)

* Indexar archivos de canal/grupo para búsqueda en línea.
* Cuando vaya a publicar un archivo en el canal/grupo de telegram, este bot lo guardará en la base de datos, por lo que puede buscarlo fácilmente en el modo en línea (inline mode).
* Admite formatos de archivo de documento, video y audio con subtítulos.

### Instalación

#### Forma fácil, en Heroku
[![Implementar](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/cursosproandroid/Media-Search-bot)

#### Forma difícil, implementa el bot en tu vps

```sh
python3 -m venv env
. ./env/bin/activate
pip3 install -r requirements.txt
# Edite info.py con variables como se indica a continuación
python3 bot.py
```
Compruebe `sample_info.py` antes de editar el archivo` info.py`

#### Variables

##### Variables requeridas
* `BOT_TOKEN`: Crea un bot utilizando [@BotFather](https://telegram.dog/BotFather), y obtén el token de la API de Telegram.
* `API_ID`: Obtén este valor desde [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Obtén este valor desde [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Nombre de usuario o ID del canal o grupo. Separe varios ID por espacio. Obtén este valor desde @googleimgbot
* `ADMINS`: ID del administrador del bot. Separe varios administradores por espacio. Obtén este valor desde @googleimgbot
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Obtén este valor desde [mongoDB](https://www.mongodb.com).
* `DATABASE_NAME`:Nombre de la base de datos en [mongoDB](https://www.mongodb.com).

##### Variables opcionales
* `COLLECTION_NAME`: Nombre de las colecciones. Por defecto es Telegram_files. Si va a utilizar la misma base de datos, utilice un nombre de colección diferente para cada bot
* `MAX_RESULTS`: Límite máximo de resultados de búsqueda en línea
* `CACHE_TIME`: La cantidad máxima de tiempo en segundos que el resultado de la consulta en línea puede almacenarse en caché en el servidor.
* `USE_CAPTION_FILTER`: Si el bot debe usar subtítulos para mejorar los resultados de búsqueda. (True o False)
* `AUTH_USERS`: Nombre de usuario o ID de los usuarios para dar acceso a la búsqueda en línea. Separe a varios usuarios por espacio. Déjelo vacío si no desea restringir el uso del bot.

### Comandos de los administradores
```
channel - Obtenga información básica sobre los canales
total - Mostrar el total de archivos guardados
delete - Eliminar archivo de la base de datos
logger - Obtener el registro del archivo
```

### Consejos
* Ejecute el archivo [one_time_indexer.py](one_time_indexer.py) para guardar archivos antiguos en la base de datos que aún no están indexados.
* Puede utilizar `|` para separar la consulta y el tipo de archivo mientras busca un tipo específico de archivo. Por ejemplo: `Avengers | video`
* Si no desea crear un canal o grupo, use su ID de chat/nombre de usuario como ID de canal. Entonces cuando envíe un archivo al bot, se guardará en la base de datos.

#### Para consultas y soporte, contacte a [Skueletor](https://telegram.dog/DKzippO)

## Créditos:

* [Cursos Pro Android](https://t.me/joinchat/VDY6seEnkeKdZNRM) 

### Licencia
Código publicado bajo [La licencia pública general GNU](LICENSE).
