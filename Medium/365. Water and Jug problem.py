class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        queue = [(0, 0)]
        explored = {(0,0)}
        while len(queue) != 0:
            a, b = queue.pop(0)
            if a + b == target:
                return True

            moves = set()

            moves.add((x, b))
            moves.add((a, y))
            moves.add((0, b))
            moves.add((a, 0))
            moves.add((0, a+b) if (a+b) < y else (a+b-y, y))
            moves.add((a+b), 0 if (a+b) < x else (x, a+b-x))

            for move in moves:
                if move not in explored:
                    explored.add(move)
                    queue.append(move)
        return False    