# baby

Python Regular Expressions (Regex) Search Methods
This repository provides a collection of Python functions for performing various types of regular expression (regex) searches. The functions allow you to search, find, extract, substitute, and manipulate strings using regular expressions in a flexible way. Each function is self-contained and provides a specific regex operation to handle different search and pattern matching tasks.

Table of Contents
Requirements
Functions
basic_search
find_all_occurrences
match_search
find_all_matches
split_by_pattern
full_match_search
extract_groups
search_with_position
substitute_pattern
case_insensitive_search
optional_pattern_search
Usage
Requirements
Python 3.x or higher
re module (comes built-in with Python)
Functions
1. basic_search(text, pattern)
Search for the first occurrence of a pattern in the given text.

Args:

text (str): The string in which to search for the pattern.
pattern (str): The pattern to search for.
Returns:

str: The matched pattern, or "No match found" if no match is found.
2. find_all_occurrences(text, pattern)
Find all occurrences of a pattern in the given text.

Args:

text (str): The string in which to find the occurrences of the pattern.
pattern (str): The pattern to search for.
Returns:

list: A list of all matches found.
3. match_search(text, pattern)
Check if the pattern matches at the start of the string.

Args:

text (str): The string to check for the pattern.
pattern (str): The pattern to match at the start of the string.
Returns:

str: The matched string, or "No match at the start" if the pattern doesn't match at the start.
4. find_all_matches(text, pattern)
Find all non-overlapping matches of a pattern in the given text.

Args:

text (str): The string to search for all matches.
pattern (str): The pattern to search for.
Returns:

list: A list of all match groups found.
5. split_by_pattern(text, pattern)
Split the text by occurrences of the pattern.

Args:

text (str): The string to split.
pattern (str): The pattern by which to split the string.
Returns:

list: A list of strings resulting from the split.
6. full_match_search(text, pattern)
Check if the entire string matches the pattern.

Args:

text (str): The string to check for a full match.
pattern (str): The pattern to match against the entire string.
Returns:

str: The matched string, or "No full match" if the entire string does not match the pattern.
7. extract_groups(text, pattern)
Extract captured groups from the text using the given pattern.

Args:

text (str): The string to extract groups from.
pattern (str): The pattern with capture groups to extract.
Returns:

tuple: A tuple of captured groups, or "No match" if no match is found.
8. search_with_position(text, pattern)
Search for a pattern and return its position in the string.

Args:

text (str): The string to search for the pattern.
pattern (str): The pattern to search for.
Returns:

tuple: A tuple containing the start and end position of the match, or "No match" if no match is found.
9. substitute_pattern(text, pattern, replacement)
Substitute the occurrences of a pattern with a replacement string.

Args:

text (str): The string in which to substitute the pattern.
pattern (str): The pattern to find.
replacement (str): The string to replace the pattern with.
Returns:

str: The modified string with the pattern replaced by the replacement.
10. case_insensitive_search(text, pattern)
Perform a case-insensitive search for a pattern in the text.

Args:

text (str): The string in which to search for the pattern.
pattern (str): The pattern to search for.
Returns:

str: The matched pattern, or "No match found" if no match is found.
11. optional_pattern_search(text, pattern)
Search for an optional pattern in the string.

Args:

text (str): The string to search for the pattern.
pattern (str): The pattern with optional parts to search for.
Returns:

str: The matched pattern, or "No match found" if no match is found.