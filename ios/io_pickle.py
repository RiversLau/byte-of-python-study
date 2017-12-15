import pickle

shopListFile = 'shoplist.data'
shopList = ['apple', 'mango', 'banana']

f = open(shopListFile, 'wb')
pickle.dump(shopList, f)
f.close()

del shopList

f = open(shopListFile, 'rb')
storedList = pickle.load(f)
print(storedList)

