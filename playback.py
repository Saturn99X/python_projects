# store the sting in a variable
variable = input('write a string that you want to be slowed down: ')
# using the playback function
def playback():
 playback_variable = variable.replace(' ', '...')
 return print(playback_variable)

print ('here is the slowed down version:')
playback()
