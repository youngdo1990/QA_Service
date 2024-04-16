# -*- coding: utf-8 -*-
import pysftp

def download_model():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None  
    with pysftp.Connection("112.160.206.172", port=5333, username="user", password="dbwj!1", cnopts=cnopts) as sftp:
        with sftp.cd("/data/alvaro/question_answering/output"):
            # print(sftp.listdir())
            sftp.get("pytorch_model.bin")


if __name__ == "__main__":
    download_model()
