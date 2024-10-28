import yaml
from models.model import CovidModel

if __name__ == "__main__":
    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)
        print("Configuración cargada".format(config))
    
    model = CovidModel(num_agents=config["num_agents"], config=config)
    print("SIMULACIÓN INICIADA------------------")
    
    for i in range(config["steps"]):
        print(f":::::Agente numero {i} ejecutandose:::::")
        model.step()
    
    # Obtener y imprimir los resultados
    results = model.get_results()
    print("Resultados de la simulación:")
    for result in results:
        print(result)
    # Guardar los resultados
    print("SIMULACIÓN FINALIZADA------------------")
