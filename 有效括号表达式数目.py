'''问题：统计给出列表括号表达式中，可以构成有效表达式数目
'''

def get_pairs(paris_list):
    leftmap = {}
    rightmap = {}
    stack = []
    com = 0
#     sumpairs=0
    for pairs in paris_list:
        print("paris: ",pairs)
        for s in pairs:
            if s=="(": # 检查字符是否为左括号，左括号推入栈中
                stack.append(s)
            else: # 此时字符为右括号
                # 栈空时，将字符加入栈中
                if len(stack)==0:
                    stack.append(s)
                else:
                    # 栈顶为左括号，匹配成功弹出元素
                    if stack[-1]=="(":
                        stack.pop()
                    else:# 无法匹配，字符入栈
                        stack.append(s)
        print("stack ",stack)
        # 若栈为空，则说明可以匹配出有效括号
        if len(stack)==0:
            com += 1
            continue
        
        # 若栈不为空，统计栈中剩余的字符种类
        ln = rn = 0
        while len(stack)>0:
            top = stack.pop()
            if top=="(":ln+= 1
            elif top==")":rn+=1
        
        # 原始字符串中的左右括号一定会被匹配出来，并筛选掉，所以栈中只会存在一种括号
        # 仅剩下右括号
        if ln==0:
            if rn in rightmap.keys():
                rightmap[rn] += 1
            else:
                rightmap.update({rn:1})
        
        # 仅剩下左括号
        if rn==0:
            if ln in leftmap:
                leftmap[ln] += 1
            else:
                leftmap.update({ln:1})
        print("lr %d, rn %d"%(ln,rn))
        print("--------step-------------")
    
    # 统计所有的字符串列表中，能够构成有效括号的数目
    sumpairs = com*com
    print("leftmap: ",leftmap)
    print("rightmap: ", rightmap)
    # 检查leftmap/rightmap是否存在相同键值，若存在则可构成有效括号表达式
    for key in leftmap.keys():
        r = rightmap[key] if key in rightmap.keys() else 0
        sumpairs += r*leftmap[key]
        
    return sumpairs


pairs_list=["(()",")))))","()()()","(((","))"]

pairs=[]
for i in pairs_list:
    pairs.append(list(i))

get_pairs(pairs)

'''测试结果:
 paris:  ['(', '(', ')']
stack  ['(']
lr 1, rn 0
--------step-------------
paris:  [')', ')', ')', ')', ')']
stack  [')', ')', ')', ')', ')']
lr 0, rn 5
--------step-------------
paris:  ['(', ')', '(', ')', '(', ')']
stack  []
paris:  ['(', '(', '(']
stack  ['(', '(', '(']
lr 3, rn 0
--------step-------------
paris:  [')', ')']
stack  [')', ')']
lr 0, rn 2
--------step-------------
com:  1
leftmap:  {1: 1, 3: 1}
rightmap:  {5: 1, 2: 1}

result->1
'''