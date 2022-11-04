def field(items, *args):
   assert len(args) > 0
   d = dict()
   l = []
   for i in range(len(items)):
       if len(args)==1:
           if items[i].get(args[0])!=None:
               l.append(items[i].get(args[0]))
       else:
           c = 0
           for j in range(len(args)):
               if items[i].get(args[j])!=None:
                   c+=1
           if c>0:
               l.append(items[i])

   return l

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'price': 5300, 'color': 'black'},
    {'vov': 58, 'sfs': 'efa'}
        ]

def main1():

    print(field(goods, 'title'))
    print(field(goods, 'title', 'price'))

if __name__ == '__main__':
    main1()