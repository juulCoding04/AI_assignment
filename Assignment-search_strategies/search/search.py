# # search.py
# # ---------
# # Licensing Information:  You are free to use or extend these projects for
# # educational purposes provided that (1) you do not distribute or publish
# # solutions, (2) you retain this notice, and (3) you provide clear
# # attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# # 
# # Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# # The core projects and autograders were primarily created by John DeNero
# # (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# # Student side autograding was added by Brad Miller, Nick Hay, and
# # Pieter Abbeel (pabbeel@cs.berkeley.edu).


# """
# In search.py, you will implement generic search algorithms which are called by
# Pacman agents (in searchAgents.py).
# """

# import util
# from game import Directions
# from typing import List

# class SearchProblem:
#     """
#     This class outlines the structure of a search problem, but doesn't implement
#     any of the methods (in object-oriented terminology: an abstract class).

#     You do not need to change anything in this class, ever.
#     """

#     def getStartState(self):
#         """
#         Returns the start state for the search problem.
#         """
#         util.raiseNotDefined()

#     def isGoalState(self, state):
#         """
#           state: Search state

#         Returns True if and only if the state is a valid goal state.
#         """
#         util.raiseNotDefined()

#     def getSuccessors(self, state):
#         """
#           state: Search state

#         For a given state, this should return a list of triples, (successor,
#         action, stepCost), where 'successor' is a successor to the current
#         state, 'action' is the action required to get there, and 'stepCost' is
#         the incremental cost of expanding to that successor.
#         """
#         util.raiseNotDefined()

#     def getCostOfActions(self, actions):
#         """
#          actions: A list of actions to take

#         This method returns the total cost of a particular sequence of actions.
#         The sequence must be composed of legal moves.
#         """
#         util.raiseNotDefined()




# def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
#     """
#     Returns a sequence of moves that solves tinyMaze.  For any other maze, the
#     sequence of moves will be incorrect, so only use this for tinyMaze.
#     """
#     s = Directions.SOUTH
#     w = Directions.WEST
#     return  [s, s, w, s, w, w, s, w]

# def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
#     """
#     Search the deepest nodes in the search tree first.

#     Your search algorithm needs to return a list of actions that reaches the
#     goal. Make sure to implement a graph search algorithm.

#     To get started, you might want to try some of these simple commands to
#     understand the search problem that is being passed in:

#     print("Start:", problem.getStartState())
#     print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
#     print("Start's successors:", problem.getSuccessors(problem.getStartState()))
#     """
#     "*** YOUR CODE HERE ***"
#     frontier = util.Stack()
#     visited = []
    
#     frontier.push((problem.getStartState(), []))

#     while not frontier.isEmpty():
#         current_state, actions = frontier.pop()

#         if problem.isGoalState(current_state):
#             return actions;

#         if current_state not in visited:
#             visited.append(current_state)
#             for succ, action, cost in problem.getSuccessors(current_state):
#                 if succ not in visited:
#                     frontier.push((succ, actions + [action]))

#     return []

# def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
#     """Search the shallowest nodes in the search tree first."""
#     "*** YOUR CODE HERE ***"
#     frontier = util.Queue()
#     visited = []
    
#     frontier.push((problem.getStartState(), []))

#     while not frontier.isEmpty():
#         current_state, actions = frontier.pop()

#         if problem.isGoalState(current_state):
#             return actions;

#         if current_state not in visited:
#             visited.append(current_state)
#             for succ, action, cost in problem.getSuccessors(current_state):
#                 if succ not in visited:
#                     frontier.push((succ, actions + [action]))

#     return []

# def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
#     """Search the node of least total cost first."""
#     "*** YOUR CODE HERE ***"
#     frontier = util.PriorityQueue()
#     frontier.push((problem.getStartState(), [], 0), 0)
#     visited = {}

#     while not frontier.isEmpty():
#         current_state, actions, current_cost = frontier.pop()

#         if problem.isGoalState(current_state):
#             return actions
        
#         if current_state not in visited or current_cost < visited[current_state]:
#             visited[current_state] = current_cost

#             for succ, action, cost in problem.getSuccessors(current_state):
#                 new_cost = current_cost + cost
#                 if succ not in visited or new_cost < visited[succ]:
#                     frontier.push((succ, actions + [action], new_cost), new_cost)
                    
#     return []

# def nullHeuristic(state, problem=None) -> float:
#     """
#     A heuristic function estimates the cost from the current state to the nearest
#     goal in the provided SearchProblem.  This heuristic is trivial.
#     """
#     return 0

# def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
#     """Search the node that has the lowest combined cost and heuristic first."""
#     "*** YOUR CODE HERE ***"
#     frontier = util.PriorityQueue()
#     start_state = problem.getStartState()
#     frontier.push((start_state, [], 0), 0)

#     visited = {}

#     while not frontier.isEmpty():
#         current_state, actions, current_cost = frontier.pop()

#         if problem.isGoalState(current_state):
#             return actions
        
#         if current_state not in visited or current_cost < visited[current_state]:
#             visited[current_state] = current_cost

#             for succ, action, cost in problem.getSuccessors(current_state):
#                 new_cost = current_cost + cost
#                 f_value = new_cost + heuristic(succ, problem)

#                 if succ not in visited or new_cost < visited[succ]:
#                     frontier.push((succ, actions + [action], new_cost), f_value)

#     return []

# # Abbreviations
# bfs = breadthFirstSearch
# dfs = depthFirstSearch
# astar = aStarSearch
# ucs = uniformCostSearch

# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from __future__ import annotations

from dataclasses import dataclass

import util
from util import PriorityQueue, Counter
from game import Directions
from typing import List, Any, Optional, Protocol

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

@dataclass 
class Node:
    """A Node in the search-space graph."""
    state: Any
    parent: Optional[Node] = None
    action: Optional[Directions] = None
    cost : float = 0.0
    def get_path(self) -> List[Directions]:
        backward_path = []
        node = self
        while node.parent is not None:
            backward_path.append(node.action)
            node = node.parent
        forward_path = list(reversed(backward_path))
        return forward_path

class FringeWithSimplePush(Protocol): 
    """Interface for fringe data structure that support simple push operations."""
    def isEmpty(self) -> bool:
        return 0
    def pop(self):# -> Node:
        """Extract node according to strategy."""
        return
    def push(self, node: Node) -> None:
        """Insert node into fringe."""
        return


def expand_node(node: Node, problem: SearchProblem):
    """Implementation of Expand algorithm from the """
    successors_list: list[Node] = []
    successor_data = problem.getSuccessors(node.state)
    successor_data: list[tuple[Any, Directions, float]]
    for successor_state, action, step_cost in successor_data:
        successor_cost = node.cost + step_cost
        successors_list.append(Node(successor_state, node, action, successor_cost))
    return successors_list

def graph_search(problem: SearchProblem, fringe: FringeWithSimplePush) -> Node:
    start_state = problem.getStartState()
    fringe.push(Node(start_state))

    closed = set()

    while not fringe.isEmpty():
        node = fringe.pop()
        if problem.isGoalState(node.state):
            return node
        
        if node.state not in closed:
            closed.add(node.state)
            successor_nodes = expand_node(node, problem)
            for successor_node in successor_nodes:
                fringe.push(successor_node)

def solve_search(problem: SearchProblem, fringe: FringeWithSimplePush) -> Node:
    goal = graph_search(problem, fringe)
    return goal.get_path()


def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    fringe = util.Stack()
    return solve_search(problem, fringe)

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    fringe = util.Queue()
    return solve_search(problem, fringe)

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    fringe = util.PriorityQueueWithFunction(lambda node: node.cost)
    return solve_search(problem, fringe)

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    Fringe = util.PriorityQueueWithFunction(lambda node: node.cost + heuristic(node.state, problem))
    return solve_search(problem, Fringe)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
