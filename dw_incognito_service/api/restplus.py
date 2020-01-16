import logging

from flask_restplus import Api
from dw_incognito_service import settings

log = logging.getLogger(__name__)

api = Api(version='1.0', title='DW Anonymization API',
          description='A Flask RestPlus powered API to anonymization client PI data')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


