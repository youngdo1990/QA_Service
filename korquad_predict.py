# -*- coding: utf-8 -*-
import argparse
from string import punctuation
from bert import QA
import pymysql.cursors
import json
import time
import numpy as np
from bert import *


# # 두런 데이터베이스 접속 정보
HOST = "121.88.250.210"
USER = "dolearn"
PASS = "Enfjs!123"
DB = "dolearn"


def db2doc(uid, table_name="_youtube_fulldata_timestamp"):
    # table_name 디폴트 값은 동영상 대본 내용 담은 테이블입니다.

    doc = ""
    # 두런 데이터베이스 연결
    connection = pymysql.connect(host= HOST,
                            user=USER,
                            password=PASS,
                            database=DB)

    # 데이터베이스 쿼리
    with connection:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM ' + table_name + ' WHERE `uid`="' + uid + '" ORDER BY `paragraph_idx`'
            cursor.execute(sql)

            # 동영상 타임스템프로 나누어 둔 문장 붙여넣기
            result = cursor.fetchall()
            for line in result:
                doc += line[3] + "\n"
    
    return doc


def get_answer(doc, q, model):
    # 모델 적재
    # model = QA('./output')
    answer = model.predict(doc,q)
    # for ans in answer:
    #     print(f"{ans} --> {answer[ans]}")
    return answer['answer'], answer['confidence']
# HmVAN1xq9KI

def make_prediction(uid, q, model):
    doc = db2doc(uid)
    start_time = time.time()
    answer, confidence = get_answer(doc=doc, q=q, model=model)
    total_time = time.time() - start_time
    # answer = "뭐야??"
    # JSON 정보 반화
    #answer = np.array(answer)
    #confidence = np.array(confidence)
    #content = {"uid": uid, "answer": answer, "confidence": confidence}
    # print(answer)
    content = json.dumps([uid,answer,confidence])
    # d = json.dumps(content)
    return str(content)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="uid" , help="동영상의 uid")
    parser.add_argument(dest="q", help="원하시는 질문")
    args = parser.parse_args()
    uid = args.uid
    q = args.q
    model = QA('./output')
    return make_prediction(uid=uid, q=q, model=model)

if __name__ == "__main__":
    # main()
    model = QA('./output')
    uid = "qkEd_HVrAxg"
    q = "엑셀%20파일20%어떻게%저장해야%20해?"
    prediction = make_prediction(uid, q, model)
    print(prediction)
