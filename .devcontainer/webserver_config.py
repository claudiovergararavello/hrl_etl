import os
from airflow.www.security import AirflowSecurityManager
from flask_appbuilder.security.manager import AUTH_DB

AUTH_TYPE = AUTH_DB
AUTH_ROLE_ADMIN = 'Admin'
AUTH_ROLE_PUBLIC = 'Viewer'
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Admin"
'''
class FakeAuthManager(AirflowSecurityManager):
    def is_user_authenticated(self):
        return True

    def get_user(self):
        return self.get_user_by_username("admin")

SECURITY_MANAGER_CLASS = "airflow.www.security.AirflowSecurityManager"
'''
CSRF_ENABLED = False
