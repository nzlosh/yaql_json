import json
import sys
import traceback

from mistral import exceptions as mistral_exceptions
from oslo_log import log as logging
LOG = logging.getLogger(__name__)


def to_json(context, obj=None):
    tmp = None
    try:
        tmp = json.dumps(obj)
        LOG.info("JSON to string produced : {} {}.".format(tmp, type(tmp)))
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        LOG.error("{}\n{}\n{}\n".format(exc_type, exc_value, exc_traceback))
        raise mistral_exceptions.YaqlEvaluationException(
            'Error converting object to JSON: {} {} {}'.format(exc_type, exc_value, exc_traceback)
        )
    return tmp


def from_json(context, obj=None):
    tmp = None
    try:
        tmp = json.loads(obj)
        LOG.info("String to JSON produced : {} {}.".format(tmp, type(tmp)))
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        LOG.error("{}\n{}\n{}\n".format(exc_type, exc_value, exc_traceback))
        raise mistral_exceptions.YaqlEvaluationException(
            'Error converting JSON to object {} {} {}'.format(exc_type, exc_value, exc_traceback)
        )
    return tmp
