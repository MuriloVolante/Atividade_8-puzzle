import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import State, GOAL_STATE
from puzzle.result import SearchResult


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        total = 0
        for i, peca in enumerate(state.tiles):
            if peca != 0:
                destino = GOAL_STATE.index(peca)
                total += abs(i // 3 - destino // 3) + abs(i % 3 - destino % 3)
        return total

    def search(self, initial: State) -> SearchResult:
        fronteira = [(self.heuristic(initial), initial)]
        melhor = {initial: 0}
        expandidos, gerados, pico = 0, 1, 1

        while fronteira:
            _, node = heapq.heappop(fronteira)

            if node.is_goal:
                return SearchResult(node, expandidos, gerados, pico, len(node.actions()))

            # ja saiu da fila um caminho melhor pra esse mesmo estado
            if node.cost > melhor[node]:
                continue

            expandidos += 1
            for filho in node.neighbors():
                gerados += 1
                if filho.cost < melhor.get(filho, float("inf")):
                    melhor[filho] = filho.cost
                    heapq.heappush(fronteira, (filho.cost + self.heuristic(filho), filho))

            pico = max(pico, len(fronteira))

        return SearchResult(None, expandidos, gerados, pico)
