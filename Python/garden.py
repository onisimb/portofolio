# Forst we must import sapcy and choose the language model
import spacy

nlp = spacy.load('en_core_web_sm')

# Below I have added the garden path sentances togheter
gardenpathSentances = ['Have the students who failed the exam take the supplementary.',
                       'She told me a little white lie will come back to haunt me.']
gardenpathSentances.extend(['Mary gave the child a Band-Aid.', ' That Jill is never here hurts.',
                           ' The cotton clothing is made of grows in Mississippi.'])

# to work around the error i received, I created a new variable joining the list of sentances for the nlp function (tokenise)
joined_gardenpathSentances = ' '.join(gardenpathSentances)
doc = nlp(joined_gardenpathSentances)
print([token.orth_ for token in doc])

# Below block of code will be for named entity recognition
print([(i, i.label_, i.label) for i in doc.ents])

# Spacy explain categories allocated to sentances code
spacy_explain_categories = spacy.explain("GPE")
print(f"The category allocated means: {spacy_explain_categories}")
spacy_explain_categories = spacy.explain("PERSON")
print(f"The category allocated means: {spacy_explain_categories}")


# Comments about entities
''' The first entity I looked at was 'GPE' allocated by spacy to the word Mississippi. The exlanation given was "Countries, cities, states". 
The explanation makes sense as Mississippi is a state in Southeastern region of the United States.
    The second entity was 'PERSON' allocated correctly to Mary. The xaplnation was "People, including fictional" and again it 
makes sense in terms of wrod association as Mary is the name of a woman/girsl.'''

# Reference:
# 1 - https://www.apartmenttherapy.com/garden-sentences-262915
# 2 - PDF and python file provided with the task by HyperionDev.
