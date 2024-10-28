import random
from models.agents import CovidAgent

class CovidModel:
    def __init__(self, num_agents, config):
        self.agents = []
        self.grid = self.initialize_grid(config["grid_size"])
        self.infection_radius = config["infection_radius"]
        for _ in range(num_agents):
            print("Creando agente")
            agent = CovidAgent(
                age=random.choice(config["ages"]),
                activity=random.choice(config["activities"]),
                mobility=random.choice(config["mobilities"]),
                awareness=random.choice(config["awareness_levels"]),
                health=random.choice(config["health_statuses"]),
                purchasing_power=random.choice(config["purchasing_power"])
            )
            print("Agente creado", agent)
            self.agents.append(agent)

    def initialize_grid(self, grid_size):
        print("Inicializando cuadrícula")
        # Inicializar la cuadrícula de simulación
        return [[None for _ in range(grid_size)] for _ in range(grid_size)]

    def step(self):
        # Un ciclo de simulación
        print("Ejecutando ciclo de simulación",self.agents.count)
        for agent in self.agents:
            if agent.state == "Susceptible":
                infection_probability = agent.calculate_infection_probability()
                if random.random() < infection_probability:
                    agent.state = "Exposed"
            elif agent.state == "Exposed":
                agent.state = "Infectious"
                agent.calculate_recovery_time()
                agent.calculate_mortality_rate()
            elif agent.state == "Infectious":
                if agent.recovery_time <= 0:
                    if random.random() < agent.mortality_rate:
                        agent.state = "Deceased"
                    else:
                        agent.state = "Recovered"
                else:
                    agent.recovery_time -= 1
        # for agent in self.agents:
        #     print("Calculando probabilidad de infección de agente... ", format(agent)) 
        #     infection_probability = agent.calculate_infection_probability()
        #     recovery_time = agent.calculate_recovery_time()
        #     mortality_rate = agent.calculate_mortality_rate()
        #     if agent.state == "Susceptible" and random.random() < infection_probability:
        #         agent.state = "Exposed"
        #     elif agent.state == "Exposed":
        #         agent.state = "Infectious"
        #     elif agent.state == "Infectious" and recovery_time <= 0:
        #         if random.random() < mortality_rate:
        #             agent.state = "Deceased"
        #         else:
        #             agent.state = "Recovered"
        #     elif agent.state == "Infectious":
        #         agent.recovery_time -= 1
            # Lógica para contagiar a los agentes cercanos
    def get_results(self):
        results = []
        for agent in self.agents:
            results.append(agent.get_state())  # Suponiendo que cada agente tiene un método get_state()
        return results
