digits={
    '0': ('###', '# #', '# #', '# #', '###'),
    '1': ('  #', '  #', '  #', '  #', '  #'),
    '2': ('###', '  #', '###', '#  ', '###'),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###')
}

number=int(input("Enter Only Number (0-9)\n"))
number=str(number)
def printSevenSegmentDisplay(number):
    for i in range(5):
        for j in number:
            
            print(digits[j][i],end=" ")
            
        print("\n")
    return 'Done Printing Seven Segment Display of',number
print(printSevenSegmentDisplay(number))

