# class BinarySearch(list):

#     def __init__(self, a, b):
#         # list.__init__(self, self.gen_list())
#         super(BinarySearch, self).__init__(self, a, b)
#         self.a = a #length 
#         self.b = b #step
#         self.length = 0
        

#     def gen_list(self):
#         list_out = []
#         count = 0
#         val = 0
#         while count <= self.a:
#             item = val+self.b
#             list_out.append(item) 
#         return list_out

#     def search(self, arg):
#         listin = self.gen_list()
#         top = len(listin)
#         bottom = 0
#         found = False
#         index = 0
#         count = 0
#         while bottom <= top and not found:
#             mid = (top + bottom) // 2
#             count = count + 1
#             if listin[mid] == arg:
#                 index = mid
#                 found = True
#             elif listin[mid] < arg:
#                 bottom = mid + 1
#             else:
#                 top = mid - 1
#         dic = {'count': count, 'index': index}
#         return dic

class ListComprehension:
    a = 0
    b = 0
    def __init__(self,a,b):
        self.a = a
        self.b = b
 
    def setA(self,a):
        self.a = a
    def setB(self,b):
        self.b = b
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getList(self,a,b):
        alist = []
        for x in range(b ,(a+1)*b)[::b]:
            alist.append(x)
        return alist
 
 
 
 
class BinarySearch(ListComprehension) :
    def __init__(self,a,b):
        super(BinarySearch,self).__init__(a,b)
    def search(self,item):
        alist = self.getList(self.a,self.b)
        first = 0
        last = len(alist)-1
        found = False
        count = 0
        dict_new = {}
        while first <= last and not found:
            midpoint = (first + last)//2
            if alist[midpoint] == item:
                found=True
            else:
                if item < alist[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
            count = count +1
        dict_new["count"] = count
        dict_new["index"] = alist.index(item)
        return dict_new