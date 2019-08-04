import base64
import hashlib


class HashGenerator():

    def generate_hash(self, arg):
        if arg is not None:
            b = arg.encode('unicode-escape')
            hasher = hashlib.sha1(b)
            return str(base64.urlsafe_b64encode(hasher.digest()[:10]))
