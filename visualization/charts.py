import matplotlib.pyplot as plt

def plot_infection_rate(results):
    steps = range(len(results))
    infection_rates = [result['infection_rate'] for result in results]

    plt.plot(steps, infection_rates)
    plt.xlabel('Time Step')
    plt.ylabel('Infection Rate')
    plt.title('Infection Rate Over Time')
    plt.show()
