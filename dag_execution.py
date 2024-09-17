from models import DAG


class DAGRunner:
    def __init__(self, dag: DAG):
        self.dag = dag
        self.adj_list = {task.id: task.dependencies for task in dag.tasks}
        self.visited = set()
        self.execution_order = []

    def topological_sort(self):
        def dfs(task_id):
            self.visited.add(task_id)
            for dep in self.adj_list.get(task_id, []):
                if dep not in self.visited:
                    dfs(dep)
            self.execution_order.append(task_id)

        for task in self.dag.tasks:
            if task.id not in self.visited:
                dfs(task.id)

        self.execution_order.reverse()
        return self.execution_order

    def execute_tasks(self):
        order = self.topological_sort()
        print(f"Execution order: {order}")
        for task_id in order:
            task = next(t for t in self.dag.tasks if t.id == task_id)
            print(f"Executing {task.name}: {task.command}")
