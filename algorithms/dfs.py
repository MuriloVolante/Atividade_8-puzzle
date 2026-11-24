from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:
        fronteira = [initial]
        melhor = {initial: 0}
        expandidos, gerados, pico = 0, 1, 1

        while fronteira:
            node = fronteira.pop()

            if node.is_goal:
                return SearchResult(node, expandidos, gerados, pico, len(node.actions()))

            if node.cost >= self.depth_limit:
                continue

            expandidos += 1
            for filho in node.neighbors():
                gerados += 1
                # volta num estado ja visto so se chegou nele por um caminho mais curto
                if filho.cost < melhor.get(filho, self.depth_limit + 1):
                    melhor[filho] = filho.cost
                    fronteira.append(filho)

            pico = max(pico, len(fronteira))

        return SearchResult(None, expandidos, gerados, pico)
