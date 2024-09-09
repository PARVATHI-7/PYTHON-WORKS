# given two strings
# Source_word="CHICKEN"
# Target_word="HEN"
# write a program to print word is kangaroo or not

source_word= "chicken" 
target_word = "hen" 
word_count= {}
for ch in source_word:
    is_kangaroo_word = True
for ch in target_word:
    if ch in word_count and word_count.get (ch)>0: 
        word_count[ch]-=1
    else:
        is_kangaroo_word = False
        break
print(is_kangaroo_word)

