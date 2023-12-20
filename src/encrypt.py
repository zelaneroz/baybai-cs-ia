from passlib.context import CryptContext

pwd_config = CryptContext(schemes=["pbkdf2_sha256"],
                            default="pbkdf2_sha256",
                            pbkdf2_sha256__default_rounds=30000
                            )

def encrypt_password(user_password):
    return pwd_config.encrypt(user_password)

def check_password(user_password,hashed):
    return pwd_config.verify(user_password,hashed)


