import hashlib

class UtilsFunction:

    def getMD5(obj):
        return hashlib.md5(obj.encode(encoding='UTF-8')).hexdigest()