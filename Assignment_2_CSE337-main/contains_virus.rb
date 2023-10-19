def contains_virus(grid)
    row = grid.length() - 1
    col = grid[0].length() - 1  
    wall_count = 0
    for i in 0..row
        for j in 0..col
            if grid[i][j] == 1 #if the region is infected
                wall_count = wall_count + 1 if (i-1 < 0 or grid[i-1][j] == 0)
                wall_count = wall_count + 1 if (j+1 > col or grid[i][j+1] == 0)
                wall_count = wall_count + 1 if (i+1 > row or grid[i+1][j] == 0)
                wall_count = wall_count + 1 if (j-1 < 0 or grid[i][j-1] == 0)
            end
        end
    end
    return(wall_count)
end
puts("test 1")
isInfected = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]] 
result = contains_virus(isInfected)
puts "Number of walls needed: #{result}"    #16

puts("test 2")
isInfected = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]] 
result = contains_virus(isInfected)
puts "Number of walls needed: #{result}"    #16

puts("test 3")
isInfected = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] 
result = contains_virus(isInfected)
puts "Number of walls needed: #{result}"    #0

puts("test 4")
isInfected = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] 
result = contains_virus(isInfected)
puts "Number of walls needed: #{result}"    #0

puts("test 5")
isInfected = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]] 
result = contains_virus(isInfected)
puts "Number of walls needed: #{result}"    #8

puts("test 6")
isInfected = [[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]] 
result = contains_virus(isInfected)
puts "Number of walls needed: #{result}"    #24

puts("test 7")
isInfected = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]] 
result = contains_virus(isInfected)
puts "Number of walls needed: #{result}"    #16

puts("test 8")
isInfected = [[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]] 
result = contains_virus(isInfected)
puts "Number of walls needed: #{result}"    #14

puts("test 9")
isInfected = [[1]] 
result = contains_virus(isInfected)
puts "Number of walls needed: #{result}"    #4

puts("test 10")
isInfected = [[0]] 
result = contains_virus(isInfected)
puts "Number of walls needed: #{result}"    #0

puts("test 11")
isInfected = [[1], [1]] 
result = contains_virus(isInfected)
puts "Number of walls needed: #{result}"    #6

puts("test 12")
isInfected = [[1], [0]] 
result = contains_virus(isInfected)
puts "Number of walls needed: #{result}"    #4

puts("test 13")
isInfected = [[1], [1], [1]] 
result = contains_virus(isInfected)
puts "Number of walls needed: #{result}"    #8

puts("test 14")
isInfected = [[1, 0], [1, 0], [1, 0]] 
result = contains_virus(isInfected)
puts "Number of walls needed: #{result}"    #8

puts("test 15")
isInfected = [[1, 0, 0], [1, 0, 0], [1, 0, 0]] 
result = contains_virus(isInfected)
puts "Number of walls needed: #{result}"    #8

# puts("test 16")
# isInfected = [[1, 0, 1], [1, 0, 1], [1, 0, 1]] 
# result = contains_virus(isInfected)
# puts "Number of walls needed: #{result}"    #18

puts("test 17")
isInfected = [[0, 1, 0], [0, 1, 0], [0, 1, 0]] 
result = contains_virus(isInfected)
puts "Number of walls needed: #{result}"    #8