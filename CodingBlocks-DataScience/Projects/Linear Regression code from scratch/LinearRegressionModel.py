# Can add method to retrieve weights for unstandardized data.

import numpy as np;
import matplotlib.pyplot as plt;

class linearRegressionModel:
    def __init__(self, inputValues, trueValues, epochs = 1000, alpha = 0.01):
        self.epochs = epochs;
        self.alpha = alpha;
        self.inputValues = inputValues;
        self.trueValues = trueValues;
        self.standInput = self.prepareInputValue(inputValues);
        self.thetas = self.prepareThetas();
        self.standTrue = self.prepareTrueValue(trueValues);
        self.lossArray = [];

    def prepareInputValue(self, values):
        mean = np.mean(values, 1).reshape((values.shape[0], 1));
        stdDev = np.std(values, 1).reshape((values.shape[0], 1));
        standInput =  (values - mean)/stdDev;
        # Ones added to last row.
        standInput = np.vstack((standInput, np.ones(inputValues.shape[1])));
        return standInput;

    def prepareTrueValue(self, values):
        mean = np.mean(values);
        stdDev = np.std(values);
        return (values - mean)/stdDev;

    def prepareThetas(self):
        # Reshaping to convert from (n,) -> (n, 1) (To avoid multiplication errors)
    	return np.zeros((self.standInput.shape[0])).reshape(self.standInput.shape[0], 1);

    # Hypothesis function gives value for just 1 point.
    # This function sums up all hypothesis functions for all values.
    def getCumulativeHypothesisFunction(self, thetas, inputValues):
        hypothesisFun = 0;
        for i in range(thetas.shape[0]):
            hypothesisFun += thetas[i]*inputValues[i, :];
        return hypothesisFun;

    def getGradient(self, thetas, inputValues, trueValues, thetaIndex):
        lossDerivative = np.sum((self.getCumulativeHypothesisFunction(thetas, inputValues) - trueValues)*(inputValues[thetaIndex, :]));
        return lossDerivative;
    
#     Returns average loss.
    def getLoss(self, thetas, inputValues, trueValues):
        return np.sum(((thetas * inputValues - trueValues)**2)/inputValues.shape[1])

    def performGradientDescent(self):
        for i in range(self.epochs):
            for j in range(self.standInput.shape[0]):
                lossDerivative = self.getGradient(self.thetas, self.standInput, self.standTrue, j);
                self.thetas[j] = self.thetas[j] - self.alpha * lossDerivative;
            self.lossArray = np.append(self.lossArray, self.getLoss(self.thetas, self.standInput, self.standTrue));
    
    def plotLoss(self):
        plt.plot(self.lossArray);

