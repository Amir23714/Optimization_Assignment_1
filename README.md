# Optimization Assignment 1

## Team Members
- Amir Gubaidullin
- Ilnaz Magizov
- Ilya Krasheninnikov
- Dima Nekrasov

# INFO
This Python script is an implementation of the Simplex method, a widely used algorithm for solving linear programming problems. It takes as input the coefficients of the objective function, the coefficients of the constraint functions, the right-hand side values of the constraints, and an approximation accuracy. It then solves the linear programming problem and provides the optimal solution and the optimal objective function value.

## Usage
To use our code, follow these steps:

1. Clone the repository to your local machine:
```bash
git clone https://github.com/Amir23714/Optimization_Assignment_1.git
```
2. Navigate to the project directory:
```bash
cd Optimization_Assignment_1
```
3. Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

### Input format
The input is expected to be provided in a specific format, as follows:

```bash
number_of_variables_in_objective_function number_of_inequalities_in_subject
vector of coefficients of the objective function
matrix of coefficients of constraint functions
vector of right-hand side numbers
approximation accuracy
```

Example:
3 2
2 -1 3
1 1 1
3 2
3

The script will output two lines:
```bash
The first line contains the optimal solution for the decision variables.
The second line contains the optimal value of the objective function.
```

### Important Notes
Ensure that the input data is provided in the specified format, with appropriate positive coefficients for the constraint functions. The method may not be applicable if these conditions are not met.
The accuracy parameter controls the number of decimal places in the output. Adjust it to your desired level of precision.

Now you're ready to use our code for solving LPP!

Example for "Method is not applicable":

2 3
1 1
-1 1
-1 0
-1 1
2 4 4
0
