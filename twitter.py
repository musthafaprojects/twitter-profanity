import re

# list of racial slurs
racial_slurs = ['slur1', 'slur2', 'slur3', ...]

# function to calculate profanity score for a tweet
def calculate_profanity(tweet):
    # tokenize tweet into individual words
    words = re.findall(r'\w+', tweet)
    # count number of racial slurs in tweet
    num_slurs = len([w for w in words if w.lower() in racial_slurs])
    # calculate profanity score
    profanity_score = num_slurs / len(words)
    return profanity_score

# example usage
tweet = "This is a racist tweet containing a racial slur."
profanity_score = calculate_profanity(tweet)
print("Profanity score:", profanity_score)

