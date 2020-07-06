def add_info():
    print('添加名片')


def del_user():
    print('删除名片')


def modify_info():
    print('修改名片')


def query_info():
    print('查询名片')


def show_al():
    print('显示所有名片')


def quit_system():
    # print('退出系统')
    answer = input('亲, 你确定要退出么?~~~~(> _ <)~~~~(yes or no)')
    # if answer.lower() == 'yes':
    #     return True
    # return False
    return answer.lower() == 'yes'


def start():
    while True:
        print("""---------------------------
        名片管理系统 V1.0
 1:添加名片
 2:删除名片
 3:修改名片
 4:查询名片
 5:显示所有名片
 6:退出系统
---------------------------""")
        operator = input('请输入要进行的操作(数字)')

        if operator == '1':
            add_info()
        elif operator == '2':
            del_user()
        elif operator == '3':
            modify_info()
        elif operator == '4':
            query_info()
        elif operator == '5':
            show_al()
        elif operator == '6':
            if quit_system():
                break
        else:
            print('输入有误,请重新输入......')


start()
