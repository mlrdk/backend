from flask_restplus.fields import String
from .. import api


post_fields = api.model(
    'Post Service',
    {
        'service_id': String(),
    },
)
