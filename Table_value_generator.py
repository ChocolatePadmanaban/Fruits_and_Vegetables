

def GenerateList(Filename="2020-07-24_03-20-47"):
    with open(Filename,'r') as f_read:
        f_list= f_read.readlines()
        print(f_list[264:1383:11])
        with open("Fruits_and_Vegetables_list.txt", 'w') as list_write:
            for f_v in f_list[264:1383:11]:
                list_write.write(f_v)


if __name__ == "__main__":
    GenerateList()