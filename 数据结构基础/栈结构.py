#  定义栈结构
# 列表尾部作为栈顶
class Stack:
	"""docstring for Stack"""
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

#----------------------------------------------------------------------
#栈应用实例-简单括号匹配
def parChecker(symbolString):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol == "(":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()

		index += 1

	if balanced and s.isEmpty():
		return True
	else:
		return False

#栈应用实例-通用符号匹配
def parChecker(symbolString):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol in "{[(":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top, symbol):
					balanced = False
		index += 1
	if balanced and s.isEmpty():
		return True
	else:
		return False

def matches(open, close):
	opens = "([{"
	closers = ")]}"
	return opens.index(open) == closers.index(close)

#-------------------------------------------------------------------------
# 进制转换 十进制-二进制
def divideBy2(decNumber):
	remstack = Stack()

	while decNumber > 0:
		rem = decNumber % 2
		remstack.push(rem)
		decNumber = decNumber // 2

	binString = ""
	while not remstack.isEmpty():
		binString = binString + str(remstack.pop())

	return binString

# 通用进制转换方法
def baseConverter(decNumber, base):
	digit = "0123456789ABCDEF"

	remstack = Stack()
	while decNumber > 0:
		rem = decNumber % base
		decNumber = decNumber // base
		remstack.push(rem)

	baseString = ""
	while not remstack.isEmpty():
		baseString = baseString + digit[remstack.pop()]

	return baseString

#-----------------------------------------------------------------------
# 中缀表达式转换为后缀表达式
def infixToPostfix(infixexpr):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["-"] = 2
	prec["+"] = 2
	prec["("] = 1
	opStack = Stack()
	postfixList = []
	tokenList = infixexpr.split()

	for token in tokenList:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postfixList.append(token)
		elif token == "(":
			opStack.push(token)
		elif token == ")":
			topToken = opStack.pop()
			while topToken != "(":
				postfixList.append(topToken)
				topToken = opStack.pop()
		else:
			while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
				postfixList.append(opStack.pop())
			opStack.push(token)

	while not opStack.isEmpty():
		postfixList.append(opStack.pop())

	return " ".join(postfixList)

# 计算后缀表达式的值
def postfitEval(postfixExpr):
	operandStack = Stack()
	tokenList = postfixExpr.split()

	for token in tokenList:
		if token in "0123456789":
			operandStack.push(int(token))
		else:
			operand2 = operandStack.pop()
			operand1 = operandStack.pop()
			result = doMath(token, operand1, operand2)
			operandStack.push(result)
	return operandStack.pop()

def doMath(op, op1, op2):
	if op == "*":
		return op1 * op2
	elif op == "/":
		return op1 / op2
	elif op == "+":
		return op1 + op2
	else:
		return op1 - op2