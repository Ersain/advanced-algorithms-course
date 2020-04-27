from __future__ import annotations

from typing import List


class LevenshteinAutomata:
    def __init__(self, s: str, n: int = 0):
        self.term = s
        self.max_errors = n

    def __initial_state(self):
        """
        Get the initial state of an automata
        """
        return list(range(len(self.term) + 1))

    def __change_state(self, state: List, c: str):
        """
        Generate the next state of an automata with the given state and character
        """
        res = [state[0] + 1]
        for i in range(len(state) - 1):
            cost = 1
            if self.term[i] == c:
                cost = 0
            res.append(
                min(res[i] + 1, state[i] + cost, state[i + 1] + 1)
            )
        return [min(x, self.max_errors + 1) for x in res]

    def __can_match(self, state: List):
        """
        Return True if the given state is a match of the initial term's state
        """
        return min(state) <= self.max_errors

    def is_similar(self, s: str, max_errors: int = 0):
        """
        Check whether a given string is a match to the initial term
        """
        if not s:
            return False
        if len(s) < len(self.term) // 2:
            return False
        self.max_errors = max_errors
        state = self.__initial_state()
        for i in range(len(s)):
            state = self.__change_state(state, s[i])
        return self.__can_match(state)
