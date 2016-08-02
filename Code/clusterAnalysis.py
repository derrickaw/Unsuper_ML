
import sys

def analysis(fileName):
	f = open(fileName, 'r')
	matrix = []
	clusters = {}
	classes  = []

	for line in f.readlines():
		instanceList = line.strip('\n').split(',')
		if instanceList[0] == '':
			continue 
		if instanceList[0][0] == '@':
			continue
		#print (instanceList)

		if (instanceList[-1] not in clusters):
			clusters[instanceList[-1]] = {}
		if (instanceList[-2] not in classes):
			classes.append(instanceList[-2])
		matrix.append(instanceList)
			
	for key in clusters:
		for item in classes:
			clusters[key][item] = 0

	for line in matrix:
		clusters[line[-1]][line[-2]] += 1

	for key in clusters:
		sum = 0
		deleteEntries = []
		for clusterKey in clusters[key]:
			sum += clusters[key][clusterKey]
		for clusterKey in clusters[key]:
			#print (clusters[key][clusterKey])
			if clusters[key][clusterKey] == 0:
				deleteEntries.append(clusterKey)	
			clusters[key][clusterKey] /= sum #format(clusters[key][clusterKey] / sum, '%')
		
		#clusters[key]['sum'] = sum

		for item in deleteEntries:
			del clusters[key][item]

		maxKey = ""
		maxKeyNum = 0
		for clusterKey in clusters[key]:
			if clusters[key][clusterKey] > maxKeyNum:
				maxKey = clusterKey
				maxKeyNum = clusters[key][clusterKey]

		# Max class per cluster
		print (key, maxKey, clusters[key][maxKey])
		
		#print (key, clusters[key], '\n')

	#del clusters[key][clusterKey]
	#for line in matrix:
	#clusters.sort()
	#print (matrix)
	#print (clusters)
	#print (classes)


def convert(fileName, numClusters):
	f = open(fileName, 'r')
	fn = open(fileName[0:-5] + "_Binary.arff", 'w')
	matrix = []
	front = []
	#clusters = {}
	#classes  = []

	for line in f.readlines():
		instanceList = line.strip('\n').split(',')
		if instanceList[0] == '' or instanceList[0][0] == '@':
			front.append("".join(instanceList))
			continue 
		#if instanceList[0][0] == '@':
		#	front
		#	continue

		#print (instanceList)

		#if (instanceList[-1] not in clusters):
		#	clusters[instanceList[-1]] = {}
		#if (instanceList[-2] not in classes):
		#	classes.append(instanceList[-2])
		matrix.append(instanceList)
	
	classificationEnd = front[-3:]
	front = front[0:-4]
	for i in range(numClusters):
		front.append("@attribute cluster" + str(i) + " numeric")

	front += classificationEnd


	for line in front:
		line += "\n"
		fn.write(line)

	#print (classificationEnd)
	#print ("\n")
	#print (front)


	for line in matrix:
		classification = line[-1]
		clusterNumber = int(line[-2][-1])
		line[-2] = '0'
		line[-1] = '0'

		for i in range(numClusters-1):
			line.append('0')
		line[-(numClusters - clusterNumber) - 1] = '1'
		line[-1] = classification

		newLine = ",".join(line) + "\n"
		#print (newLine)
		fn.write(newLine)


		#print(clusterNumber, line)

	#print (matrix)
	f.close()
	fn.close()

def main():
    args = sys.argv

    fileName = args[1]
    #numClusters = int(args[2])
    
    analysis(fileName)
    #convert(fileName, numClusters)





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