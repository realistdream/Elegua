import math
from collections import Counter
import matplotlib.pyplot as plt
from scipy.stats import chisquare

def calculate_entropy(data):
    """
    Calculate the Shannon entropy of the input string.
    """
    if not data:
        return 0
    counter = Counter(data)
    total_length = len(data)
    entropy = -sum((count / total_length) * math.log2(count / total_length) for count in counter.values())
    return entropy

def visualize_character_frequencies(data):
    """
    Visualize the frequency of characters in the string.
    """
    counter = Counter(data)
    plt.bar(counter.keys(), counter.values(), color='skyblue')
    plt.xlabel("Characters")
    plt.ylabel("Frequency")
    plt.title("Character Frequency Distribution")
    plt.show()

def calculate_block_entropies(data, block_size):
    """
    Calculate entropy for fixed-size blocks of the string.
    """
    if len(data) < block_size:
        return [calculate_entropy(data)]
    block_entropies = [
        calculate_entropy(data[i:i+block_size]) 
        for i in range(0, len(data), block_size)
    ]
    return block_entropies

def assess_randomness_and_encryption(data):
    """
    Assess the string's randomness and likelihood of encryption based on entropy.
    """
    entropy = calculate_entropy(data)
    max_entropy = math.log2(len(set(data)))  # Maximum possible entropy for the alphabet
    normalized_entropy = entropy / max_entropy if max_entropy > 0 else 0

    if normalized_entropy > 0.8:
        randomness = "High"
        likely_encrypted = True
    elif normalized_entropy > 0.5:
        randomness = "Moderate"
        likely_encrypted = False
    else:
        randomness = "Low"
        likely_encrypted = False

    return {
        "Entropy": entropy,
        "Max Entropy": max_entropy,
        "Normalized Entropy": normalized_entropy,
        "Randomness": randomness,
        "Likely Encrypted": likely_encrypted
    }

def check_patterns(data):
    """
    Check for repeating patterns or structures in the string.
    """
    length = len(data)
    for i in range(1, length // 2 + 1):
        if data[:i] * (length // i) == data[:length - (length % i)]:
            return f"Pattern detected: '{data[:i]}' repeating."
    return "No repeating patterns detected."

def check_encryption_patterns(data, block_size=16):
    """
    Perform encryption-specific checks.
    """
    # Uniformity check
    counter = Counter(data)
    total_length = len(data)
    uniformity_score = len(counter) / total_length

    # Repeating blocks (ECB detection)
    blocks = [data[i:i+block_size] for i in range(0, len(data), block_size)]
    unique_blocks = set(blocks)
    ecb_detection = len(unique_blocks) < len(blocks)

    # Chi-Square test
    expected_frequency = total_length / len(counter) if counter else 0
    observed_frequencies = list(counter.values())
    chi_square_stat, p_value = chisquare(observed_frequencies)

    return {
        "Uniformity Score": uniformity_score,
        "ECB Detection": ecb_detection,
        "Chi-Square Statistic": chi_square_stat,
        "Chi-Square P-Value": p_value,
        "Likely Encrypted": p_value < 0.05
    }

def main():
    # Input string
    data = input("Enter a string to analyze: ").strip()

    # Analysis
    result = assess_randomness_and_encryption(data)
    patterns = check_patterns(data)
    block_size = int(input("Enter block size for entropy analysis: "))
    block_entropies = calculate_block_entropies(data, block_size)
    encryption_checks = check_encryption_patterns(data, block_size)

    # Display results
    print("\n=== Analysis Results ===")
    print(f"String: {data}")
    print(f"Entropy: {result['Entropy']:.4f}")
    print(f"Max Possible Entropy: {result['Max Entropy']:.4f}")
    print(f"Normalized Entropy: {result['Normalized Entropy']:.4f}")
    print(f"Randomness: {result['Randomness']}")
    print(f"Likely Encrypted (Based on Entropy): {result['Likely Encrypted']}")
    print(f"Pattern Analysis: {patterns}")
    print("\nBlock Entropies:")
    for i, entropy in enumerate(block_entropies):
        print(f"Block {i + 1}: {entropy:.4f}")

    print("\n=== Encryption Pattern Checks ===")
    print(f"Uniformity Score: {encryption_checks['Uniformity Score']:.4f}")
    print(f"ECB Detection (Repeating Blocks): {'Yes' if encryption_checks['ECB Detection'] else 'No'}")
    print(f"Chi-Square Statistic: {encryption_checks['Chi-Square Statistic']:.4f}")
    print(f"Chi-Square P-Value: {encryption_checks['Chi-Square P-Value']:.4f}")
    print(f"Likely Encrypted (Based on Chi-Square Test): {encryption_checks['Likely Encrypted']}")

    # Visualize character frequencies
    visualize_character_frequencies(data)

if __name__ == "__main__":
    main()
