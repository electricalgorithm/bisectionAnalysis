# This code is downloaded from github.com/electricalgorithm/bisectionAnalysis
# Under the MPL-2.0, See LICENSE file.

import sys, getopt, math;

# To calculate f(x), for any giving x.
def fCalc(f, x):
	funcListType = list(f);
	for index, char in enumerate(funcListType):
		 if (char == "x"):
			 funcListType[index] = str(x);
	f = "".join(funcListType);
	return eval(f);

# --help Text
helpText = """
#### bisectionAnalysis.py ################################################
################ A script to find root of a function via given error rate.

|	# USAGE
|	bisectionAnalysis.py -f <function> -l <lower number of range> -h <higher number of range> -e <error rate>
|
|	-f : To initalize the function. Only one paramter (x) accepted.
|	The function you provide must be formated as Python scripts.
|	For example, if you want to write a function like this:
|		ex1. 15(x)^3 + (14x)^2 + |-5| + 10x^(-1)
|	You need to write it as like this:
|		15(x**3) + (14x)**2 + abs(-5) + 10(x**(-1))
|	You can't use any other unknown except (lower case) "x".
|	NOTE: Math libary is included. You can use it.
|	For more information: https://docs.python.org/3/library/math.html
|
|	-l : To initalize range's lower number.
|	-h : To initalize range's higher number.
|	To search root in [a, b] and b > a, you need to write as like: "-l a -h b"
|	Numbers a and b are also included in the range/gap.
|	NOTE: Program gives error when you tried to give -l a -h -a because
|	(a + -a)/2 is zero. You should careful about it.
|
|	-e : To initalize error number as relative approach error.
|	Relative approach error is a error type and can be formuleted:
|	a: last found root, b: earlier found root -->   (a-b)/a
|
|	# License
|	This program/script made by Gökhan Koçmarlı (electricalgorithm in GitHub).
|	The program is licensed under the Mozilla Public License 2.0 (MPL-2.0).
|	To see license's details use --license command.
|
|	Program has written in Python 3 language.
|
"""

# --license Text
licenseText = """
Notice: This panel is for summary information only.

	Permisions	------	Conditions	------	Limitations
	*Commercial use		*Disclose source	*Liability
	*Distribution		*License and		*Trademark use
	*Modification		copyright notice	*Warranty
	*Patent use		*Same license
	*Private use

FOR MORE INFORMATION AND FULL LICENSE TEXT:
https://choosealicense.com/licenses/mpl-2.0/
https://spdx.org/licenses/MPL-2.0.html
"""

# Empty variable decleration
func = "";
funcToPrint = "";
lowNumber = 0.0;
highNumber = 0.0;
errorRate = 0.0;

# To check if arguments have passed correctly.
# WARNING: Long flag doesn't work (except help).
try:
	opts, args = getopt.getopt(sys.argv[1:], "f:l:h:e:", ["func=", "lowNum=", "highNum=", "errorRate=", "help", "license"]);
except getopt.GetoptError as err:
	print("Error:", err);
	print("Use --help for more help");
	sys.exit(2);

# Arguments assigned to variables.
for opt, arg in opts:
	if (opt == "--help"):
		print(helpText);
		sys.exit();
	elif (opt == "--license"):
		print(licenseText);
		sys.exit();
	elif (opt in ("-f", "--func")):
		func = arg;
		funcToPrint = arg;
	elif (opt in ("-l", "--lowNum")):
		lowNumber = float(arg);
	elif (opt in ("-h", "--highNum")):
		highNumber = float(arg);
	elif (opt in ("-e", "--errorRate")):
		errorRate = float(arg);

# This section is all about bisection method
oldGuess = 0.0;
newGuess = 0.0;
numberOfGuess = 0;
if (fCalc(func, lowNumber) * fCalc(func, highNumber) >= 0):
	print("The gap you provided doesn't include root. Try any other highNum and lowNum.");
	sys.exit(1);
else:
	# First initalizatiın
	newGuess = (highNumber + lowNumber) / 2;
	if (fCalc(func, lowNumber) * fCalc(func, newGuess) < 0):
		highNumber = newGuess;
		numberOfGuess += 1;
	elif (fCalc(func, lowNumber) * fCalc(func, newGuess) > 0):
		lowNumber = newGuess;
		numberOfGuess += 1;
	else:
		print("Root is: ", newGuess);

	# To prevent /newGuess = /0 problem
	while (float(abs((newGuess - oldGuess) / newGuess)) > errorRate):
		oldGuess = newGuess;
		newGuess = (highNumber + lowNumber) / 2;
		if (fCalc(func, lowNumber) * fCalc(func, newGuess) < 0):
			highNumber = newGuess;
			numberOfGuess += 1;
		elif (fCalc(func, lowNumber) * fCalc(func, newGuess) > 0):
			lowNumber = newGuess;
			numberOfGuess += 1;
		else:
			print("Root is: ", newGuess);
			sys.exit(0);

# This section prints the data program found.
errorRateProv = float(abs((newGuess - oldGuess) / newGuess));
printedText = f"""
{'-'*40}
# Given function: {funcToPrint}
# Excepted error rate: {errorRate}
~> Number of gueses: {numberOfGuess}
~> Error rate provided: {errorRateProv}
~> Root: {newGuess}
{'-'*40}
""";

print(printedText);
