word = input("Word: ")
frame_width = 30

word_length = len(word)
spaces_needed = frame_width - word_length - 2  

left_spaces = spaces_needed // 2
right_spaces = spaces_needed - left_spaces  

print('*' * frame_width)

print('*' + ' ' * left_spaces + word + ' ' * right_spaces + '*')

print('*' * frame_width)
 