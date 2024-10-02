const fs = require('fs');
const path = require('path');
const process = require('process');

// Define the UniqueInt class
class UniqueInt {
    // Static method to process the file
    static processFile(inputFilePath) {
        // Use path.resolve to construct the full path
        const resolvedInputFilePath = path.resolve(inputFilePath);

        if (!fs.existsSync(resolvedInputFilePath)) {
            console.error(`Error: File '${resolvedInputFilePath}' does not exist.`);
            return;
        }

        const hw01 = 'hw01';
        const sample_results = path.join(hw01, 'sample_results');

        if (!fs.existsSync(sample_results)) {
            fs.mkdirSync(sample_results, { recursive: true });
        }

        const inputFileName = path.basename(resolvedInputFilePath);
        const outputFileName = path.parse(inputFileName).name + '_results.txt';
        const outputFilePath = path.join(sample_results, outputFileName);

        const inputFileContent = fs.readFileSync(resolvedInputFilePath, 'utf8');
        const integers = [];
        const lines = inputFileContent.split('\n');

        lines.forEach(line => {
            const nums = line.trim().split(/\s+/);
            if (nums.length === 1 && /^-?\d+$/.test(nums[0])) {
                integers.push(parseInt(nums[0], 10));
            }
        });

        const uniqueIntegers = UniqueInt.removeDuplicates(integers);
        UniqueInt.bubbleSort(uniqueIntegers);

        fs.writeFileSync(outputFilePath, uniqueIntegers.join('\n'));

        console.log(`Unique integers from '${inputFileName}' have been written to '${outputFilePath}'.`);
    }

    static removeDuplicates(integers) {
        return [...new Set(integers)];
    }

    static bubbleSort(integers) {
        const n = integers.length;
        for (let i = 0; i < n - 1; i++) {
            for (let j = 0; j < n - i - 1; j++) {
                if (integers[j] > integers[j + 1]) {
                    const temp = integers[j];
                    integers[j] = integers[j + 1];
                    integers[j + 1] = temp;
                }
            }
        }
    }

    static measureTimeAndMemory(func, ...args) {
        const startTime = process.hrtime.bigint();
        const startMemory = process.memoryUsage().rss;

        func(...args);

        const endTime = process.hrtime.bigint();
        const endMemory = process.memoryUsage().rss;

        const executionTimeMs = Number(endTime - startTime) / 1000000;
        const memoryUsage = endMemory - startMemory;

        return {
            executionTime: executionTimeMs,
            memoryUsage: memoryUsage
        };
    }
}

// Example usage: Process the input file and measure time & memory
const inputFilePath = './sample_inputs/small_sample_input_02.txt';  // Updated to relative path
const result = UniqueInt.measureTimeAndMemory(UniqueInt.processFile, inputFilePath);

console.log(`Execution time: ${result.executionTime.toFixed(2)} ms`);
console.log(`Memory usage: ${result.memoryUsage} bytes`);
