import base64
import os
import re
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key_base64 = '1qck4mmSyJ+YQ10PKzdZ6+J6AuvUAR8TS/7AiIDNyTA='
key = base64.b64decode(key_base64)
iv = b'\x00' * 16  # 和 Node.js 的 Buffer.alloc(16) 等价


class EncryptionHelper:
    @staticmethod
    def aes_decrypt(data: bytes) -> str:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(data)
        # Node.js 开了 autoPadding，对应 PKCS7
        decrypted = unpad(decrypted, AES.block_size)
        return decrypted.decode('utf-8', errors='ignore')


def find_version_directory(base_dir: str):
    return base_dir


def main():
    dest_file_name = 'app.conf.dat'
    app_dir = r'C:\Users\Administrator\Desktop\hyp\2.7.5_srbeta_1.4.1.192'

    version_dir = find_version_directory(app_dir)
    if not version_dir:
        print('未找到有效版本目录')
        return

    file_path = os.path.join(version_dir, dest_file_name)

    try:
        with open(file_path, 'rb') as f:
            buffer = f.read()

        decrypted_content = EncryptionHelper.aes_decrypt(buffer)
        print('解密内容:', decrypted_content)

    except Exception as e:
        print('解密失败:', str(e))


if __name__ == '__main__':
    main()
