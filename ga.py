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

    # max_number_landmarks_near_bin in keyframe_ba_monolid.launch
    max_number_landmarks_near_bin = decode_function(genome[11:22])*1000
    if max_number_landmarks_near_bin > 999:
        max_number_landmarks_near_bin = 999.0

    # max_number_landmarks_middle_bin in keyframe_ba_monolid.launch
    max_number_landmarks_middle_bin = decode_function(genome[23:33])*1000
    if max_number_landmarks_middle_bin > 999:
        max_number_landmarks_middle_bin = 999.0

    # max_number_landmarks_far_bin in keyframe_ba_monolid.launch
    max_number_landmarks_far_bin = decode_function(genome[34:44])*1000
    if max_number_landmarks_far_bin > 999:
        max_number_landmarks_far_bin = 999.0

    # shrubbery_weight in keyframe_ba_monolid.launch
    shrubbery_weight = decode_function(genome[45:55])
    if shrubbery_weight > 1:
        shrubbery_weight = 1


    print('Saving parameters to params.yaml...')
    with open('/tmp/params.yaml', 'w') as output:
        output.write("outlier_rejection_quantile: " + str(out_rej_quant) + "\n") 
        output.write("max_number_landmarks_near_bin: " + str(max_number_landmarks_near_bin) + "\n") 
        output.write("max_number_landmarks_middle_bin: " + str(max_number_landmarks_middle_bin) + "\n") 
        output.write("max_number_landmarks_far_bin: " + str(max_number_landmarks_far_bin) + "\n") 
        output.write("shrubbery_weight: " + str(shrubbery_weight) + "\n") 

    query = "./script.sh"

    #calling limo to calculate rmse value
    os.system(query)     

    # read fitness value as root mean square value (rmse) from text file
    file = open('/tmp/rmse_output1.txt', 'r')
    rmse1 = float(file.read())

    file = open('/tmp/rmse_output2.txt', 'r')
    rmse2 = float(file.read())

    # Average of two RMSE values
    rmse_avg = rmse1 + rmse2
    rmse_avg = rmse_avg/2

    print('Saving fitnesses for each evaluation')
    with open('/tmp/fitnesses_dump.txt', 'a') as output:
        output.write("" + str(timesEvaluated) + " " + str(rmse1) + " " + str(rmse2) + " " + str(rmse_avg) + "\n") 

    os.system("rm -f /tmp/rmse_output1.txt")
    os.system("rm -f /tmp/rmse_output2.txt")

    global bestrmse
    if bestrmse == -1:
        bestrmse = rmse_avg
    if rmse_avg < bestrmse:
        bestrmse = rmse_avg
        with open('/tmp/BestParameters.txt', 'a') as output:
            output.write("Best rmse value : " + str(bestrmse) + "\n")
            output.write("outlier_rejection_quantile = " + str(out_rej_quant) + "\n")
            output.write("max_number_landmarks_near_bin = " + str(max_number_landmarks_near_bin) + "\n")
            output.write("max_number_landmarks_middle_bin = " + str(max_number_landmarks_middle_bin) + "\n")
            output.write("max_number_landmarks_far_bin = " + str(max_number_landmarks_far_bin) + "\n")
            output.write("shrubbery_weight = " + str(shrubbery_weight) + "\n")
            output.write("=================================================")
            output.write("\n")

    print('Average rmse for this run:' + str(rmse_avg))

    print("Best rmse so far : "+str(bestrmse))
    return 1/rmse_avg

def decode_function(genome_partial):

    prod = 0
    for i,e in reversed(list(enumerate(genome_partial))):
        if e == False:
            prod += 0
        else:
            prod += 2**abs(i-len(genome_partial)+1)
    return prod/1000

if os.path.isfile('/tmp/fitnesses_dump.txt'):
    os.system("rm -f /tmp/fitnesses_dump.txt")
# Configure the algorithm:
population_size = 50
genome_length = 55
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
ga.run(50) # default 1000

best_genome, best_fitness = ga.get_best_genome()

print("BEST FITNESS IS")
print(best_fitness)
print("BEST CHROMOSOME IS")
print(best_genome)
print("It's decoded value is:")
print("outlier_rejection_quantile = " + str(decode_function(best_genome[0:10])))
print("max_number_landmarks_near_bin = " + str(decode_function(best_genome[11:22])*1000))
print("max_number_landmarks_middle_bin = " + str(decode_function(best_genome[23:33])*1000))
print("max_number_landmarks_far_bin = " + str(decode_function(best_genome[34:44])*1000))
print("shrubbery_weight = " + str(decode_function(best_genome[45:55])))
#print("noise_epsilon = " + str(decode_function(best_genome[56:66])))

# If you want, you can have a look at the population:
population = ga.population

# and the fitness of each element:
fitness_vector = ga.get_fitness_vector()
