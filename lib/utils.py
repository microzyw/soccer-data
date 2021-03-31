import hashlib

class UtilsFunction:

    def getMD5(self, obj):
        return hashlib.md5(obj.encode(encoding='UTF-8')).hexdigest()