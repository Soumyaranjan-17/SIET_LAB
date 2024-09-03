# WAP tp print the following pattern
# * 
# * * 
# * * * 
# * * * * 
# 
#       * 
#     * * 
#   * * * 
# * * * * 

for i in range(1,5):
    for j in range(i):
        print("* ", end="")
    print()

print()
 
for i in range(1,5):
    # print space
    for s in range(5-i-1):
        print("  ", end="")

    for j in range(i):
        print("* ", end="")
    print()
 
#  OUTPUT

# * 
# * * 
# * * * 
# * * * * 
# 
#       * 
#     * * 
#   * * * 
# * * * * 
