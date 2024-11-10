# main.py
from models.model import CovidModel

# Configuración de entrada JSON
config = {
   "agents": 100,
   "infected": 1,
   "distribution": {
      "poblationalAge": { "neonatal": 0.05, "kid": 0.2, "young": 0.15, "adult": 0.35, "old": 0.2, "oldest": 0.05 },
      "healthCondition": { "athetic": 0.2, "healthy": 0.4, "sedentary": 0.3, "comorbility": 0.1 },
      "movility": { "restricted": 0.3, "constant": 0.4, "intermitent": 0.3 },
      "atention": { "low": 0.2, "medium": 0.5, "high": 0.3 },
      "wealthyDistribution": { "halfMinimumSalary": 0.4, "minimumSalary": 0.3, "twoMinimumSalary": 0.2, "threeMinimumSalary": 0.06,
         "fiveMinimumSalary": 0.02, "tenMinimumSalary": 0.015, "moreThanTwelveMinimumSalary": 0.005 },
      "profesionalActivity": { "healthProfesional": 0.05, "essentialProfesional": 0.2, "normalProfesional": 0.2, "student": 0.3,
         "retired": 0.05, "inactive": 0.1, "domestic": 0.1 }
   },
   "ambientalParameters": {
      "quarentine": True, "maskUse": True, "socialDistance": True
   },
   "contagiousPercentage": { "minimum": 0.15, "maximum": 0.45 },
   "recoveryTime": { "minimum": 15, "maximum": 21 },
   "deathPercentage": { "minimum": 0.15, "maximum": 0.45 }
}

# Configurar la duración de la simulación (en minutos)
simulation_duration = 15  # Duración en minutos

# Inicialización y ejecución del modelo
model = CovidModel(config)

for step in range(simulation_duration * 60):  # Convertimos minutos en pasos (suponiendo un paso por segundo)
    print(f"\n--- Ciclo de simulación {step + 1} ---")
    model.step()
    
    # Contar los estados de los agentes
    state_counts = model.count_agent_states()
    print(f"Estados de los agentes: {state_counts}")
    
# Resultados finales de la simulación
print("\n--- Resultados finales de la simulación ---")
final_results = model.get_results()
for result in final_results[-1]:
    print(result)


# import yaml
# from models.model import CovidModel

# if __name__ == "__main__":
#     with open("config/config.yaml", "r") as f:
#         config = yaml.safe_load(f)
#         print("Configuración cargada:", config)
    
#     model = CovidModel(
#         num_agents=config["num_agents"],
#         initial_infected_agents=config["initial_infected_agents"],
#         config=config
#     )
#     print("SIMULACIÓN INICIADA------------------")
    
#     for i in range(config["steps"]):
#         print(f":::::Ciclo de simulación {i + 1}:::::")
#         model.step()
    
#     # Obtener y imprimir los resultados
#     results = model.get_results()
#     print("Resultados de la simulación:")
#     for result in results:
#         print(result)
#     print("SIMULACIÓN FINALIZADA------------------")



# import yaml
# from models.model import CovidModel

# if __name__ == "__main__":
#     with open("config/config.yaml", "r") as f:
#         config = yaml.safe_load(f)
#         print("Configuración cargada".format(config))
    
#     model = CovidModel(num_agents=config["num_agents"], config=config)
#     print("SIMULACIÓN INICIADA------------------")
    
#     for i in range(config["steps"]):
#         print(f":::::Agente numero {i} ejecutandose:::::")
#         model.step()
    
#     # Obtener y imprimir los resultados
#     results = model.get_results()
#     print("Resultados de la simulación:")
#     for result in results:
#         print(result)
#     # Guardar los resultados
#     print("SIMULACIÓN FINALIZADA------------------")
