import pymysql

def find_emp(emp_no):

    conn = pymysql.connect(host='192.168.56.101', port=4567 ,user='project_naji',password='ghgh77',
                           db='Convenience_store')
    cur = conn.cursor()

    select_emp = "SELECT * FROM EMPLOYEE WHERE Emp_no = %s "
    cur.execute(select_emp, emp_no)
    res = cur.fetchall()

    #직원 조회 성공
    if res:
        res_emp_name = res[0][1]
        print("=============== 출근 직원: ", res_emp_name)

    # 직원 조회 실패
    else:
        print("=============== 직원 조회 실패, 다시 입력해주세요. ===============\n")
