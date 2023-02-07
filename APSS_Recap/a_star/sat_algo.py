from queue import PriorityQueue


def calculate_heuristic(cnf, truth_assignment):
    """Calculate the heuristic score based on the number of unsatisfied clauses."""
    score = 0
    for clause in cnf:
        clause_satisfied = False
        for literal in clause:
            variable = abs(literal)
            if literal > 0 and truth_assignment[variable - 1]:
                clause_satisfied = True
                break
            elif literal < 0 and not truth_assignment[variable - 1]:
                clause_satisfied = True
                break
        if not clause_satisfied:
            score += 1
    return score


def boolean_satisfiability(cnf, n):
    """Solve the Boolean Satisfiability Problem using A* algorithm."""
    visited = set()
    pq = PriorityQueue()
    root = ([None] * n, 0, calculate_heuristic(cnf, [None] * n))
    pq.put(root)
    while not pq.empty():
        node, cost, heuristic = pq.get()
        if None not in node:
            if calculate_heuristic(cnf, node) == 0:
                return node
            continue
        index = node.index(None)
        true_assignment = node[:]
        true_assignment[index] = True
        true_node = (true_assignment, cost + 1, calculate_heuristic(cnf, true_assignment))
        false_assignment = node[:]
        false_assignment[index] = False
        false_node = (false_assignment, cost + 1, calculate_heuristic(cnf, false_assignment))
        if str(true_assignment) not in visited:
            pq.put(true_node)
            visited.add(str(true_assignment))
        if str(false_assignment) not in visited:
            pq.put(false_node)
            visited.add(str(false_assignment))
    return None


def variables_in_cnf(cnf: list) -> int:
    vars_in_cnf = []
    for vals in cnf:
        for unique_vals in vals:
            if unique_vals < 0:
                unique_vals *= -1
            if unique_vals not in vars_in_cnf:
                vars_in_cnf.append(unique_vals)
    return len(vars_in_cnf)
