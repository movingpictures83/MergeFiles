import sys
import glob
import PyPluMA

class MergeFilesPlugin:
    def input(self, filename):
        patternfile = open(filename, 'r')
        self.patterns = []
        for line in patternfile:
            self.patterns.append(line.strip())


    def run(self):
      self.data = set()
      for taxclass in self.patterns:
        print(PyPluMA.prefix()+"/"+taxclass)
        pattern = r""+PyPluMA.prefix()+"/"+taxclass
        #"*/**/*."+taxclass+".txt"
        results = glob.glob(pattern)

        for filename in results:
           txtfile = open(filename, 'r')
           for line in txtfile:
              self.data.add(line.strip())

    def output(self, filename):
        outfile = open(filename, 'w')
        for element in self.data:
           outfile.write(element+"\n")
