from api.application import ApplicationListAPI, ApplicationAPI
from api.cluster import ClusterListAPI, ClusterAPI
from api.user import UserListAPI, UserAPI


def init(api):
    api.add_resource(
        ApplicationListAPI,
        '/applications',
        endpoint='api/applications'
    )
    api.add_resource(
        ApplicationAPI,
        '/applications/<id>',
        endpoint='api/application'
    )
    api.add_resource(
        ClusterListAPI,
        '/clusters',
        endpoint='api/clusters'
    )
    api.add_resource(
        ClusterAPI,
        '/clusters/<id>',
        endpoint='api/cluster'
    )
    api.add_resource(
        UserListAPI,
        '/users',
        endpoint='api/users'
    )
    api.add_resource(
        UserAPI,
        '/users/<id>',
        endpoint='api/user'
    )
