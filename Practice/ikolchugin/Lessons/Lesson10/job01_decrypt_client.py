import socket
import random
import time
import pickle
from job01_crypto import encrypt

class TcpClient:
    def __init__(self, host, port, encrypted):
        self.host = host
        self.port = port
        self._encrypted = encrypted
        self._decrypted = None
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        time.sleep(0.1)
        self._socket.send(pickle.dumps(self._encrypted))
        print(f'Sent encrypted: {self._encrypted}')
        self._decrypted = pickle.loads(self._socket.recv(1024))
        print(f'Received decrypted: {self._decrypted}')
        self._socket.close()


if __name__ == '__main__':
    with open('crypt_dict.bin', 'rb') as f:
        secret_dict = pickle.load(f)

    # print(secret_dict)
    encrypted_words = [
        encrypt(f'word{i}', secret_dict) for i in range(30)
    ]
    name = 'Python client ' + str(random.randint(1, 1000))
    # print(encrypted_words)
    myclient = TcpClient(host='127.0.0.1', port=9292, encrypted=encrypted_words)
    myclient.run()