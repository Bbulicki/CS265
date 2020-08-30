#!/usr/bin/python3
#
#    calc.py - Parses infix epressions into tokens, converts to postfix form and evaluates
#
# Created By: Brandin Bulicki
# Last Modified: 5/17/18
#
# cols = 80; tabstop = 3
#
#

import sys
import collections


#Output, for each input expression, on the same line
#Postfix expression = result

#----Infix to Postfix----
def In2Post(expression) :
 	
	iExpression = expression
	pExpression = []
	operators = []
	iExpression.append(")")
	operators.append("(")

	for token in iExpression :
		if token == "(" :
			operators.append("(")
		elif token == ")" :
			for ops in reversed(operators) :
				if ops != "(" :
					pExpression.append( operators.pop() )
				else :
					operators.pop()
					break
		elif token == "+" :
			for ops in reversed(operators) :
				if ops != "(" :
					pExpression.append( operators.pop() )
				else : 
					break
			operators.append( token )
		elif token == "-" :
			for ops in reversed(operators) :
				if ops != "(" :
					pExpression.append( operators.pop() )
				else :
					break	
			operators.append ( token )
		elif token == "/" :
			for ops in reversed(operators) :
				if ops == "(" :
					break
				elif ops == '+' :
					break
				elif ops == '-' :
					break
				else :
					pExpression.append( operators.pop() )
			operators.append( token )
		elif token == "%" :
			for ops in reversed(operators) :
				if ops == "(" :
					break
				elif ops == "+" :
					break
				elif ops == "-" :
					break
				else :
					pExpression.append ( operators.pop() )
			operators.append( token )
		elif token == "*" :
			for ops in reversed(operators) :
				if ops == "(" :
					break
				elif ops == "+" :
					break
				elif ops == "-" :
					break
				else :
					pExpression.append( operators.pop() )
			operators.append( token ) 
		else :
			pExpression.append( token )	

	return pExpression

#----Evaluating Postfix Expressions----
def evalPost(expression) :
	result = []
	tokens = expression
	for token in tokens :
		if token == "+" : 
			y = int(result.pop())
			x = int(result.pop())
			result.append(x + y)
		elif token == "-" :
			y = int(result.pop())
			x = int(result.pop())
			result.append(x - y)
		elif token == "*" :
			y = int(result.pop())
			x = int(result.pop())
			result.append(x * y)
		elif token == "/" :
			y = int(result.pop())
			x = int(result.pop())
			result.append(x / y)
		elif token == "%" :
			y = int(result.pop())
			x = int(result.pop())
			result.append(x % y)
		else :  #If it is an operand
			result.append(token)      

	return result

#----Main Function----
#parse input file and hand expression to change to Postfix
def main():
	
	inExpress = ""

	if len(sys.argv) == 1 :
		for line in sys.stdin :
			inExpress = line.strip().split()
			postExpress = In2Post(inExpress)
			answer = evalPost(postExpress)
			
			line = " ".join(str(x) for x in postExpress)
			line += " = "
			line += str(answer[0])
			print ( line )
	else :
		filename = sys.argv[1]
		fname = open( filename , "r")
		for lines in fname :
			inExpress = lines.strip().split()
			
			if lines == '^""$' :
				continue
			else :
				postExpress = In2Post(inExpress)
				answer = evalPost(postExpress)	

				line = " ".join(str(x) for x in postExpress)
				line += " = "
				line += str(answer[0])	
				print (line)

main()
