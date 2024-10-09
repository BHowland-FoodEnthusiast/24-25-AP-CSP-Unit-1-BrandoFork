import matplotlib.pyplot as plt
from Music_algorithm_Folder.Music_Algorithm import PityRandom


def run_simulation(num_students, num_runs):
    pity_random = PityRandom(num_students)
    results = [pity_random.pick_student() for _ in range(num_runs)]

    # Calculate distribution
    distribution = {i: results.count(i) for i in range(1, num_students + 1)}

    return distribution


def plot_distribution(distribution):
    students = list(distribution.keys())
    counts = list(distribution.values())

    plt.bar(students, counts)
    plt.xlabel('Student Number')
    plt.ylabel('Number of Times Picked')
    plt.title('Distribution of Student Picks')
    plt.show()


# Example usage
num_students = 30  # Adjust the number of students as needed
num_runs = 100
distribution = run_simulation(num_students, num_runs)
plot_distribution(distribution)
