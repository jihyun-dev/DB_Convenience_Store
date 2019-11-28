import pymysql

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

