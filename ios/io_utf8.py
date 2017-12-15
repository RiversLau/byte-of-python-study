import io

f = io.open('hello.txt', 'wt', encoding='utf-8')
f.write('你好，世界')
f.close()

text = io.open('hello.txt', encoding='utf-8').read()
print(text)
