import yaml
from model.model import CovidModel

def run_manual_simulation():
    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    model = CovidModel(num_agents=config["num_agents"], config=config)
    
    for i in range(config["steps"]):
        model.step()
        print(f"Step {i} completed.")
    
    print("Simulation finished.")

if __name__ == "__main__":
    run_manual_simulation()
