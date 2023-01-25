#
#  Copyright (C) Tessact Pvt. Ltd. - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Faiz P <faiz@tessact.com>, January 2023
#
from .common import Common
import os


class Container(Common):
    DEBUG = True
    INSTALLED_APPS = Common.INSTALLED_APPS

    ALLOWED_HOSTS = ["*"]
