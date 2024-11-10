import random

class CovidAgent:
    def __init__(self, agent_id, config, grid_size=(10, 10)):
        self.agent_id = agent_id
        self.state = "Susceptible"  # Estado inicial es Susceptible
        self.infected = False
        self.recovery_time = random.randint(config["recoveryTime"]["minimum"], config["recoveryTime"]["maximum"])
        self.inmunity_time = random.randint(config["inmunityTime"]["minimum"], config["inmunityTime"]["maximum"])
        self.mortality_rate = random.uniform(config["deathPercentage"]["minimum"], config["deathPercentage"]["maximum"])
        self.quarantine_rate = config["ambientalParameters"]["quarentine"]
        self.mask_use = config["ambientalParameters"]["maskUse"]
        self.social_distance = config["ambientalParameters"]["socialDistance"]
        self.config = config
        
        # Distribución de características
        self.age_group = self.random_age_group(config["distribution"]["poblationalAge"])
        self.health_condition = self.random_health_condition(config["distribution"]["healthCondition"])
        self.mobility = self.random_mobility(config["distribution"]["movility"])
        self.attention = self.random_attention(config["distribution"]["atention"])
        self.wealth = self.random_wealth(config["distribution"]["wealthyDistribution"])
        self.profession = self.random_profession(config["distribution"]["profesionalActivity"])

        # Inicialización de las coordenadas del agente en la cuadrícula
        self.x, self.y = random.randint(0, grid_size[0] - 1), random.randint(0, grid_size[1] - 1)
        self.grid_size = grid_size
        
        # Inmunidad (en ciclos)
        self.immunity_duration = 0  # Duración de la inmunidad (en ciclos)
        self.immunity_expired = False  # Indicador si la inmunidad ha expirado

    def random_age_group(self, age_distribution):
        return random.choices(list(age_distribution.keys()), list(age_distribution.values()))[0]

    def random_health_condition(self, health_condition_distribution):
        return random.choices(list(health_condition_distribution.keys()), list(health_condition_distribution.values()))[0]

    def random_mobility(self, mobility_distribution):
        return random.choices(list(mobility_distribution.keys()), list(mobility_distribution.values()))[0]

    def random_attention(self, attention_distribution):
        return random.choices(list(attention_distribution.keys()), list(attention_distribution.values()))[0]

    def random_wealth(self, wealth_distribution):
        return random.choices(list(wealth_distribution.keys()), list(wealth_distribution.values()))[0]

    def random_profession(self, profession_distribution):
        return random.choices(list(profession_distribution.keys()), list(profession_distribution.values()))[0]

    def move(self):
        """Lógica de movimiento teniendo en cuenta la cuarentena, movilidad y el espacio en la cuadrícula."""
        if self.quarantine_rate or self.immunity_expired:
            return  # No se mueve si está en cuarentena o si la inmunidad ha expirado
        
        move_probability = self.calculate_move_probability()
        
        # Movimiento solo si la probabilidad lo permite
        if random.random() < move_probability:
            # Moverse dentro de la cuadrícula de tamaño definido
            self.x, self.y = self.random_move()

    def calculate_move_probability(self):
        """Calcula la probabilidad de movimiento basada en la movilidad y factores ambientales."""
        # Si tiene movilidad constante, siempre se mueve
        if self.mobility == "constant":
            return 1.0  # Siempre se mueve
        
        # Si tiene movilidad intermitente, la probabilidad es menor
        elif self.mobility == "intermitent":
            return 0.5  # 50% de probabilidad de moverse en cada iteración
        
        # Si tiene movilidad restringida, la probabilidad de moverse es baja
        elif self.mobility == "restricted":
            return 0.2  # 20% de probabilidad de moverse
        
        return 0.0  # Caso por defecto, no se mueve

    def random_move(self):
        """Define el movimiento aleatorio dentro de la cuadrícula."""
        direction = random.choice(["up", "down", "left", "right"])
        
        # Movimiento en la cuadrícula asegurando que no salga de los límites
        if direction == "up" and self.y > 0:
            self.y -= 1
        elif direction == "down" and self.y < self.grid_size[1] - 1:
            self.y += 1
        elif direction == "left" and self.x > 0:
            self.x -= 1
        elif direction == "right" and self.x < self.grid_size[0] - 1:
            self.x += 1

        return self.x, self.y

    def update_state(self):
        """Actualiza el estado del agente según las condiciones actuales."""
        if self.state == "Susceptible" and random.random() < self.exposure_chance():
            self.state = "Exposed"
        elif self.state == "Exposed" and random.random() < self.infection_chance():  # Probabilidad de pasar a infectado
            self.state = "Infectious"
        elif self.state == "Infectious":
            self.recovery_time -= 1
            if self.recovery_time <= 0:
                if random.random() < self.mortality_rate:
                    self.state = "Deceased"
                else:
                    self.state = "Recovered"
                    self.immunity_duration = random.randint(self.config["inmunityTime"]["minimum"], self.config["inmunityTime"]["maximum"])  # Duración de la inmunidad (en ciclos)
                    self.immunity_expired = False  # Asume que la inmunidad no ha expirado

        elif self.state == "Recovered":
            if self.immunity_duration > 0:
                self.immunity_duration -= 1  # Decrementa la duración de la inmunidad
            else:
                self.immunity_expired = True  # La inmunidad ha expirado
                # Reinfección con probabilidad
                random_val = random.random()
                if random_val < 0.05:  # 5% de probabilidad de reinfección después de que la inmunidad caduque
                    self.state = "Infectious"
                
        elif self.state == "Deceased":
            pass  # Los agentes muertos no deben cambiar de estado

    def exposure_chance(self):
        """Calcula la probabilidad de exposición al virus basada en varios factores."""
        exposure_chance = random.uniform(self.config["contagiousPercentage"]["minimum"], self.config["contagiousPercentage"]["maximum"])

        # Ajustes según la edad, salud, movilidad, etc.
        if self.age_group in ['neonatal', 'old', 'oldest']:
            exposure_chance *= 1.2  # Los más jóvenes y mayores tienen mayor probabilidad de exposición
        if self.health_condition == 'comorbility':
            exposure_chance *= 1.5  # Aumenta la probabilidad si tiene comorbilidades
        if self.mask_use:
            exposure_chance *= 0.5  # Reduce la probabilidad si usa mascarilla
        if self.social_distance:
            exposure_chance *= 0.7  # Reduce la probabilidad si mantiene distanciamiento social
        if self.mobility == 'high':
            exposure_chance *= 1.1  # Aumenta la probabilidad si tiene alta movilidad
        
        return random.random() * exposure_chance

    def infection_chance(self):
        """Calcula la probabilidad de infección luego de la exposición."""
        infection_chance = random.uniform(self.config["contagiousPercentage"]["minimum"], self.config["contagiousPercentage"]["maximum"])

        # Ajustes basados en la interacción cercana, condición de salud y otros factores
        if self.health_condition == 'sedentary':
            infection_chance *= 0.8  # Si es sedentario, menor chance de infección
        if self.age_group in ['young', 'adult']:
            infection_chance *= 0.9  # Menor probabilidad en estos grupos
        if self.attention == 'high':
            infection_chance *= 0.8  # Menor probabilidad de infección si tiene alta atención

        return infection_chance

    def get_state(self):
        return {
            "id": self.agent_id,
            "state": self.state,
            "age_group": self.age_group,
            "health_condition": self.health_condition,
            "mobility": self.mobility,
            "attention": self.attention,
            "wealth": self.wealth,
            "profession": self.profession,
            "position": (self.x, self.y),
            "immunity_expired": self.immunity_expired,  # Información sobre si la inmunidad ha expirado
        }
