# agents.py
import random

class CovidAgent:
    def __init__(self, age, health, mobility, awareness, wealth, activity, infection_probability, recovery_time, mortality_rate):
        self.state = "Susceptible"  # Todos los agentes inician como susceptibles
        self.age = age
        self.health = health
        self.mobility = mobility
        self.awareness = awareness
        self.wealth = wealth
        self.activity = activity
        self.infection_probability = infection_probability
        self.recovery_time = recovery_time
        self.mortality_rate = mortality_rate
        self.infected = False

    def calculate_infection_probability(self):
        return self.infection_probability

    def calculate_recovery_time(self):
        self.recovery_time = random.randint(self.recovery_time[0], self.recovery_time[1])

    def calculate_mortality_rate(self):
        self.mortality_rate = random.uniform(self.mortality_rate[0], self.mortality_rate[1])

    def get_state(self):
        return {
            "state": self.state,
            "age": self.age,
            "health": self.health,
            "mobility": self.mobility,
            "awareness": self.awareness,
            "wealth": self.wealth,
            "activity": self.activity,
            "infection_probability": self.infection_probability,
            "recovery_time": self.recovery_time,
            "mortality_rate": self.mortality_rate
        }


# class CovidAgent:
#     def __init__(self, age, activity, mobility, awareness, health, purchasing_power, infection_probability, recovery_days, mortality_rate):
#         print("Creando agente", self, age, activity, mobility, awareness, health, purchasing_power)
#         self.age = age
#         self.activity = activity
#         self.mobility = mobility
#         self.awareness = awareness
#         self.health = health
#         self.purchasing_power = purchasing_power
#         self.infection_probability = infection_probability
#         self.recovery_days = recovery_days
#         self.mortality_rate = mortality_rate
#         self.recovery_time = None
#         self.state = "Susceptible"
#         self.infected = False

#     def calculate_infection_probability(self):
#         # Fórmula para calcular la probabilidad de infección con ajuste de movilidad y actividad
#         self.probability_of_infection = min(self.infection_probability, (self.mobility * self.activity) / (self.awareness + 1))
#         return self.probability_of_infection

#     def calculate_recovery_time(self):
#         # Fórmula para calcular el tiempo de recuperación con ajuste de salud
#         self.recovery_time = max(self.recovery_days - (self.health / 10), 0)  # Asegura que no sea negativo
#         return self.recovery_time

#     def calculate_mortality_rate(self):
#         # Fórmula para calcular la tasa de mortalidad con ajuste de salud
#         self.mortality_rate = self.mortality_rate * (1 - self.health / 100)  # Ajusta el porcentaje basado en la salud
#         return self.mortality_rate

#     def get_state(self):
#         # Devuelve el estado actual del agente
#         return {
#             "age": self.age,
#             "activity": self.activity,
#             "mobility": self.mobility,
#             "awareness": self.awareness,
#             "health": self.health,
#             "purchasing_power": self.purchasing_power,
#             "state": self.state,
#             #"probability_of_infection": self.probability_of_infection,
#             #"recovery_time": self.recovery_time,
#             "mortality_rate": self.mortality_rate
#         }

# class CovidAgent:
#     def __init__(self, age, activity, mobility, awareness, health, purchasing_power):
#         print("Creando agente", self, age, activity, mobility, awareness, health, purchasing_power)
#         self.age = age
#         self.activity = activity
#         self.mobility = mobility
#         self.awareness = awareness
#         self.health = health
#         self.purchasing_power = purchasing_power
#         self.infected = False
#         self.recovery_time = None
#         self.mortality_rate = None
#         self.probability_of_infection = None
#         self.state = "Susceptible"
    
#     def calculate_infection_probability(self):
#         # Fórmula para calcular la probabilidad de infección
#         self.probability_of_infection = (self.mobility * self.activity) / (self.awareness + 1)
#         return self.probability_of_infection

#     def calculate_recovery_time(self):
#         # Fórmula para calcular el tiempo de recuperación
#         self.recovery_time = 14 - (self.health / 10)  # Ejemplo: 14 días menos un factor de salud
#         return self.recovery_time

#     def calculate_mortality_rate(self):
#         # Fórmula para calcular la tasa de mortalidad
#         self.mortality_rate = 0.02 * (1 - self.health / 100)  # Ejemplo: 2% de mortalidad ajustada por salud
#         return self.mortality_rate

#     # def calculate_infection_probability(self):
#     #     # Fórmula proporcionada
#     #     self.probability_of_infection = (self.age + self.activity + self.mobility + self.awareness) / 4
#     #     print("Probabilidad de infección:", self.probability_of_infection)
#     #     return self.probability_of_infection

#     # def calculate_recovery_time(self):
#     #     self.recovery_time = (self.health + self.purchasing_power + self.awareness) / 3
#     #     print("Tiempo de recuperación:", self.recovery_time)
#     #     return self.recovery_time

#     # def calculate_mortality_rate(self):
#     #     self.mortality_rate = (self.health + self.purchasing_power) / 2
#     #     print("Tasa de mortalidad:", self.mortality_rate)
#     #     return self.mortality_rate
    
#     def get_state(self):
#         # Devuelve el estado actual del agente
#         return {
#             "age": self.age,
#             "activity": self.activity,
#             "mobility": self.mobility,
#             "awareness": self.awareness,
#             "health": self.health,
#             "purchasing_power": self.purchasing_power,
#             "state": self.state,
#             "probability_of_infection": self.probability_of_infection,
#             "recovery_time": self.recovery_time,
#             "mortality_rate": self.mortality_rate
#         }
