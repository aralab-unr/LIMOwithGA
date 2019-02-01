from mchgenalg import GeneticAlgorithm
import mchgenalg
import numpy as np
import os

timesEvaluated = 0
bestrmse = -1

# First, define function that will be used to evaluate the fitness
def fitness_function(genome):

    global timesEvaluated
    timesEvaluated += 1

    print("Fitness function invoked "+str(timesEvaluated)+" times")

    #setting parameter values using genome
    # outlier_rejection_quantile in keyframe_ba_monolid.launch
    out_rej_quant = decode_function(genome[0:10])
    if out_rej_quant > 1:
        out_rej_quant = 1

    print('Saving parameters to params.yaml...')
    with open('params.yaml', 'w') as output:
        output.write("out_rej_quant: " + str(out_rej_quant) + "\n") 

    query = "./script.sh"

    #calling limo to calculate rmse value
    os.system(query)     

    # read fitness value as root mean square value (rmse) from text file
    file = open('rmse.txt', 'r')
    rmse = int(file.read())

    global bestrmse
    if bestrmse == -1:
        bestrmse = rmse
    if rmse < bestrmse:
        bestrmse = rmse
        with open('BestParameters.txt', 'a') as output:
            output.write("Best rmse value : " + str(bestrmse) + "\n")
            output.write("outlier_rejection_quantile = " + str(out_rej_quant) + "\n")
            #output.write("Gamma = " + str(gamma) + "\n")
            #output.write("Q_learning = " + str(Q_lr) + "\n")
            #output.write("pi_learning = " + str(pi_lr) + "\n")
            #output.write("random_epsilon = " + str(random_eps) + "\n")
            #output.write("noise_epsilon = " + str(noise_eps) + "\n")
            #output.write("\n")
            output.write("=================================================")
            output.write("\n")

    print('rmse for this run:' + str(rmse))

    print("Best rmse so far : "+str(bestrmse))
    return 1/rmse

def decode_function(genome_partial):

    prod = 0
    for i,e in reversed(list(enumerate(genome_partial))):
        if e == False:
            prod += 0
        else:
            prod += 2**abs(i-len(genome_partial)+1)
    return prod/1000

# Configure the algorithm:
population_size = 30
genome_length = 11
ga = GeneticAlgorithm(fitness_function)
ga.generate_binary_population(size=population_size, genome_length=genome_length)

# How many pairs of individuals should be picked to mate
ga.number_of_pairs = 5

# Selective pressure from interval [1.0, 2.0]
# the lower value, the less will the fitness play role
ga.selective_pressure = 1.5
ga.mutation_rate = 0.1

# If two parents have the same genotype, ignore them and generate TWO random parents
# This helps preventing premature convergence
ga.allow_random_parent = True # default True
# Use single point crossover instead of uniform crossover
ga.single_point_cross_over = False # default False

# Run 100 iteration of the algorithm
# You can call the method several times and adjust some parameters
# (e.g. number_of_pairs, selective_pressure, mutation_rate,
# allow_random_parent, single_point_cross_over)
ga.run(30) # default 1000

best_genome, best_fitness = ga.get_best_genome()

print("BEST CHROMOSOME IS")
print(best_genome)
print("It's decoded value is")
print("outlier_rejection_quantile = " + str(decode_function(best_genome[0:10])))
#print("Gamma = " + str(decode_function(best_genome[11:22])))
#print("Q_learning = " + str(decode_function(best_genome[23:33])))
#print("pi_learning = " + str(decode_function(best_genome[34:44])))
#print("random_epsilon = " + str(decode_function(best_genome[45:55])))
#print("noise_epsilon = " + str(decode_function(best_genome[56:66])))

# If you want, you can have a look at the population:
population = ga.population

# and the fitness of each element:
fitness_vector = ga.get_fitness_vector()
