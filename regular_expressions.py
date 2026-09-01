##regular expressions:
import re
pattern = r"[A-Z]+Well"
text ='''Well being is what is non-instrumentally good for a person. Also called welfare and quality of life, it is a measure of how well life is going for someone. In the broadest sense, it covers the balance of all positive and negative aspects of a person's life. More narrowly, it refers only to positive degrees and contrasts with ill-being, which denotes negative ones. In this sense, well-being is what egoists typically seek for themselves and altruists aim to enhance in others, serving as a central goal of many individual and societal endeavors.
Researchers discuss different types of well-being by how they are measured, who they belong to, and which domain of life they affect. Subjective well-being refers to how a person feels about and evaluates their life. Objective well-being encompasses factors that can be assessed from an external perspective, such as health, income, and security. Individual well-being concerns the quality of life of a particular person, whereas community well-being measures how well a group of people functions and thrives. Forms of well-being belonging to specific domains of life include physical, psychological, emotional, social, and economic well-being.
Theories of well-being aim to identify its essential features. Hedonism argues that well-being ultimately depends on the balance of pleasure over pain. Desire theories hold that the satisfaction of desires is the source of well-being. Objective list theories assert that a combination of diverse elements is responsible for well-being. Often-discussed contributing factors include feelings, emotions, life satisfaction, achievement, finding a sense of meaning, interpersonal relationships, and health.
'''
#match = re.search(pattern, text)
#print(match)
matches = re.finditer(pattern, text)
for match in matches:
    print(match.span())
    print(text[match.span()[0],match.span()[1]])
