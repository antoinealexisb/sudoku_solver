# Python : sudoku_solver
This is a sudoku solver in python.
## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org).You can launch the python script with an annex file. Or directly with the script.

```sh
$ git clone https://github.com/antoinealexisb/sudoku_solver.git
$ cd sudoku_solver/

$ python3 main.py examples/file2.txt

---- Filename :  examples/file2.txt


0 0 0  | 2 9 6  | 0 0 0
6 0 0  | 3 8 1  | 0 0 2
0 0 0  | 0 0 0  | 0 0 0
- - - - - - - - - - - - -
0 0 9  | 0 0 0  | 5 0 0
0 0 0  | 0 6 0  | 0 0 0
5 7 3  | 0 0 0  | 4 6 1
- - - - - - - - - - - - -
0 0 1  | 0 0 0  | 9 0 0
8 0 2  | 0 3 0  | 6 0 4
0 4 0  | 0 1 0  | 0 3 0


4 1 7  | 2 9 6  | 8 5 3
6 9 5  | 3 8 1  | 7 4 2
3 2 8  | 7 5 4  | 1 9 6
- - - - - - - - - - - - -
1 6 9  | 4 7 3  | 5 2 8
2 8 4  | 1 6 5  | 3 7 9
5 7 3  | 8 2 9  | 4 6 1
- - - - - - - - - - - - -
7 3 1  | 6 4 2  | 9 8 5
8 5 2  | 9 3 7  | 6 1 4
9 4 6  | 5 1 8  | 2 3 7


$ python3 main.py
give your sudoku board : 780400120600075009000601078007040260001050930904060005070300012120007400049206007

7 8 0  | 4 0 0  | 1 2 0
6 0 0  | 0 7 5  | 0 0 9
0 0 0  | 6 0 1  | 0 7 8
- - - - - - - - - - - - -
0 0 7  | 0 4 0  | 2 6 0
0 0 1  | 0 5 0  | 9 3 0
9 0 4  | 0 6 0  | 0 0 5
- - - - - - - - - - - - -
0 7 0  | 3 0 0  | 0 1 2
1 2 0  | 0 0 7  | 4 0 0
0 4 9  | 2 0 6  | 0 0 7


7 8 5  | 4 3 9  | 1 2 6
6 1 2  | 8 7 5  | 3 4 9
4 9 3  | 6 2 1  | 5 7 8
- - - - - - - - - - - - -
8 5 7  | 9 4 3  | 2 6 1
2 6 1  | 7 5 8  | 9 3 4
9 3 4  | 1 6 2  | 7 8 5
- - - - - - - - - - - - -
5 7 8  | 3 9 4  | 6 1 2
1 2 6  | 5 8 7  | 4 9 3
3 4 9  | 2 1 6  | 8 5 7

```

## Documentation
### files:
example : `files2.txt`
```
7 8 0 4 0 0 1 2 0
6 0 0 0 7 5 0 0 9
0 0 0 6 0 1 0 7 8
0 0 7 0 4 0 2 6 0
0 0 1 0 5 0 9 3 0
9 0 4 0 6 0 0 0 5
0 7 0 3 0 0 0 1 2
1 2 0 0 0 7 4 0 0
0 4 9 2 0 6 0 0 7
```
....
