from fuzzywuzzy import fuzz, process

Str1 = "Apple Inc."
Str2 = "apple Inc"
Ratio = fuzz.ratio(Str1.lower(), Str2.lower())
print(Ratio)  # Result 95


Str1 = "Los Angeles Lakers"
Str2 = "Lakers"
Ratio = fuzz.ratio(Str1.lower(), Str2.lower())
Partial_Ratio = fuzz.partial_ratio(Str1.lower(), Str2.lower())
print(Ratio)  # Result 50
print(Partial_Ratio)  # Result 100


# strings comparison the same, but they are in a different order
Str1 = "united states v. nixon"
Str2 = "Nixon v. United States"
Ratio = fuzz.ratio(Str1.lower(), Str2.lower())
Partial_Ratio = fuzz.partial_ratio(Str1.lower(), Str2.lower())
Token_Sort_Ratio = fuzz.token_sort_ratio(Str1, Str2)
print(Ratio)  # Result 59
print(Partial_Ratio)  # Result 74
print(Token_Sort_Ratio)  # Result 100


# these two strings are of widely differing lengths
Str1 = "The supreme court case of Nixon vs The United States"
Str2 = "Nixon v. United States"
Ratio = fuzz.ratio(Str1.lower(), Str2.lower())
Partial_Ratio = fuzz.partial_ratio(Str1.lower(), Str2.lower())
Token_Sort_Ratio = fuzz.token_sort_ratio(Str1, Str2)
Token_Set_Ratio = fuzz.token_set_ratio(Str1, Str2)
print(Ratio)
print(Partial_Ratio)
print(Token_Sort_Ratio)
print(Token_Set_Ratio)

# get the string with the highest score
str2Match = "apple inc"
strOptions = ["Apple Inc.", "apple park", "apple incorporated", "iphone"]
Ratios = process.extract(str2Match, strOptions)
print(Ratios)
# You can also select the string with the highest matching percentage
highest = process.extractOne(str2Match, strOptions)
# highest two
process.extract(str2Match, strOptions, limit=2)
print(highest)
# [('Apple Inc.', 100), ('apple incorporated', 90), ('apple park', 67), ('iphone', 30)]
# ('Apple Inc.', 100)
