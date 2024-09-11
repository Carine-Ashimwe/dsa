import os
import psutil
import time

class UniqueInt:
    @staticmethod
    def processFile(inputFilePath):
        """
        Read a list of integers from an input file, generate an output file
        containing a sorted list of unique integers from the input file, and
        store the output file in the 'sample_results' directory within the 'hw01' directory.
        Parameters:
        inputFilePath (str): The full path of the input file to be processed.
        Returns:
        None
        """
        # Prepare file paths
        hw01 = 'hw01'
        sample_results = os.path.join(hw01, 'sample_results')

        # Ensure sample_results directory exists
        os.makedirs(sample_results, exist_ok=True)

        inputFileName = os.path.basename(inputFilePath)
        outputFileName = os.path.splitext(inputFileName)[0] + '_results.txt'
        outputFilePath = os.path.join(sample_results, outputFileName)

        # Read integers from input file
        with open(inputFilePath, 'r') as inputFile:
            integers = []
            for line in inputFile:
                line = line.strip()
                for num in line.split():  
                    if num.lstrip('-').isdigit():  
                        integers.append(int(num))

         # Remove duplicates
        unique_integers = UniqueInt.remove_duplicates(integers)
        # Sort the unique integers (using Bubble Sort)
        UniqueInt.bubble_sort(unique_integers)

        # Write unique integers to the output file
        with open(outputFilePath, 'w') as outputFile:
            for integer in unique_integers:
                outputFile.write(str(integer) + '\n')

        print(f"Unique integers from '{inputFileName}' have been written to '{outputFilePath}'.")

    @staticmethod
    def remove_duplicates(integers):
        """
        Remove duplicates from a list of integers.

        Parameters:
        integers (list): List of integers with possible duplicates.
        
        Returns:
        list: List of unique integers.

        """
        unique_integers = []
        for num in integers:
            if num not in unique_integers:
                unique_integers.append(num)
        return unique_integers

    @staticmethod
    def bubble_sort(integers):
        """
        Sort a list of integers using Bubble Sort algorithm.

         Parameters:
        integers (list): List of integers to be sorted.
        
        Returns:
        None

        """
        n = len(integers)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if integers[j] > integers[j + 1]:
                    integers[j], integers[j + 1] = integers[j + 1], integers[j]
    @staticmethod
    def measure_time_and_memory(func, *args, **kwargs):
        """
        Measure the execution time and memory usage of a function.
        
        Parameters:
        func (function): The function to be measured.
        *args: Variable length argument list for the function.
        **kwargs: Arbitrary keyword arguments for the function.
        
        Returns:
        float: Execution time in milliseconds.
        float: Memory usage in bytes.
        """
        start_time = time.time()
        process = psutil.Process(os.getpid())
        start_memory = process.memory_info().rss
        
        func(*args, **kwargs)
        
        end_time = time.time()
        end_memory = process.memory_info().rss
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        memory_usage = end_memory - start_memory
        
        return execution_time, memory_usage


inputFilePath = input("Enter the input file path: ")
# Measure execution time and memory usage of uniqueint class
execution_time, memory_usage = UniqueInt.measure_time_and_memory(UniqueInt.processFile, inputFilePath)
print(f"Execution time: {execution_time:.2f} ms")
print(f"Memory usage: {memory_usage} bytes")