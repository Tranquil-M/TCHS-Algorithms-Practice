# Pseudocode Example

This is an example of pseudocode.
If you use pseudocode for your solution, it must be written on paper.
Your dialect of pseudocode does not need to be the same as the one that I use.
Your dialect should have about as high level as Python or Lua. 
- For example, you shouldn't have a function that's called "navigate the grid" unless you declare it with lower level functions.
- However, using things like collection comprehension is ok, such as max(), which iterates through a list and returns the greatest value within.


This example calculates the distance to the nearest apple using Manhattan Distance.
Remember that your dialect need not be identical, just understandable. Try to limit ambiguity.

let grid = get_grid()

for range 0 to 5 as y:
	for range 0 to 5 as x:
		if grid[y][x] is 'o':
			let apple_pos = [ x , y ]

print abs(position_x - apple_pos.x) + abs(position_y - apple_pos.y)