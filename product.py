import pymysql

def find_product():

    conn = pymysql.connect(host='192.168.56.101', port=4567 ,user='project_naji',password='ghgh77',db='Convinience_store')
    cur = conn.cursor()

    select_product = "SELECT * FROM PRODUCT"
    cur.execute(select_product)
    res = cur.fetchall()

    # 상품 조회 성공
    if res:
        print("<상품 이름 \t 판매 단가 \t 재고 수량>")
        for row in res:
            print(row[1],"-", row[3],"원 -", row[4],"개")

    # 상품 조회 실패
    else:
        print("=============== 상품 조회 실패, 다시 시도하세요. ===============\n")

    print("\n")