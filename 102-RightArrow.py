'''Right arrow'''


def arrow(width, height):
    '''Hehe'''
    for i in range(height):
        if i >= height//2:
            line = ' '*(height-i-1)
        else:
            line = ' '*i
        print(line+'*'*width)


arrow(int(input()), int(input()))
# *******
#  *******
#   *******
#  *******
# *******
#
# *******
#  *******
#   *******
#  *******
# *******
#
# **********
#  **********
#   **********
#    **********
#     **********
#      **********
#     **********
#    **********
#   **********
#  **********
# **********
#
# **********
#  **********
#   **********
#    **********
#     **********
#      **********
#     **********
#    **********
#   **********
#  **********
# **********
