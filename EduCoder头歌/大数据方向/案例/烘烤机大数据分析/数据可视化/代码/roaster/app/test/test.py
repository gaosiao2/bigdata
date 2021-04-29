def list_parse(list1):
    list2=[]
    for list in list1:
        a=list/max(list1)
        list2.append(float('%.4f' % a))
    return list2

if __name__ == '__main__':
    list111=[403.41,401.05,404.55,403.95,366.95]
    print(list_parse(list111))
