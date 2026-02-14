import sys
from .topsis_calc import run_topsis, validate_inputs

def main():
    if len(sys.argv) != 5:
        print("Error: Incorrect number of parameters")
        print("Usage: topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        print("Example: topsis data.csv \"1,1,1,2\" \"+,+,-,+\" result.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]
    
    try:
        run_topsis(input_file, weights, impacts, output_file)
        print(f"Results saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
