import pymysql
# 상품 판매 시간을 위한 모듈
import time
from datetime import datetime

conn = pymysql.connect(host='192.168.56.101', port=4567, user='project_naji', password='ghgh77', db='Convenience_store')
cur = conn.cursor()


def show_product():
    # 재고 확인 기능
    select_product = "SELECT * FROM PRODUCT"
    cur.execute(select_product)
    res = cur.fetchall()

    # 상품 조회 성공
    if res:
        print("=============================================")
        print("  <상품 번호 \t 상품 이름 \t 판매 단가 \t 재고 수량>   ")
        for row in res:
            print(row[0],"-", row[1],"-", row[3],"원 -", row[4],"개")
        print("=============================================")

    # 상품 조회 실패
    else:
        print("=============== 상품 조회 실패, 다시 시도하세요. ===============\n")

    print("\n")


def put_product(product_no, product_name, product_date, price, product_quantity):
    # 상품 입고 기능
    select_product = "SELECT * FROM PRODUCT WHERE Product_no = %s"
    cur.execute(select_product, product_no)
    res = cur.fetchall()

    if res:
        # 이미 존재하는 상품이므로, 재고 수량만 늘림
        print("res true1")

        exist_quantity = int(res[0][4])

        print("true2")
        quantity = exist_quantity + product_quantity
        print(quantity)
        update_product = "UPDATE PRODUCT SET Product_quantity = %s WHERE Product_no = %s"
        update_data = (quantity, product_no)
        cur.execute(update_product, update_data)

    else:
        # 존재하지 않는 상품은 PRODUCT 테이블에 입력된 정보를 insert
        insert_product = 'INSERT INTO PRODUCT VALUES ( %s, %s, %s, %s, %s)'
        insert_data = (product_no, product_name, product_date, price, product_quantity)
        cur.execute(insert_product, insert_data)

    conn.commit()

    print("상품 입고 완료: ", product_no, product_name, product_date, price, product_quantity)


def create_orderno():
    # 주문 번호를 가장 '큰 번호 + 1'로 만들기 위한 기능
    find_orderno = "SELECT MAX(Order_no) FROM ORDERS"
    cur.execute(find_orderno)
    res = cur.fetchall()
    return int(res[0][0])


def check_product(product_no, order_quantity):

    # 1. 입력한 상품 번호의 상품이 존재하는 지 확인하는 기
    select_quantity = "SELECT Product_quantity FROM PRODUCT WHERE Product_no = %s"
    cur.execute(select_quantity, product_no)
    res = cur.fetchall()

    if bool(res) is False :
        print("**** 판매 불가 ****")
        return False

    # 2. 입력 수량만큼 판매가 가능한 지 확인하는 기능
    while res:
        exist_quantity = int(res[0][0])

        if exist_quantity >= order_quantity:
            return exist_quantity
        else:
            print("상품이 존재하지 않거나, 재고가 부족합니다. 상품 번호와 수량을 다시 확인해주세요.")
            return False


def sell_product(product_no, order_quantity, cust_no, payment_type, emp_no, exist_quantity):
    # 상품 판매 기능

    # 1. 판매 정보 DB에 추가
    time = datetime.now()
    sell_date = str(time.year) + "-" + str(time.month) + "-" + str(time.day)
    sell_time = str(time.hour) + ":" + str(time.minute)
    order_no = str(create_orderno() + 1)

         # ORDER 테이블 insert
    insert_order = "INSERT INTO ORDERS VALUES (%s, %s, %s, %s, %s, %s)"
    order_data = (order_no, cust_no, emp_no, sell_date, sell_time, payment_type)
    cur.execute(insert_order, order_data)

         # ORDER_LIST 테이블 insert
    insert_orderlist = "INSERT INTO ORDER_LIST VALUES (%s, %s, %s)"
    orderlist_data = (order_no, product_no, str(order_quantity))
    cur.execute(insert_orderlist, orderlist_data)

    # 2. 상품 수량 변경
    change_quantity = exist_quantity - order_quantity
    update_product = "UPDATE PRODUCT SET Product_quantity = %s WHERE Product_no = %s"
    update_data = (change_quantity, product_no)
    cur.execute(update_product, update_data)

    print("=============== 상품 판매 완료. 감사합니다. ===============\n")
    conn.commit()
    show_product()

