import pymysql


def show_orders():

    conn = pymysql.connect(host='192.168.56.101', port=4567 ,user='project_naji',password='ghgh77',
                           db='Convenience_store')
    cur = conn.cursor()

    show_orders = "SELECT o.Order_no, o.Order_date, o.Order_time, c.Cust_name, p.Product_name, p.Price," \
                  "ol.Order_quantity, e.Emp_name, o.Payment_type FROM ORDER_LIST ol, ORDERS o,PRODUCT p, EMPLOYEE e, CUSTOMER c" \
                  " WHERE o.Order_no = ol.Order_no AND ol.Product_no = p.Product_no AND o.Emp_no = e.Emp_no and c.Cust_no = o.Cust_no"
    # select_data = (Order_no, Order_no)
    cur.execute(show_orders)
    res = cur.fetchall()

    #판매 내역 조회 성공
    print("\n============================================================================ 판매 내역 "
          "===============================================================================")

    if res:
        for row in res:
            print("판매 번호: ", row[0], ", 판매 일시: ", row[1], row[2], ", 고객 이름: ", row[3], ", 상품 이름: ", row[4],
                  ",판매 가격: ", row[5], ", 판매 수량: ", row[6], ", 판매자 이름: ", row[7], ", 결제 방법: ", row[8])
        print("=================================================================================================="
              "=================================================================\n")

    # 판매 내역 조회 실패
    else:
        print("=============== 판매 내역 조회 실패, 다시 시도해주세요. ===============\n")

