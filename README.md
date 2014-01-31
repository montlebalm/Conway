# Conway's Game of Life

"Life" is an evolution simulator game for zero players. The premise is simple. Start with a two-dimensional array of cells (the "board"). Each cell is either "alive" -- represented by the integer "1" -- or "dead" -- represented by "0". The initial board represents the first generation of cells.

At the start of each generation, rules are applied to every cell in order to determine whether it will live or die. Once every cell has been examined you can create a new board using the updated live/dead states. Applying these simple rules to certain patterns can produce [dramatic results](http://www.youtube.com/watch?v=XcuBvj0pw-E).

# Rules

From the Wikipedia [page](http://en.wikipedia.org/wiki/Conway's_Game_of_Life):

> Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
> - Any live cell with fewer than two live neighbours dies, as if caused by under-population.
> - Any live cell with two or three live neighbours lives on to the next generation.
> - Any live cell with more than three live neighbours dies, as if by overcrowding.
> - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
