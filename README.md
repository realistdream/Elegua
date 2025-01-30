# Elegua

*Overview*

Elegua.py is a Python script designed to analyze strings for patterns, randomness, and potential encryption. The script uses Shannon entropy to assess randomness, checks for repeating patterns, and performs encryption-specific tests, including detection of ECB mode encryption through repetition and a Chi-Square test.

*Features*

 - Entropy Calculation: Computes the Shannon entropy of a given string to assess its randomness.
 - Pattern Detection: Identifies and reports repeating patterns or structures within a string.
 - Block Entropy Analysis: Calculates entropy for fixed-size blocks within the string to provide insight into its local randomness.
 - Encryption Detection: Utilizes uniformity scoring, ECB detection (repeating blocks), and Chi-Square testing to evaluate the likelihood of encryption.
 - Character Frequency Visualization: Plots a bar chart showing the frequency distribution of characters in the  string.

*Usage*

 - Step 1 - User Input: The script begins by prompting the user to input a string for analysis.
 - Step 2 - Pattern Analysis: Checks for repeating patterns within the input string.
 - Step 3 - Entropy Analysis: Computes the overall entropy and block-wise entropies, calculates the normalized entropy, and assesses the randomness.
 - Step 4 - Encryption Checks: Performs encryption pattern checks including uniformity scoring and Chi-Square test.
 - Step 5 - Visualization: Displays a bar chart of character frequencies.

To run the script, execute python Elegua.py from the command line and follow the prompts.

*Dependencies*

 - math: For mathematical operations including logarithms.
 - collections.Counter: Used to count the frequency of characters in the string.
 - matplotlib.pyplot: To plot the character frequency distribution.
 - scipy.stats.chisquare: For performing the Chi-Square statistical test.

Ensure that all necessary libraries are installed. You can install matplotlib and scipy using pip:

> bash pip install matplotlib scipy

Example:

Run the script and provide input when prompted:

Enter a string to analyze: ExampleData123! Enter block size for entropy analysis: 4

The script will output:

 - Shannon entropy values.
 - Results of pattern detection.
 - Encryption likelihood based on entropy and Chi-Square test results.
 - A visual plot of character frequencies.

*Conclusion*

Elegua.py is a comprehensive tool that combines multiple analytical techniques to offer insights into the structure and potential encryption of text data. It is suitable for use in fields where statistical analysis of text is necessary, such as cybersecurity and data encryption analysis.
