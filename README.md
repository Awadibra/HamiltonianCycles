
#Introduction:

As we learned in Automata and Formal Languages course, we know that the Hamiltonian cycle problem is NP-Hard, meaning it is easy to determine whether a given solution is correct (it is in fact a Hamiltonian cycle), however it is computationally hard to find such a solution.

#The thought process:

Logically two solutions come to mind, first: the naïve solution, being brute force, which is finding all combinations of the vertices in the given graph then checking whether each two adjacent vertices are in fact connected in the given graph (an edge exists between them), however this is extremely inefficient, and the second solution being: backtracking, which is the approach I took in my program.

#The algorithm:

The backtracking algorithm is rather simple and self-explanatory:
Starting with any given vertex ( I chose vertex 1), traverse the edges until finding a complete Hamiltonian cycle, or a dead end and backtrack. In my program the comments as well as the readability of the code make it very clear and simple to understand.

#How to run:

There are 2 python files and 2 folders:
Bonus1.py, Bonus1tester.py, Rand, Results.
Here is a brief explanation about each file/folder:
Bonus1.py:
This is the program itself, which is run through the terminal using the command:
“python bonus1.py <path-to-instance>”.
Where <path-to-instance> is the relative or absolute path to a given instance.
Bonus1.py can receive more than one instance, for example you can run:
“python bonus1.py <path-to-instance1> <path-to-instance2> <path-to-instance3>”.
And the outputs for each instance will be located inside the results folder.
Bonus1tester.py:
This is a program I wrote to batch test the rand tests, it runs each instance separately and then compares the output with the given solution in the instance, if both are the same Hamiltonian cycle it will print “PASSED!”, otherwise it
will print the Hamiltonian cycle that the bonus1.py program found.
If there is a filename that contains spaces in the working directory, it will prevent this
program from running and result in an error.
Rand:
This is a folder containing all the tests you provided, uncompressed.
Results:
This is the folder that my program will output <instance>.hamsol to.
