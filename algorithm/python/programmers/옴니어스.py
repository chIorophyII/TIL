"""
DB 구조
DESCRIBE TAGGER_M;
+---------+--------------+------+-----+---------+-------+
|  Field  |     Type     | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+-------+
|   ID    |     int      |  NO  | PRI |  NULL   |       | <-----+
| NAME_EN | varchar(255) | YES  |     |  NULL   |       |     | |
| NAME_KO | varchar(255) | YES  |     |  NULL   |       |     | |
| NAME_ZH | varchar(255) | YES  |     |  NULL   |       |     | |
| NAME_JA | varchar(255) | YES  |     |  NULL   |       |     | |
+---------+--------------+------+-----+---------+-------+     | |
                                                              | |
DESCRIBE TAGGER_R;                                            | |
+-------------+------+------+-----+---------+-------+         | |
|    Field    | Type | Null | Key | Default | Extra |         | |
+-------------+------+------+-----+---------+-------+         | |
| CATEGORY_ID | int  | YES  | MUL |   NULL  |       |---------+ |
| ITEM_ID     | int  | YES  | MUL |   NULL  |       |-----------+
+-------------+------+------+-----+---------+-------+
"""

import sqlalchemy
import pytest
import re

from sqlalchemy.sql import text
from typing import List, Dict, Optional


def test_case1():
    service = Service()
    res = service.solution(" blue 밀리터리재킷&@*@ 7,000원 ")
    assert res == ["재킷", "밀리터리재킷"]


def test_case2():
    service = Service()
    res = service.solution(" Gown-Dress and 캐주얼상의 (10,000)")
    assert res == ["dresses", "gown-dress", "캐주얼상의", ""]


def test_case3():
    service = Service()
    res = service.solution("T恤衫")
    assert res == ["休闲上衣", "T恤衫"]


def test_case4():
    service = Service()
    res = service.solution(" blue밀리터리재킷&@*@ 7,000원 ")
    assert res == ["", ""]


def test_case5():
    service = Service()
    res = service.solution("Gracious life 피그먼트 스웨트셔츠 [Blue]_맨투맨")
    assert res == ["캐주얼상의", "스웨트셔츠"]


pytest.main()


class Mysql:
    def __init__(self):
        # Connect to the DB and reflect metadata.
        engine = sqlalchemy.create_engine('mysql://coderpad:@/coderpad?unix_socket=/tmp/mysql/socket/mysqld.sock')
        self.connection = engine.connect()

    def execute(self, query: str, data: Optional[dict] = None) -> List[Dict[str, any]]:
        """
        사용 예:
        res = Mysql().execute("SELECT * FROM TAGGER_M WHERE ID = :id", {"id": 1})

        참조: https://docs.sqlalchemy.org/en/14/core/sqlelement.html#sqlalchemy.sql.expression.text
        """
        query_result = self.connection.execute(text(query), data)
        return [{column: value for (column, value) in row._mapping.items()} for row in query_result]


class Service:
    def __init__(self):
        pass

    def language(self, search, result):
        en = Mysql().execute("SELECT * FROM TAGGER_M WHERE NAME_EN = :w", {"w": search})

        if en:
            return "NAME_EN"
        elif search == result[0]["NAME_KO"]:
            return "NAME_KO"
        elif search == result[0]["NAME_ZH"]:
            return "NAME_ZH"
        elif search == result[0]["NAME_JA"]:
            return "NAME_JA"
        else:
            pass

    def solution(self, product_name: str) -> List[str]:
        item_list = []
        words = product_name.split(" ")

        for word in words:
            # -를 뺀 특수문자 제거
            word = re.sub(r"[^\w\s\-]", "", word).strip()
            product = Mysql().execute(
                "SELECT * FROM TAGGER_M WHERE NAME_EN = :NAME OR NAME_KO = :NAME OR NAME_ZH = :NAME OR NAME_JA = :NAME",
                {"NAME": word})

            if product:
                item_r = Mysql().execute("SELECT * FROM TAGGER_R WHERE ITEM_ID = :id", {"id": product[0]["ID"]})

                # 아이템 이름일 때
                if item_r:
                    tag_m = Mysql().execute("SELECT * FROM TAGGER_M WHERE ID = :id", {"id": item_r[0]["CATEGORY_ID"]})

                    # 입력받은 상품명의 언어
                    word_lan = Service.language(self, word, product)

                    if word_lan == "NAME_EN":
                        word = product[0][word_lan]

                    item_list.extend([tag_m[0][word_lan], word])

                # 카테고리 이름일 때
                else:
                    item_list.extend([word, ""])

        # 빈 배열일 때
        if not item_list:
            item_list = ["", ""]

        return item_list