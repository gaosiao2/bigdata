f = open(r"/root/files/part-r-00000", "r")
lines = f.readlines()

flag= False
i=0
for line in lines:
    if "\t" not in line:
        print("请检查分隔符是否为 \t，以下是检测出来的数据：")
        print(line)
        flag = False
        break;

    if len(line.split("\t"))!=18:
        print("数据长度不为18，请检查数据长度是否完整，以下是检测出来的不完整数据：")
        print(line)
        flag=False
        break;

    if line.split("\t")[0]=="date_time":
        print("首列没有删除，请重试！")
        flag=False
        break;

    if len(line.split("\t")[0].split(" ")[1].split(":"))!=2:
        print("日期转换失败！，请重试")
        flag=False
        break;

    if len(line.split("\t")[16].split(".")[1].strip()) != 2:
        print("H_data 没有保存为两位小数，以下是你的数据：")
        print(line)
        flag = False
        break
    else:
        flag= True

    if len(line.split('\t')[17].split(".")[1].strip())!=2:
        print("AH_data 没有保存为两位小数，以下是你的数据：")
        print(line)
        flag = False
        break
    else:
        flag= True
    i = i + 1


if flag:
    print("共清洗："+str(2108631-i)+"行")
    print("日期转换成功")
    print("首列清洗成功")
    print("保存两位小数操作成功")

