CS4641 - HW3 - Unsupervised Learning
By: Derrick Williams

Data package:
ABAGAIL, scipy, numpy, and WEKA gui were used to implement this project.  ABAGAIL was used to reconstruct PCA and RP for analysis purposes and for selecting which projections to keep for final dimensionality reduction.  Scipy and numpy were used to find the kurtosis and mean of a projection for ICA.  WEKA was used for more of the heavy lifting in running cross validation for parameter selection for running in neural networks, running clustering algorithms k-Means and EM, all of the dimensionality reduction algorithms, and resampling or adjusting datasets.  The Experimenter module was used to run the CV experiments.
The Explorer module was used to run training, testing, and algorithm experiments.


WEKA GUI:

Experimenter Module (Cross-Validation):
1. Click on the Experimenter Module
2. Click new
3. Change Iteration Control to 1
4. Add appropriate datasets that are being CV trained (see excel sheet for all tests performed and parameters and below)
5. Add appropriate algorithms that are being CV trained (see excel sheet for all tests performed and paremeters and below)
6. Go to Run tab at top, click start
7. Once run is complete with no errors, go to Analysis tab.
8. Click Experiment
9. Make sure Comparison field is Percent Correct
10. Click Perform Test
11. Click Save output to save the output

Explorer Module(Neural Net Training and Testing):
1. Click on the Explorer Module
2. Under the Preprocess tab, click on open file to load whatever training file needs to be trained on.
3. Click on the Classify tab.
4. Choose the classifer to run on the training data.
5. Choose Use Training Set for Training error
6. Choose Supplied Test Set for Testing error
7. Click start
8. Save data once run is complete

Explorer Module(k-Means/EM clustering):
1. Click on the Explorer Module
2. Under the Preprocess tab, click on open file to load whatever training file needs to be trained on.
3. Click on the Cluster tab.
4. Choose the cluster algorithm to run on the training data.
5. Choose Use Training Set for Training error
6. Choose Supplied Test Set for Testing error
7. Choose Classes to clusters evaluation for checking classes to cluster error.
8. Select the Ignore attributes and choose the classification attribute so that the clustering is evaluated on that attribute.
8. Click start
9. Save data once run is complete

Explorer Module(PCA/Information Gain Evaluation):
1. Click on the Explorer Module
2. Under the Preprocess tab, click on open file to load whatever training file needs to be trained on.
3. Click on the Select Attributes tab.
4. Choose the Attribute Evaluator dimensionality algorithm to run on the training data.
5. Choose the Search Method of Ranker.
6. Choose Attribute Selection Mode of full training set.
7. Click start
8. Save data or results once run is complete

Explorer Module(Adjusting dataset or running dimensionality reduction algorithm filters):
1. Click on the Explorer Module
2. Under the Preprocess tab, click on open file to load whatever training file needs to be trained on.
3. Choose Filter (Resampling, Reordering, PCA, ICA, RP, IGAE) that should be run. 
4. Click Apply.
5. Save data once filtering is done.


Algorithms and parameters:
WWQ - kMeans and EM:
Seed: 42	numClusters: 1-11

LR - kMeans and EM:
Seed: 42	numClusters: 16-36

PCA:
Variance Covered: 0.95

RP:
Seeds: 42, 77, 15

ICA and IGAE:
Defaults, if any

NN:
Classifier	Learning Rate	Momentum Rate	Training Set %	# of Epochs		Hidden Layers
MP				0.1				0.2				10%-90%		500-1500			5-11
MP				0.1				0.4				10%-90%		500-1500			5-11
MP 				0.3				0.2				10%-90%		500-1500			5-11
MP 				0.3				0.4				10%-90%		500-1500			5-11

Data Folder:
Files used in or outputted from Weka to model the White Wine Quality and Letter Recognition datasets:

Part 1 and 2 input files:
winequality-white.arff						- original data from UCI converted to arff format
letter-recognition-letterAtEnd.arff			- original data from UCI converted to arff format and adjusted with letter at end

Part 1 output files:
winequality-white-kMeans_Cluster-7_NoNum_QualityEnd.arff 	- 100% of kMeans data after clustering
winequality-white-EM_Cluster-7_NoNum_QualityEnd.arff		- 100% of EM data after clustering

Part 2 output files and Part 3 input files:
winequality-white-PCA.arff					- 100% of WWQ-PCA data after dimensionality reduction
winequality-white-ICA_TEMP_REDUCED1.arff	- 100% of WWQ-ICA data after dimensionality reduction
winequality-white-RP6.arff					- 100% of WWQ-RF data after dimensionality reduction
winequality-white-IGAE.arff					- 100% of WWQ-IGAE data after dimensionality reduction
letter-recognition-letterAtEnd-PCA.arff					- 100% of LR-PCA data after dimensionality reduction
letter-recognition-letterAtEnd-ICA_TEMP_REDUCED1.arff	- 100% of LR-ICA data after dimensionality reduction
letter-recognition-letterAtEnd_RP13.arff				- 100% of LR-RP data after dimensionality reduction
letter-recognition-letterAtEnd-IGAE.arff				- 100% of LR-IGAE data after dimensionality reduction

Part 3 output files:
winequality-white-PCA-kMeans.arff						- 100% of WWQ-PCA-kMeans
winequality-white-PCA-EM.arff							- 100% of WWQ-PCA-EM
winequality-white-ICA_TEMP_REDUCED1-kMeans.arff			- 100% of WWQ-ICA-kMeans
winequality-white-ICA-TEMP_REDUCED1-EM.arff				- 100% of WWQ-ICA-EM
winequality-white-RP6-kMeans.arff						- 100% of WWQ-RF-kMeans
winequality-white-RP6-EM.arff							- 100% of WWQ-RF-EM
winequality-white-IGAE-kMeans.arff						- 100% of WWQ-IGAE
winequality-white-IGAE-EM.arff							- 100% of WWQ-IGAE
letter-recognition-letterAtEnd-PCA-kMeans.arff					- 100% of LR-PCA
letter-recognition-letterAtEnd-PCA-EM.arff						- 100% of LR-PCA
letter-recognition-letterAtEnd-ICA_TEMP_REDUCED1-kMeans.arff	- 100% of LR-ICA
letter-recognition-letterAtEnd-ICA_TEMP_REDUCED1-EM.arff		- 100% of LR-ICA
letter-recognition-letterAtEnd_RP13-kMeans.arff					- 100% of LR-RP
letter-recognition-letterAtEnd_RP13-EM.arff						- 100% of LR-RP
letter-recognition-letterAtEnd-IGAE-kMeans.arff					- 100% of LR-IGAE
letter-recognition-letterAtEnd-IGAE-EM.arff						- 100% of LR-IGAE

Part 4 Input Files to Neural Network:
winequality-white-PCA.arff					- 100% of PCA dataset
winequality-white-PCA-Train.arff			- 70% of PCA data for training neural networks with
winequality-white-PCA-Test.arff				- 30% of PCA data for testing neural networks with
winequality-white-PCA-Train-10.arff			- 10% of the training data file for CV
winequality-white-PCA-Train-20.arff			- 20% of the training data file for CV
winequality-white-PCA-Train-30.arff			- 30% of the training data file for CV
winequality-white-PCA-Train-40.arff			- 40% of the training data file for CV
winequality-white-PCA-Train-50.arff			- 50% of the training data file for CV
winequality-white-PCA-Train-60.arff			- 60% of the training data file for CV
winequality-white-PCA-Train-70.arff			- 70% of the training data file for CV
winequality-white-PCA-Train-80.arff			- 80% of the training data file for CV
winequality-white-PCA-Train-90.arff			- 90% of the training data file for CV
winequality-white-ICA_TEMP_REDUCED1.arff	- 100% of ICA dataset 
winequality-white-ICA-Train.arff			- 70% of ICA data for training neural networks with
winequality-white-ICA-Test.arff				- 30% of ICA data for testing neural networks with
winequality-white-ICA-Train-10.arff			- 10% of the training data file for CV
winequality-white-ICA-Train-20.arff			- 20% of the training data file for CV
winequality-white-ICA-Train-30.arff			- 30% of the training data file for CV
winequality-white-ICA-Train-40.arff			- 40% of the training data file for CV
winequality-white-ICA-Train-50.arff			- 50% of the training data file for CV
winequality-white-ICA-Train-60.arff			- 60% of the training data file for CV
winequality-white-ICA-Train-70.arff			- 70% of the training data file for CV
winequality-white-ICA-Train-80.arff			- 80% of the training data file for CV
winequality-white-ICA-Train-90.arff			- 90% of the training data file for CV
winequality-white_RP6.arff					- 100% of RP dataset
winequality-white_RP6-Train.arff			- 70% of RP data for training neural networks with
winequality-white_RP6-Test.arff				- 30% of RP data for testing neural networks with 
winequality-white-RP6-Train-10.arff			- 10% of the training data file for CV
winequality-white-RP6-Train-20.arff			- 20% of the training data file for CV
winequality-white-RP6-Train-30.arff			- 30% of the training data file for CV
winequality-white-RP6-Train-40.arff			- 40% of the training data file for CV
winequality-white-RP6-Train-50.arff			- 50% of the training data file for CV
winequality-white-RP6-Train-60.arff			- 60% of the training data file for CV
winequality-white-RP6-Train-70.arff			- 70% of the training data file for CV
winequality-white-RP6-Train-80.arff			- 80% of the training data file for CV
winequality-white-RP6-Train-90.arff			- 90% of the training data file for CV
winequality-white-IGAE.arff					- 100% of IGAE dataset
winequality-white-IGAE-Train.arff			- 70% of IGAE data for training neural networks with
winequality-white-IGAE-Test.arff			- 30% of IGAE data for testing neural networks with
winequality-white-IGAE-Train-10.arff		- 10% of the training data file for CV
winequality-white-IGAE-Train-20.arff		- 20% of the training data file for CV
winequality-white-IGAE-Train-30.arff		- 30% of the training data file for CV
winequality-white-IGAE-Train-40.arff		- 40% of the training data file for CV
winequality-white-IGAE-Train-50.arff		- 50% of the training data file for CV
winequality-white-IGAE-Train-60.arff		- 60% of the training data file for CV
winequality-white-IGAE-Train-70.arff		- 70% of the training data file for CV
winequality-white-IGAE-Train-80.arff		- 80% of the training data file for CV
winequality-white-IGAE-Train-90.arff		- 90% of the training data file for CV

Part 5 Input Files for Neural Network:
winequality-white-kMeans_Cluster-7_NoNum_QualityEnd.arff			- 100% of kMeans clustered dataset
winequality-white-kMeans_Cluster-7_NoNum_QualityEnd-Train.arff		- 70% of kMeans data for training neural networks with
winequality-white-kMeans_Cluster-7_NoNum_QualityEnd-Test.arff		- 30% of kMeans data for testing neural networks with
winequality-white-kMeans_Cluster-7_NoNum_QualityEnd-Train-10.arff	- 10% of the training data file for CV
winequality-white-kMeans_Cluster-7_NoNum_QualityEnd-Train-20.arff	- 20% of the training data file for CV
winequality-white-kMeans_Cluster-7_NoNum_QualityEnd-Train-30.arff	- 30% of the training data file for CV
winequality-white-kMeans_Cluster-7_NoNum_QualityEnd-Train-40.arff	- 40% of the training data file for CV
winequality-white-kMeans_Cluster-7_NoNum_QualityEnd-Train-50.arff	- 50% of the training data file for CV
winequality-white-kMeans_Cluster-7_NoNum_QualityEnd-Train-60.arff	- 60% of the training data file for CV
winequality-white-kMeans_Cluster-7_NoNum_QualityEnd-Train-70.arff	- 70% of the training data file for CV
winequality-white-kMeans_Cluster-7_NoNum_QualityEnd-Train-80.arff	- 80% of the training data file for CV
winequality-white-kMeans_Cluster-7_NoNum_QualityEnd-Train-90.arff	- 90% of the training data file for CV
winequality-white-EM_Cluster-7_NoNum_QualityEnd.arff				- 100% of EM clustered dataset
winequality-white-EM_Cluster-7_NoNum_QualityEnd-Train.arff			- 70% of EM data for training neural networks with
winequality-white-EM_Cluster-7_NoNum_QualityEnd-Test.arff			- 30% of EM data for testing neural networks with
winequality-white-EM_Cluster-7_NoNum_QualityEnd-Train-10.arff		- 10% of the training data file for CV
winequality-white-EM_Cluster-7_NoNum_QualityEnd-Train-20.arff		- 20% of the training data file for CV
winequality-white-EM_Cluster-7_NoNum_QualityEnd-Train-30.arff		- 30% of the training data file for CV
winequality-white-EM_Cluster-7_NoNum_QualityEnd-Train-40.arff		- 40% of the training data file for CV
winequality-white-EM_Cluster-7_NoNum_QualityEnd-Train-50.arff		- 50% of the training data file for CV
winequality-white-EM_Cluster-7_NoNum_QualityEnd-Train-60.arff		- 60% of the training data file for CV
winequality-white-EM_Cluster-7_NoNum_QualityEnd-Train-70.arff		- 70% of the training data file for CV
winequality-white-EM_Cluster-7_NoNum_QualityEnd-Train-80.arff		- 80% of the training data file for CV
winequality-white-EM_Cluster-7_NoNum_QualityEnd-Train-90.arff		- 90% of the training data file for CV

Code Folder:
icaAnalysis.py 			- Calculate kurtosis of each ICA projection
						- Use "python icaAnalysis.py fileName"
						- fileName - file name of file that you want to calculate kurtosis on
meanSquareError.py		- Calculate square error with between original file and changed file (projection analysis mainly for RP)
						- Use "python meanSquareError.py ../Data/originalFile.arff ../Data/firstChangedFile.arff N"
						- originalFile - being the original dataset file (WWQ or LR)
						- firstChangedFile - being the first file to compare to
						- N - number of files to compare
AFilterRunner.java		- Support file for RPRunner.java
RPRunner.java			- Randomized Projection


Results Folder:
HW3Results.xlsx			- results from all ABAGAIL and Weka runs for WhiteWineTest and Letter Recognition datasets

ABAGAIL Running Code:
1. An ABAGAIL folder is provided in the Code folder that has the java packages to compile and run the provided code.  This folder should be placed somewhere on your network where you want to run the code such as your Desktop.  
2. The java files in the Code folder and the data files in the Data folder should be placed inside the ABAGAIL folder that you just moved to the location of Desktop/ABAGAIL/src/opt/test/.
3. Navigate now to this location Desktop/ABAGAIL ('cd ABAGAIL', if you are currently in the Desktop folder).
4. Type 'ant', this will compile the files
5. Type 'java -cp ABAGAIL.jar RPRunner ./projectFiles/letter-recognition-letterAtEnd.arff 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16' to run the entire file for LR dataset that will run the RP algorithm.



Original Files from UCI Machine Learning Respository not used in Weka:
letter-recognition.data                     - original data from UCI Machine Learning Respository
letter-recognition.names                    - original name file from UCI Machine Learning Respository
winequality-white.csv						- original data from UCI Machine Learning Respository
winequality.names							- original name file from UCI Machine Learning Respository
