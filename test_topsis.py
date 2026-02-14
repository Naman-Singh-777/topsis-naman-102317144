import sys
import os

# Add package directory to path
package_dir = os.path.join(os.path.dirname(__file__), 'Topsis-Naman-102317144')
sys.path.insert(0, package_dir)

from topsis_calc import run_topsis
import pandas as pd

def test_basic_topsis():
    """Test basic TOPSIS functionality"""
    print("Testing basic TOPSIS...")
    
    # Create test data
    test_data = {
        'Fund Name': ['M1', 'M2', 'M3', 'M4', 'M5'],
        'P1': [0.84, 0.91, 0.79, 0.78, 0.94],
        'P2': [0.71, 0.83, 0.62, 0.61, 0.88],
        'P3': [6.7, 7.0, 4.8, 6.4, 3.6],
        'P4': [42.1, 31.7, 46.7, 42.4, 62.2],
        'P5': [12.59, 10.11, 13.23, 12.55, 16.91]
    }
    
    df = pd.DataFrame(test_data)
    df.to_csv('test_input.csv', index=False)
    
    # Run TOPSIS
    result = run_topsis(
        'test_input.csv',
        '1,1,1,1,1',
        '+,+,-,+,+',
        'test_output.csv'
    )
    
    print("✓ TOPSIS executed successfully")
    print("\nResults:")
    print(result[['Fund Name', 'Topsis Score', 'Rank']])
    
    # Verify output
    assert 'Topsis Score' in result.columns
    assert 'Rank' in result.columns
    assert len(result) == 5
    
    print("\n✓ All assertions passed")
    
    # Clean up
    os.remove('test_input.csv')
    os.remove('test_output.csv')
    
    print("✓ Test completed successfully!\n")

def test_error_handling():
    """Test error handling"""
    print("Testing error handling...")
    
    # Test 1: File not found
    try:
        run_topsis('nonexistent.csv', '1,1', '+,+', 'out.csv')
        print("✗ Should have raised FileNotFoundError")
    except FileNotFoundError:
        print("✓ FileNotFoundError handled correctly")
    
    # Test 2: Invalid weights format
    df = pd.DataFrame({'Name': ['A', 'B'], 'X': [1, 2], 'Y': [3, 4]})
    df.to_csv('temp.csv', index=False)
    
    try:
        run_topsis('temp.csv', 'abc', '+,+', 'out.csv')
        print("✗ Should have raised ValueError")
    except ValueError:
        print("✓ Invalid weights format handled correctly")
    
    # Test 3: Mismatched counts
    try:
        run_topsis('temp.csv', '1', '+,+', 'out.csv')
        print("✗ Should have raised ValueError")
    except ValueError:
        print("✓ Mismatched counts handled correctly")
    
    os.remove('temp.csv')
    
    print("✓ Error handling tests passed!\n")

if __name__ == "__main__":
    print("="*50)
    print("TOPSIS Package Test Suite")
    print("="*50 + "\n")
    
    test_basic_topsis()
    test_error_handling()
    
    print("="*50)
    print("All tests passed! ✓")
    print("="*50)
