import json

contacts = []

# 讀取檔案
filepath = r'C:\Users\brian\Documents\Python\contacts_system_project\contacts.txt'
with open(filepath, 'r', encoding='utf-8') as file:
    for item in file:
        contacts.append(json.loads(item.strip()))

# 顯示所有聯絡人函式
def show_all(contacts):
    for index, data in enumerate(contacts, 1):
        print(f'{index}.  {data["name"]}  {data["phone"]}  {data["mail"]}')

while True:
    print('1. 顯示所有聯絡人')
    print('2. 新增聯絡人')
    print('3. 刪除聯絡人')
    print('4. 搜尋聯絡人')
    print('5. 修改聯絡人資料')
    print('6. 離開程式')

    # 功能選擇, 判斷是否有效
    while True:
        try:
            choice = int(input('要使用什麼功能(1~6) : '))
            if 1 <= choice <= 6:
                break
        except ValueError:
            print('請輸入有效功能')
            continue

    if choice == 1: # 顯示
        if not contacts:
            print('無聯絡人 請先新增聯絡人')
        else:
            show_all(contacts)

    elif choice == 2: # 新增
        new_name = input('請輸入聯絡人姓名 : ')
        new_phone = input('請輸入聯絡人電話 : ')
        new_mail = input('請輸入聯絡人信箱 : ')

        contacts.append({'name':new_name, 'phone':new_phone, 'mail':new_mail})

        print(f'新增{new_name}到聯絡人')

    elif choice == 3: # 刪除
        if not contacts:
            print('無聯絡人 請先新增聯絡人')
        else:
            show_all(contacts)

            while True:
                try:
                    delete = int(input('請輸入要刪除聯絡人的編號 : '))
                    if 1 <= delete <= len(contacts):
                        break
                    else:
                        print('請輸入現有的聯絡人編號')
                except ValueError:
                    print('請輸入有效編號')
                    continue

            remove = contacts.pop(delete - 1)
            print(f'已刪除{remove["name"]}')

    elif choice == 4: # 搜尋
        if not contacts:
            print('無聯絡人 請先新增聯絡人')
        else:
            while True:
                try:
                    search = int(input('請輸入以什麼搜尋 (1.姓名 2.電話 3.信箱) : '))
                    if 1 <= search <= 3:
                        break
                    else:
                        print('請輸入正確的搜尋項目')
                except ValueError:
                    print('請輸入正確數字 (1.姓名 2.電話 3.信箱)')
                    continue

            found = False
            if search == 1:
                searching = input('請輸入姓名 : ')
                for data in contacts:
                    if searching in data['name']:
                        print(f'你搜尋的聯絡人資料 {data['name']}  {data['phone']}  {data['mail']}')
                        found = True
                if not found:
                    print('未搜尋到該聯絡人')
            elif search == 2:
                searching = input('請輸入電話 : ')
                for data in contacts:
                    if searching in data['phone']:
                        print(f'你搜尋的聯絡人資料 {data['name']}  {data['phone']}  {data['mail']}')
                        found = True
                if not found:
                    print('未搜尋到該聯絡人')
            elif search == 3:
                searching in input('請輸入信箱 : ')
                for data in contacts:
                    if searching == data['mail']:
                        print(f'你搜尋的聯絡人資料 {data['name']}  {data['phone']}  {data['mail']}')
                        found = True
                if not found:
                    print('未搜尋到該聯絡人')

    elif choice == 5: # 修改
        if not contacts:
            print('無聯絡人 請先新增聯絡人')
        else:
            show_all(contacts)

            while True:
                try:
                    change = int(input('請輸入要修改的聯絡人編號'))
                    if 1 <= change <= len(contacts):
                        break
                    else:
                        print('請輸入現有的聯絡人編號')
                except ValueError:
                    print('請輸入有效編號')
                    continue

            # 選擇修改項目, 判斷輸入是否正確
            while True:
                try:
                    change_what = int(input('請輸入要修改的項目 (1.姓名 2.電話 3.信箱) : '))
                    if 1 <= change_what <= 3:
                        break
                    else:
                        print('請輸入正確的修改項目')
                except ValueError:
                    print('請輸入正確數字 (1.姓名 2.電話 3.信箱)')
                    continue

            if change_what == 1:
                new = input('請輸入新聯絡人姓名 : ')
                contacts[change - 1]['name'] = new
            elif change_what == 2:
                new = input('請輸入新聯絡人電話 : ')
                contacts[change - 1]['phone'] = new
            elif change_what == 3:
                new = input('請輸入新聯絡人信箱 : ')
                contacts[change - 1]['mail'] = new

    elif choice == 6: # 結束
        #儲存檔案
        with open(filepath, 'w', encoding='utf-8') as file:
            for item in contacts:
                file.write(json.dumps(item) + '\n')

        print('結束程式')
        break