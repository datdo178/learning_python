from src.imports.entities.cloud.user_entity import UserCloud
from src.imports.data.config import config_data
from src.imports.entities.onpremise.user_entity import UserOnpre


def import_user():
    cloud_user_config_data = config_data['cloud']['user']
    cloud_is_enabled = cloud_user_config_data['enable']
    onpre_user_config_data = config_data['onpre']['user']
    onpre_is_enabled = onpre_user_config_data['enable']

    if cloud_is_enabled:
        user_flow = UserCloud()
        user_flow.create_import_file(cloud_user_config_data)

    if onpre_is_enabled:
        user_flow = UserOnpre()
        user_flow.create_import_file(onpre_user_config_data)


import_user()
