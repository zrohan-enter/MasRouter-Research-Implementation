import argparse
import yaml
import json
from dotenv import load_dotenv
from masrouter.router import MasRouter
from masrouter.runner import run_mas
def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    model_config = load_yaml("configs/models.yaml")
    routing_config = load_yaml("configs/routing.yaml")
    router = MasRouter(routing_config, model_config)
    plan = router.route(args.query)
    print("\n=== MasRouter Plan ===")
    print(json.dumps(plan, indent=2))
    if args.dry_run:
        return
    print("\n=== Running Multi-Agent System ===")
    final_answer, outputs = run_mas(args.query, plan)
    print("\n=== Agent Outputs ===")
    for item in outputs:
        print(f"\n--- {item['role']} | {item['model']} ---")
        print(item["answer"])
    print("\n=== Final Answer ===")
    print(final_answer)
if __name__ == "__main__":
    main()
