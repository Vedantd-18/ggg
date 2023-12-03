import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Example sentence
sentence = "The cat runs."

# Process the sentence with spaCy
doc = nlp(sentence)

# Extract part-of-speech tags
predicted_tags = [(token.text, token.pos_) for token in doc]

print(predicted_tags)
