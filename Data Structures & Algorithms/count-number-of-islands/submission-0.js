class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid) {
        const seen = new Set();
        const queue = [];
        let numIsland = 0;
        const coordinate = (x, y) => `${x}, ${y}`;

        const bfs = (initY, initX) => {
            queue.push([initY, initX]);
            while (queue.length > 0) {
                const [y, x] = queue.shift();
                if (grid[y][x] == '1' && !seen.has(coordinate(x, y))) {
                    seen.add(coordinate(x, y));
                    y < grid.length - 1 && queue.push([y + 1, x]);
                    x < grid[y].length - 1 && queue.push([y, x+1]);
                    y > 0 && queue.push([y-1, x]);
                    x > 0 && queue.push([y, x-1]);
                }
            }
        }

        for (let y = 0; y < grid.length; y++) {
            for (let x = 0; x < grid[y].length; x++) {
                if (grid[y][x] == '1') {
                    const coords = coordinate(x, y);
                    // bfs on a never seen piece of land to add to the island
                    if (!seen.has(coords)) {
                        bfs(y, x);
                        numIsland++;
                    }
                }
            }
        }
        return numIsland;
    }
}
