
import sys
import statistics
import scipy.stats
import numpy
import matplotlib.pyplot as plt




def readIn(fileName):
	f = open(fileName, 'r')
	matrix = []

	for line in f.readlines():
		instanceList = line.strip('\n').split(',')
		if instanceList[0] == '' or instanceList[0][0] == '@':
			continue 
		matrix.append(instanceList)

	return matrix


def measureError(matrix1, matrix2):
	
	sumOfErrors = [0] * (len(matrix1[0]) - 1)

	for i in range(len(matrix1)):
		for j in range(len(matrix1[0]) - 1):
			sumOfErrors[j] += (float(matrix1[i][j]) - float(matrix2[i][j]))**2

	return sum(sumOfErrors)

	#clusters = {}
	#classes  = []
	
	#print (len(matrix1))
	#print (len(matrix2))


	




	# kurtosis  = [0] * len(matrix[0])
	# means     = [0] * len(matrix[0])
	
	# for i in range(len(means)-1):
	# 	means[i] = []


	# for line in matrix:
	# 	for i in range(len(line)-1):
	# 		line[i] = float(line[i])
	# 	for i in range(len(line)-1):
	# 		means[i].append(line[i])
	
	# for mean in means:
	# 	#print (statistics.mean(mean))
	# 	print ("Kurtosis", scipy.stats.kurtosis(mean, None, fisher=False, bias=False))
	# 	print ("Mean",numpy.mean(mean))





	#print (statistics.mean(tempMean))
	# for line in matrix:
	# 	for i in range(len(line)):
	# 		means[i] += line[i]
	# for i in range(len(means)):
	# 	means[i] /= len(matrix)

	#print (means)


		# if (instanceList[-1] not in clusters):
		# 	clusters[instanceList[-1]] = {}
		# if (instanceList[-2] not in classes):
		# 	classes.append(instanceList[-2])
	#print (matrix)



	# for key in clusters:
	# 	for item in classes:
	# 		clusters[key][item] = 0

	# for line in matrix:
	# 	clusters[line[-1]][line[-2]] += 1

	# for key in clusters:
	# 	sum = 0
	# 	deleteEntries = []
	# 	for clusterKey in clusters[key]:
	# 		sum += clusters[key][clusterKey]
	# 	for clusterKey in clusters[key]:
	# 		#print (clusters[key][clusterKey])
	# 		if clusters[key][clusterKey] == 0:
	# 			deleteEntries.append(clusterKey)	
	# 		clusters[key][clusterKey] /= sum #format(clusters[key][clusterKey] / sum, '%')
		
	# 	#clusters[key]['sum'] = sum

	# 	for item in deleteEntries:
	# 		del clusters[key][item]

	# 	maxKey = ""
	# 	maxKeyNum = 0
	# 	for clusterKey in clusters[key]:
	# 		if clusters[key][clusterKey] > maxKeyNum:
	# 			maxKey = clusterKey
	# 			maxKeyNum = clusters[key][clusterKey]

	# 	# Max class per cluster
	# 	print (key, maxKey, clusters[key][maxKey])
		
		#print (key, clusters[key], '\n')

	#del clusters[key][clusterKey]
	#for line in matrix:
	#clusters.sort()
	#print (matrix)
	#print (clusters)
	#print (classes)






def main():
    args = sys.argv

    firstFile   = args[1]
    secondFile  = args[2]
    extension   = secondFile[-6:]
    #print (extension)
    numberFiles = int(args[3])

    matrix1 = readIn(firstFile)
    #print (secondFile[-7])
    errors = []
    for i in range(1,numberFiles+1):
    	#print (i)
    	newSecondFile = secondFile[0:-7] + str(i) + extension
    	#print (secondFile)
    	matrix2 = readIn(newSecondFile)
    	errors.append((measureError(matrix1, matrix2), i))

    errors.sort(reverse=True)
    worstError = errors[0][0]

    print (errors)
    # Normalize
    #for i in range(len(errors)):
    #	errors[i] = (errors[i][0] / worstError, errors[i][1])


    print (errors)
    x,y = zip(*errors)
    #print (x,y)
    plt.plot(x)
    plt.xlabel("RP Combination ID")
    plt.ylabel("Sum of Squared errors")
    plt.show()
	#plt.ylabel('some numbers')




    # if len(args) != 6:
    #     print ("Incorrect number of arguments - Format-> python evalSim.py "
    #            "world2.csv [police, noWest, random] [0.01-1.00] [capacity,path,"
    #            "or both] [# of simulations]")
    #     exit(0)

    # mapFile = args[1]
    # RUN_METHOD = args[2] # 1(Police), 2(No West), 3(Random, Redlight)
    # PARKING_CAPACITY = float(args[3])
    # plottingMethod = args[4]
    # NUM_SIMULATIONS = int(args[5])




if __name__=="__main__":
	main()