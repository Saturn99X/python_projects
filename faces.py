# store the prompt in a variable
variable = input('type your text here, know those emoticons :) and :( shall get converted into emoji ')
#emoji variables
slightly_smiley_face = '🙂'
slightly_frowning_face = '🙁'
# converting
new_variable = variable.replace(':)', slightly_smiley_face).replace(':(', slightly_frowning_face)

print(new_variable)



