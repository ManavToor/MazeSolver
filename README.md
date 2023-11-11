<h1>Maze Solver</h1>

<h2>Description</h2>
Wanted to learn more about algorithms so I watched some youtube videos about maze solvers. This is a simple code that uses Breadth First Search (BFS) to solve a maze
<br />
<br />
<b>This is my maze solver:</b><br /><br />
  &emsp;&emsp;-solves maze using breadth-first-search<br /><br />
  &emsp;&emsp;-maze is in code<br /><br />

<br />
I followed a tutorial but I did make some modifications to help the code run faster and be more visually apealing:<br />
<br />
The first thing I did was make it so that the code didn't repeat over itself (it would do patterns like DownUpDownUp... or RightRightLeftLeftRightRightLeftLeft...). It was super simple, I just had to alter the if statements to also check if a spot had already been traveled upon by adding "and maze[x][y] != '+'<br />

![image](https://github.com/ManavToor/MazeSolver/assets/68403400/fc422f84-1d18-47b3-9bf2-7bd353290267)

<br />
The other thing I did was make it so at the end, the maze would be printed with only the final path instead of with every path explored and covered in plus signs. In doing so, I realized that I couldn't pass arrays by value but instead python always passed them by reference, so whenever I called the function to print the maze, it actually added the plus signs into original maze array. The fix was easy however, I just had to make a deep copy of the array that I could use to solve the maze, and then use the original to print the final path.
<h2>Languages and Utilities Used</h2>

- <b>Python</b> 

<h2>Output:</h2>
.<br />
.<br />
.<br />

![image](https://github.com/ManavToor/MazeSolver/assets/68403400/d08fed7b-5018-4b4e-904d-d9fb5b4ac6e5)



<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
