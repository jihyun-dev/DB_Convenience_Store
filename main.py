from emp import *
from product import *

start_work = True

print("===============  편의점 상품 판매 및 재고 관리 시스템\n")

while start_work:
    print("=============== <메뉴> \t 1. 직원 출근(start) \t 2. 시스템 종료(quit)")
    start_work = int((input('<선택>: ')))

    if start_work == 1:
        # 1. 직원 출근

        print("<직원 출근> 출근할 근무자 번호를 입력하세요.")
        emp_no = int((input('근무자 번호: ')))
        find_emp(emp_no) # 근무자 번호 조회

        # 시스템 메인 메뉴
        print("=============== <메뉴> 1. 재고 확인 \t 2. 상품 입고 \t 3. 상품 판매 \t 4. 판매 내역 조회 ")
        menu_num = int((input('선택: ')))
        find_product()


    if start_work == 2:
        # 2. 시스템 종료
        start_work = False

print("===============  시스템이 종료되었습니다.  ========================================\n")

