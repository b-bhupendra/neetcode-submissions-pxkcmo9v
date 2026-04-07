# import random
# random_integer = random.randint(1, 10)
# print(random_integer)

class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        fx = lambda x : 2 * x
        nx = init
        while iterations :
            nx = nx - learning_rate * fx(nx)
            iterations -= 1

        return round(nx,5)
        























    