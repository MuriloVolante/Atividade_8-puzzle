from collections import deque
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class BFS(BaseSearch):

    def search(self, initial: State) -> SearchResult:
        fronteira = deque([initial])
        visitados = {initial}
        expandidos, gerados, pico = 0, 1, 1

        while fronteira:
            node = fronteira.popleft()

            if node.is_goal:
                return SearchResult(node, expandidos, gerados, pico, len(node.actions()))

            expandidos += 1
            for filho in node.neighbors():
                gerados += 1
                if filho not in visitados:
                    visitados.add(filho)
                    fronteira.append(filho)

            pico = max(pico, len(fronteira))

        return SearchResult(None, expandidos, gerados, pico)
