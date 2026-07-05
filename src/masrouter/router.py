import re
class MasRouter:
    def __init__(self, routing_config, model_config):
        self.routing_config = routing_config
        self.model_config = model_config["models"]
    def classify_task(self, query: str) -> str:
        q = query.lower()
        if any(x in q for x in ["code", "python", "function", "bug", "program", "algorithm"]):
            return "coding"
        if any(x in q for x in ["solve", "calculate", "equation", "math", "probability"]):
            return "math"
        if any(x in q for x in ["paper", "research", "summarize", "abstract", "methodology"]):
            return "research"
        return "general"
    def choose_collaboration(self, task_type: str) -> str:
        if task_type == "coding":
            return "Chain"
        if task_type == "math":
            return "Chain + Verification"
        if task_type == "research":
            return "Research-Analysis-Summary"
        return "Single/Light Chain"
    def allocate_roles(self, task_type: str):
        return self.routing_config["roles"].get(task_type, self.routing_config["roles"]["general"])
    def route_llms(self, task_type: str, roles):
        selected = []
        for role in roles:
            r = role.lower()
            if "programmer" in r or "tester" in r:
                selected.append(self.model_config["coding"])
            elif "math" in r or "calculator" in r:
                selected.append(self.model_config["strong_general"])
            elif "verifier" in r:
                selected.append(self.model_config["verifier"])
            elif "summarizer" in r:
                selected.append(self.model_config["cheap_general"])
            else:
                selected.append(self.model_config["cheap_general"])
        return selected
    def route(self, query: str):
        task_type = self.classify_task(query)
        collaboration = self.choose_collaboration(task_type)
        roles = self.allocate_roles(task_type)
        llms = self.route_llms(task_type, roles)
        return {
            "query": query,
            "task_type": task_type,
            "collaboration_mode": collaboration,
            "agents": [
                {"role": role, "llm": llm}
                for role, llm in zip(roles, llms)
            ]
        }
