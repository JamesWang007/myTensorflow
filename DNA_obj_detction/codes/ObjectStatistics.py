import numpy as np
import matplotlib.pyplot as plt
import re


class ObjectStatistics():
    def __init__(self, file=None):
        self.__Ntype = 6
        self.__fileLines = []
        self.__typeCounts = np.zeros(self.__Ntype, dtype=int)
        self.loadAFile(file)

    def loadAFile(self, file=None):
        try:
            f = None
            if file:
                f = open(file, 'r')
            else:
                f = open('../file.txt', 'r')
            for line in f.readlines():
                self.__fileLines.append(line.strip()) # delete the ending '\n'
        finally:
            if f:
                f.close()

    def showFileNodeLise(self):
        for line in self.__fileLines:
            print(line)

    def getFileContent(self):
        return self.__fileLines

    def analysis(self):
        for line in self.__fileLines:
            ins = re.findall('[0-9]+', line)
            self.__typeCounts[int(ins[1])-1] += 1

    def showDist(self):
        x = [v+1 for v in list(range(self.__Ntype))]
        y = self.__typeCounts

        tick_label = ['Thin L', 'Wide L', 'Thin Rec', 'Small Rec', 'Tiny Tile', 'Others']
        plt.bar(x, y, tick_label=tick_label, width=0.8, color=['green'])

        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Type Dist.')

        plt.show()

def main():
    st = ObjectStatistics('../txtData/obj.txt')
    st.analysis()
    st.showDist()
    #fContent = st.getFileContent()
    st.showFileNodeLise()

if __name__ == '__main__':
    main()



