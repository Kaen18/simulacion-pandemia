# models.py
import random
from models.agents import CovidAgent

class CovidModel:
    def __init__(self, config):
        self.agents = []
        self.grid = self.initialize_grid(10)  # Tamaño de la cuadrícula fijo, modificar si es necesario
        self.config = config
        self.infection_radius = 2  # Radio de infección fijo
        self.history = []  # Para almacenar el historial de los estados de los agentes en cada paso

        # Inicialización de agentes con distribuciones de características
        for i in range(config["agents"]):
            # Asegúrate de que cada atributo se genera antes de pasar al agente
            age = self.choose_attribute(config["distribution"]["poblationalAge"])
            health = self.choose_attribute(config["distribution"]["healthCondition"])
            mobility = self.choose_attribute(config["distribution"]["movility"])
            awareness = self.choose_attribute(config["distribution"]["atention"])
            wealth = self.choose_attribute(config["distribution"]["wealthyDistribution"])
            activity = self.choose_attribute(config["distribution"]["profesionalActivity"])
            infection_probability = random.uniform(config["contagiousPercentage"]["minimum"], config["contagiousPercentage"]["maximum"])
            recovery_time = (config["recoveryTime"]["minimum"], config["recoveryTime"]["maximum"])
            mortality_rate = random.uniform(config["deathPercentage"]["minimum"], config["deathPercentage"]["maximum"])

            print("Creando agente", age, health, mobility, awareness, wealth, activity, infection_probability, recovery_time, mortality_rate)

            # Pasamos las variables correctamente al agente
            agent = CovidAgent(
                age=age,
                health=health,
                mobility=mobility,
                awareness=awareness,
                wealth=wealth,
                activity=activity,
                infection_probability=infection_probability,
                recovery_time=recovery_time,
                mortality_rate=[0.01, 0.100]
            )
            
            # Configuración inicial de agentes infectados
            if i < config["infected"]:
                agent.state = "Infectious"
                agent.infected = True
                agent.calculate_recovery_time()
                agent.calculate_mortality_rate()
            
            self.agents.append(agent)

    # Definir el método count_agent_states para contar los estados de los agentes
    def count_agent_states(self):
        # Inicializamos un diccionario para contar los estados
        state_counts = {
            "Susceptible": 0,
            "Exposed": 0,
            "Infectious": 0,
            "Recovered": 0,
            "Deceased": 0
        }
        
        # Recorremos todos los agentes y contamos los estados
        for agent in self.agents:
            if agent.state in state_counts:
                state_counts[agent.state] += 1
        
        return state_counts

    def initialize_grid(self, grid_size):
        return [[None for _ in range(grid_size)] for _ in range(grid_size)]

    def choose_attribute(self, distribution):
        """
        Selecciona un valor basado en la distribución de probabilidades especificada.
        """
        rand_val = random.uniform(0, 1)
        cumulative_probability = 0.0
        for attribute, probability in distribution.items():
            cumulative_probability += probability
            if rand_val <= cumulative_probability:
                return attribute
        return list(distribution.keys())[-1]  # Devuelve el último atributo en caso de error de redondeo

    def step(self):
        current_step = []
        for agent in self.agents:
            if agent.state == "Susceptible":
                infection_probability = agent.calculate_infection_probability()
                if random.uniform(0, 1) < infection_probability:
                    agent.state = "Exposed"
            elif agent.state == "Exposed":
                agent.state = "Infectious"
                agent.calculate_recovery_time()
                agent.calculate_mortality_rate()
            elif agent.state == "Infectious":
                if agent.recovery_time <= 0:
                    if random.uniform(0, 1) < agent.mortality_rate:
                        agent.state = "Deceased"
                    else:
                        agent.state = "Recovered"
                else:
                    agent.recovery_time -= 1

            # Guardar el estado actual del agente
            current_step.append(agent.get_state())
        
        self.history.append(current_step)

    def get_results(self):
        return self.history
