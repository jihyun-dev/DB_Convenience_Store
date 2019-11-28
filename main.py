# -*- coding: utf-8 -*-

from emp import *
from product import *
from orders import *


def print_menu():
    print("<<< 메뉴 >>> 1. 재고 확인 \t 2. 상품 입고 \t 3. 상품 판매 \t 4. 판매 내역 조회 \t 5. 시스템 종료 ")


start_work = True
global emp_no
print("\n********************************************* \n"
         "       편의점 상품 판매 및 재고 관리 시스템 \n"
         "********************************************* \n\n")

print("=============== <메뉴> \t 1. 직원 출근(start) \t 0. 시스템 종료(quit)")
start_work = int((input('<선택>: ')))

while start_work:
    if start_work == 1:
        # 직원 출근

        show_emp()
        print("<직원 출근> 출근할 근무자 번호를 입력하세요.")
        emp_no = str((input('근무자 번호: ')))
        find_emp(emp_no) # 근무자 번호 조회
        start_menu = True

    while start_menu:
        # 시스템 메인 메뉴
        print_menu()
        menu_num = int((input('선택: ')))
        if menu_num == 1:
            # 1. 재고 확인
            show_product()

        if menu_num == 2:
            # 2. 상품 입고
            put = True
            while put:
                print("<상품 입고> 입고된 상품의 정보를 입력하세요.")
                product_no = str((input('상품 번호: ')))
                product_name = str((input('상품 이름: ')))
                product_date = str((input('유통기한: ')))
                price = str((input('판매 단가: ')))
                product_quantity = int((input('입고 수량: ')))

                put_product(product_no, product_name, product_date, price, product_quantity)

                put = int((input('입고 입력을 계속하려면 1, 완료하였으면 0을 입력하세요.: ')))

        if menu_num == 3:
            # 3. 상품 판매
            show_product()
            print("<상품 판매> 판매 정보를 입력하세요.")
            product_no = str((input('상품 번호: ')))
            order_quantity = int((input('판매 수량: ')))
            cust_no = str((input('고객 번호: ')))
            payment_type = str((input('결제 방법: ')))


            create_orderno()
            # 주문 번호를 가장 '큰 번호 + 1'로 만들기 위한 함수
            exist_quantity = check_product(product_no, order_quantity)
            # 입력 수량만큼 판매가 가능한 지 확인하는 기능, 가능하면 재고 수량, 불가하면 False를 반환

            if exist_quantity:
                sell_product(product_no, order_quantity, cust_no, payment_type, emp_no, exist_quantity)
            else:
                print("**** 판매 불가 **** 재고가 부족합니다. 상품 수량을 다시 확인해주세요.")

        if menu_num == 4:
            show_orders()

        if menu_num == 5:
            # 시스템 종료
            start_menu = False
            start_work = False

print("===============  시스템이 종료되었습니다. \n")


