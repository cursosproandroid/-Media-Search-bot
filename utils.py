# Cursos Pro Android by Skueletor ©️ 2021
import re
import logging
from pymongo.errors import DuplicateKeyError
from umongo import Instance, Document, fields
from motor.motor_asyncio import AsyncIOMotorClient
from marshmallow.exceptions import ValidationError
from info import DATABASE_URI, DATABASE_NAME, COLLECTION_NAME, USE_CAPTION_FILTER

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

client = AsyncIOMotorClient(DATABASE_URI)
db = client[DATABASE_NAME]
instance = Instance(db)


@instance.register
class Media(Document):
    file_id = fields.StrField(attribute='_id')
    file_ref = fields.StrField()
    file_name = fields.StrField(required=True)
    file_size = fields.IntField(required=True)
    file_type = fields.StrField()
    mime_type = fields.StrField()
    caption = fields.StrField()

    class Meta:
        collection_name = COLLECTION_NAME


async def save_file(media):
    """Save file in database"""

    try:
        file = Media(
            file_id=media.file_id,
            file_ref=media.file_ref,
            file_name=media.file_name,
            file_size=media.file_size,
            file_type=media.file_type,
            mime_type=media.mime_type,
        )
    except ValidationError:
        logger.exception('Se produjo un error al guardar el archivo en la base de datos')
    else:
        caption = media.caption
        if caption:
            file.caption = caption

        try:
            await file.commit()
        except DuplicateKeyError:
            logger.warning(media.file_name + " ya está guardado en la base de datos")
        else:
            logger.info(media.file_name + " se guarda en la base de datos")


async def get_search_results(query, file_type=None, max_results=10, offset=0):
    """Para la devolución de las búsquedas determinadas (resultados, next_offset)"""

    raw_pattern = query.lower().strip().replace(' ', '.*')
    if not raw_pattern:
        raw_pattern = '.'

    try:
        regex = re.compile(raw_pattern, flags=re.IGNORECASE)
    except:
        return []

    if USE_CAPTION_FILTER:
        filter = {'$or': [{'file_name': regex}, {'caption': regex}]}
    else:
        filter = {'file_name': regex}

    if file_type:
        filter['file_type'] = file_type

    total_results = await Media.count_documents(filter)
    next_offset = offset + max_results

    if next_offset > total_results:
        next_offset = ''

    cursor = Media.find(filter)
    # Ordenar por reciente
    cursor.sort('$natural', -1)
    # Cortar archivos según el desplazamiento y los resultados máximos
    cursor.skip(offset).limit(max_results)
    # Obtener lista de archivos
    files = await cursor.to_list(length=max_results)

    return files, next_offset
