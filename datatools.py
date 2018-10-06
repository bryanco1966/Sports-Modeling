import matplotlib.pyplot as plt
import seaborn as sns

class DataGrapher:

    data_set = None
    def __init__(self, data_set = None):
        print("Let Graph")

    def getdata(self, num):

        self.data_set = num

    def plothist(self, column, bins = 30, color = 'g', size = (12,7)):
        fig = plt.figure(figsize= size)
        ax = plt.gca()
        ax.hist(self.data_set[column], color = color, bins = bins)
        ax.set_title("Histogram of: " + column)
        plt.xlabel(column)

    def plotscat(self, column1, column2, color = 'b', size = (15,7)):
        fig = plt.figure(figsize= size)
        ax = plt.gca()
        ax.scatter(self.data_set[column1], self.data_set[column2], color = color)
        ax.set_title("Scatterplot of: " + column1 + ' and '+ column2)
        plt.xlabel(column1)
        plt.ylabel(column2)


    def plotheatc(self, var, annot = True,  size = (20,30)):
        fig = plt.figure(figsize= size)
        ax = plt.gca()
        ax = sns.heatmap(self.data_set.corr()[[var]], annot=True)
        ax.set_title("Correlations with Target Variable: " + var)

    def boxplot(self, column, size = (9,7), color = 'red'):
        sns.boxplot(self.data_set[column])
