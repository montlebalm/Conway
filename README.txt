# Conway's Game of Life

"Life" is an evolution simulator game for zero players. The premise is simple. Start with a two-dimensional array of cells. Each cell is either "alive" -- represented by the integer "1" -- or "dead" -- represented by "0". The initial board state represents the first generation of cells.

Upon starting the game, simple rules are applied to each cell. The outcome of the rules decides whether a live cell becomes dead or a dead cell is resurrected into life. Applying these rules to complicated patterns can produce [dramatic results](http://www.youtube.com/watch?v=XcuBvj0pw-E).

# Rules

From the Wikipedia [page](http://en.wikipedia.org/wiki/Conway's_Game_of_Life):

> The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
> - Any live cell with fewer than two live neighbours dies, as if caused by under-population.
> - Any live cell with two or three live neighbours lives on to the next generation.
> - Any live cell with more than three live neighbours dies, as if by overcrowding.
> - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
> The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed—births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick (in other words, each generation is a pure function of the preceding one). The rules continue to be applied repeatedly to create further generations.