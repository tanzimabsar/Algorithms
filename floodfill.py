initial_matrix = [
    [0,1,1],
    [0,1,0],
    [1,1,1]
]



def flood_fill(image, i, j, new_colour):

    if image[i][j] == new_colour:
        return

    def fill(image, i, j, colour, new_colour):
        if i < 0 or i > len(image) or j < 0 or j > len(image) or image[i][j] != colour:
            return

        image[i][j] == new_colour

        fill(image, i + 1, j, colour, new_colour) 
        fill(image, i - 1, j, colour, new_colour) 
        fill(image, i, j+1, colour, new_colour) 
        fill(image, i, j-1, colour, new_colour) 

        fill(image, i,j, image[i][j], new_colour)
    
    return image
    
    


print(initial_matrix)

for idx_x, x in enumerate(initial_matrix):
    for idx_y, y in enumerate(x):
        flood_fill(initial_matrix, idx_x,idx_y,0)

print(initial_matrix)