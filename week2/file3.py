#with구문을 써서 파일을 열면 close처리를 안해줘도 된다.

# f = open("foo.txt", "w")
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")