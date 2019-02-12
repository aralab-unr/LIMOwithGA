import os

sequence_number = 01
num_runs = 10
if os.path.isfile('/tmp/testfitnesses_dump_' + sequence_number + '.txt'):
    os.system("rm -f /tmp/testfitnesses_dump_" + sequence_number + ".txt")

for x in range(1, num_runs):
    query = "./test_script.sh"
    os.system(query)

    # read fitness value as root mean square value (rmse) from text file
    file = open('/tmp/rmse_output.txt', 'r')
    rmse = float(file.read())

    print('Saving fitnesses for each evaluation')
    with open('/tmp/testfitnesses_dump_' + sequence_number + '.txt', 'a') as output:
        output.write("" + str(x) + " " + str(rmse) + "\n") 

    os.system("rm -f /tmp/rmse_output.txt")


