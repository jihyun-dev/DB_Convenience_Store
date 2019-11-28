# -*- coding: utf-8 -*-

from emp import *
from product import *


def print_menu():
    print("=============== <메뉴> 1. 재고 확인 \t 2. 상품 입고 \t 3. 상품 판매 \t 4. 판매 내역 조회 5. 시스템 종료 ")


print("===============  편의점 상품 판매 및 재고 관리 시스템\n")

print("=============== <메뉴> \t 1. 직원 출근(start) \t 2. 시스템 종료(quit)")
start_work = int((input('<선택>: ')))

if start_work == 1:
    # 직원 출근

    print("<직원 출근> 출근할 근무자 번호를 입력하세요.")
    emp_no = int((input('근무자 번호: ')))
    find_emp(emp_no) # 근무자 번호 조회

while start_work:
    # 시스템 메인 메뉴
    print_menu()
    menu_num = int((input('선택: ')))
    if menu_num == 1:
        # 1. 재고 확인
        find_product()

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

            put = int((input('입고 정보 입력을 계속하려면 1, 완료하였으면 0을 입력하세요.: ')))

    if menu_num == 3:
        # 3. 상품 판매
        find_product()
        print("판매할 상품 번호를 입력하세요.: ")

if start_work == 2:
    # 시스템 종료
    start_work = False
    print("===============  시스템이 종료되었습니다.  ========================================\n")


