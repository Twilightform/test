print("하나","둘","셋",1,2,3)
print("하나","둘","셋",1,2,3,sep='-')
print("첫번째 값")
print("두번째 값")

print("첫번째 값", end=" ---> ")
print("두번째 값")

file = open("text.txt", "w")
print("hello Python!!", file=file)
file.close()