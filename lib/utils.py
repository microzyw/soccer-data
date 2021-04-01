import hashlib
import datetime
import urllib.request

class UtilsFunction:

    C_YYYYMMDD = "%Y%m%d"
    C_YYYYMMDDHHMMSS = "%Y%m%d%H%M%S"
    C_YYYY_MM_DD = "%Y-%m-%d"
    C_YYYY_MM_DD_HH_MM_SS = "%Y-%m-%d %H:%M:%S"
    C_HH_MM = "%H:%M"

    @staticmethod
    def getHtmlCode(url):
        user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
        headers = {
            'User-Agent': user_agent
        }
        req = urllib.request.Request(url, headers=headers, method='GET')
        html = urllib.request.urlopen(req).read().decode('utf-8')
        return html

    @staticmethod
    def isEmpty(obj):
        if obj is None: return True
        if obj == '': return True
        return False

    @staticmethod
    def formatTwoPoint(obj):
        try:
            floatValue = float(obj)
        except:
            floatValue = 0.00
        return format(floatValue, '.2f')
    
    @staticmethod
    def getMD5(obj):
        return hashlib.md5(obj.encode(encoding='UTF-8')).hexdigest()

    @staticmethod
    def getNowTime():
        return datetime.datetime.now()

    @staticmethod
    def getNowString(format):
        return datetime.datetime.now().strftime(format)

    @staticmethod
    def getDatetime(timestamp):
        return datetime.datetime.fromtimestamp(timestamp)

    @staticmethod
    def getTimestampString(timestamp, format):
        temp = ''
        if BaseFunction.isEmpty(timestamp):
            temp = ''
        else:
            if BaseFunction.isEmpty(format):
                temp = ''
            else:
                temp = datetime.datetime.fromtimestamp(timestamp).strftime(format)
        return temp