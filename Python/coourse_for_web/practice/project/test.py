import hashlib
from server import PASSWORD_SALT

old_password = "12345"
hash1 = hashlib.sha256((old_password + PASSWORD_SALT).encode()).hexdigest()
print(hash1)

old_password2 = "Diablo_535"
hash2 = hashlib.sha256((old_password2 + PASSWORD_SALT).encode()).hexdigest()
print(hash2)
