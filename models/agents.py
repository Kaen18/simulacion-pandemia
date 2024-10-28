class CovidAgent:
    def __init__(self, age, activity, mobility, awareness, health, purchasing_power):
        print("Creando agente", self, age, activity, mobility, awareness, health, purchasing_power)
        self.age = age
        self.activity = activity
        self.mobility = mobility
        self.awareness = awareness
        self.health = health
        self.purchasing_power = purchasing_power
        self.infected = False
        self.recovery_time = None
        self.mortality_rate = None
        self.probability_of_infection = None
        self.state = "Susceptible"
    
    def calculate_infection_probability(self):
        # Fórmula para calcular la probabilidad de infección
        self.probability_of_infection = (self.mobility * self.activity) / (self.awareness + 1)
        return self.probability_of_infection

    def calculate_recovery_time(self):
        # Fórmula para calcular el tiempo de recuperación
        self.recovery_time = 14 - (self.health / 10)  # Ejemplo: 14 días menos un factor de salud
        return self.recovery_time

    def calculate_mortality_rate(self):
        # Fórmula para calcular la tasa de mortalidad
        self.mortality_rate = 0.02 * (1 - self.health / 100)  # Ejemplo: 2% de mortalidad ajustada por salud
        return self.mortality_rate

    # def calculate_infection_probability(self):
    #     # Fórmula proporcionada
    #     self.probability_of_infection = (self.age + self.activity + self.mobility + self.awareness) / 4
    #     print("Probabilidad de infección:", self.probability_of_infection)
    #     return self.probability_of_infection

    # def calculate_recovery_time(self):
    #     self.recovery_time = (self.health + self.purchasing_power + self.awareness) / 3
    #     print("Tiempo de recuperación:", self.recovery_time)
    #     return self.recovery_time

    # def calculate_mortality_rate(self):
    #     self.mortality_rate = (self.health + self.purchasing_power) / 2
    #     print("Tasa de mortalidad:", self.mortality_rate)
    #     return self.mortality_rate
    
    def get_state(self):
        # Devuelve el estado actual del agente
        return {
            "age": self.age,
            "activity": self.activity,
            "mobility": self.mobility,
            "awareness": self.awareness,
            "health": self.health,
            "purchasing_power": self.purchasing_power,
            "state": self.state,
            "probability_of_infection": self.probability_of_infection,
            "recovery_time": self.recovery_time,
            "mortality_rate": self.mortality_rate
        }
