def contains_virus(grid)
    row = grid.length() - 1
    col = grid[0].length() - 1  
    for i in 0..row
        for j in 0..col
            print(grid[i][j])
        end
        puts
    end
    return(0)
end

isInfected = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

# Call the function and store the result in a variable
result = contains_virus(isInfected)

# Print the result
puts "Number of walls needed: #{result}"