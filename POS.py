import nltk
from nltk.corpus import brown

# Training the POS tagger using the Brown Corpus
tagged_sentences = brown.tagged_sents(categories='news')
train_data = [[(word, tag) for word, tag in sentence] for sentence in tagged_sentences]  # Ensure each element is a list of (word, tag) pairs
tagger = nltk.HiddenMarkovModelTagger.train(train_data)

# Define the Viterbi algorithm for POS tagging
def viterbi_pos_tag(sentence, tagger):
    return tagger.tag(sentence)

# Example sentence
sentence = ['The', 'cat', 'runs.']

# Use the Viterbi algorithm to predict POS tags
predicted_tags = viterbi_pos_tag(sentence, tagger)

print(predicted_tags)
