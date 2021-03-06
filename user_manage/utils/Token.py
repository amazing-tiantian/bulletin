from itsdangerous import URLSafeTimedSerializer as usts
import base64

# generate verify key

class Token():
    def __init__(self, security_key):
        self.security_key = security_key
        self.salt = base64.encodestring(security_key)

    def generate_validate_token(self, username):
        serializer = usts(self.security_key)
        return serializer.dumps(username, self.salt)

    def confirm_validate_token(self, token, expiration=3600):
        serializer = usts(self.security_key)
        return serializer.loads(token, salt=self.salt, max_age=expiration)

