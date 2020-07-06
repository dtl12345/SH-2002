user_list = [{'name': 'zhangsan', 'tel': '123', 'qq': '321'},
             {'name': 'lisi', 'tel': '456', 'qq': '654'},
             {'name': 'wangwu', 'tel': '789', 'qq': '987'},
             ]


def add_info():
    # print('添加名片')

    # 1. 使用input语句，接收用户的输入
    name = input('请输入姓名:')

    # 4. 用户输入完成以后，查看用户名是否存在
    for user in user_list:  # 4.1 遍历user_list列表
        if user['name'] == name:  # 如果发现列表里有相同的姓名
            print('此用户名已经被占用,请重新输入')  # 提示用户，姓名已经被占用了
            return  # 直接使用return结束整个函数
            # break  # 不需要再使用break

    tel = input('请输入手机号:')
    qq = input('请输入QQ号:')

    # 2. 使用字典的形式将数据保存
    user_dict = {'name': name, 'tel': tel, 'qq': qq}

    # 3. 把创建好的用户添加到用户列表里
    user_list.append(user_dict)

    print(user_list)


def del_user():
    print('删除名片')


def modify_info():
    print('修改名片')


def query_info():
    print('查询名片')


def show_al():
    # print('显示所有名片')
    print('序号	姓名		手机号		QQ')
    for i, user in enumerate(user_list):
        print(i, user['name'].center(15), user['tel'].center(10), user['qq'].center(10))


def quit_system():
    answer = input('亲, 你确定要退出么?~~~~(> _ <)~~~~(yes or no)')
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
