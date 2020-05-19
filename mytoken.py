from itsdangerous import TimedJSONWebSignatureSerializer as TJWSSerializer
from itsdangerous import BadData
import time
import uuid
class Token():
    def __init__(self, data):
        self.__secret = str(uuid.uuid4())
        t = TJWSSerializer(secret_key=self.__secret, expires_in=3600)
        self.token = t.dumps(data).decode()

    def decode_token(self):
        t = TJWSSerializer(secret_key=self.__secret)
        try:
            res_data = t.loads(self.token)
        except BadData:
            print('解密失败')
        else:
           return res_data
