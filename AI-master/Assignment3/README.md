CS4341 Assignment 3
Everett Harding
Kenedi Heather 
Dean Schifilliti
Dan Seaman

This submission includes:
	- sample.py, our main program
	- probabilities.py, a helper file
	- 4 text files continaing outputs from our four test queries
	- an analysis excel sheet
	- this readme file

To run our program*, provide a node to observe, a number of samples, and any number of pre-observed nodes from 0 to all 6 others.
The program is not case sensitive, but there is no error checking for improperly assigned node values - BE CAREFUL. 
For example:
$$ python3 sample.py temperature=warm 1000 cloudy=true stress=high

Our programs output will be well-labeled and in this order:
	- Samples completed
	- Accepted samples (based on pre-observed nodes)
	- Valid results (the number of expected examples that match the desired node being observed)
	- P(node) (the probability of the conditional query)
	- Mean (the mean value of the non-rejected probabilities)
	- Standard Deviation (the standard deviation of the non-rejected probabilities)
	- 95% Confidence Interval (the 95% confidence interval value and corresponding boundaries for the query)

Our 4 test queries are as follows: 
	1.) cloudy=false X
	2.) stress=high X temperature=cold day=weekday
	3.) stress=high X temperature=cold day=weekday cloudy=true exams=true
	4.) cloudy=false X humidity=medium temperature=cold day=weekend exams=false snow=true stress=low
The analysis excel sheet contains output values for them all, as well as graphs of the probabilities vs. sample sizes. 
It also contains a table and graph of the approximate sample sizes needed to hit the specified confidence intervals: 0.2, 0.1, 0.05, and 0.01.
The output.txt files contian the outputs the excel sheet were made with, in full verbosity.  

*The program requires python3 and the numpy and scipy libraries to be installed. 