import pymysql

conn = pymysql.connect(host='192.168.56.101', port=4567, user='project_naji', password='ghgh77', db='Convenience_store')
cur = conn.cursor()


def show_emp():
    # 직원 목록 출력 기능
    select_emp = "SELECT * FROM EMPLOYEE"
    cur.execute(select_emp)
    res = cur.fetchall()

    # 직원 목록 조회 성공
    if res:
        print("=============================================")
        print("  <직원 번호 \t 직원 이름>   ")
        for row in res:
            print("\t", row[0], " \t", row[1])
        print("=============================================")

    # 상품 조회 실패
    else:
        print("=============== 직원 조회 실패, 다시 시도하세요. ===============\n")

    print("\n")



def find_emp(emp_no):
    select_emp = "SELECT * FROM EMPLOYEE WHERE Emp_no = %s "
    cur.execute(select_emp, emp_no)
    res = cur.fetchall()

    #직원 조회 성공
    if res:
        res_emp_name = res[0][1]
        print("=============== 출근 직원: ", res_emp_name, "\n")
        return True

    # 직원 조회 실패
    else:
        print("=============== 직원 조회 실패, 다시 입력해주세요. ===============\n")
        return False
