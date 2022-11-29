# import first
# print("####################################",first.__name__)
def sum1(file_obj):
    data = file_obj.read()
    return sum(map(int, data.split()))

if __name__ == "__main__":
    with open("testfile.txt", "r") as f1:
        print(sum1(f1))