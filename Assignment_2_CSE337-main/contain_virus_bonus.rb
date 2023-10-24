require 'set'
class Region
    attr_accessor :infected, :uninfected, :walls
    
    def initialize
        @infected = Set.new
        @uninfected = Set.new
        @walls = 0
    end
end

def add_soon_to_be_infected(regions, matrix, row, col)
    if matrix[row][col] == 1 || matrix[row][col] == -1
        return
    end
    if row - 1 >= 0 and matrix[row-1][col] == 1
        region = find_infected_region(regions, matrix, row-1, col)
        region.uninfected.add([row, col])
    end
    if col + 1 < matrix[0].length() and matrix[row][col+1] == 1
        region = find_infected_region(regions, matrix, row, col+1)
        region.uninfected.add([row, col])
    end
    if row + 1 < matrix.length() and matrix[row+1][col] == 1
        region = find_infected_region(regions, matrix, row+1, col)
        region.uninfected.add([row, col])
    end
    if col - 1 >= 0 and matrix[row][col-1] == 1
        region = find_infected_region(regions, matrix, row, col-1)
        region.uninfected.add([row, col])
    end
end

def find_infected_region(regions, matrix, row, col)
    for region in regions
        if region.infected.empty?
            return region
        end
        if region.infected.include?([row, col])
            return region
        end
    end
    region = Region.new
    regions.append(region)
    return region
end
def find_existing_regions(regions, matrix, row, col)
    for region in regions
        if region.infected.empty?
            return region
        end
        if region.infected.include?([row - 1, col])
            return region
        elsif region.infected.include?([row, col + 1])
            return region
        elsif region.infected.include?([row + 1, col])
            return region
        elsif region.infected.include?([row, col - 1])
            return region
        end
    end
    region = Region.new
    regions.append(region)
    return region
end

def create_regions(regions, matrix, row, col)
    if matrix[row][col] == 1
        region = find_existing_regions(regions, matrix, row, col)
        region.infected.add([row, col])
    end
end

def dangerous_region(regions)
    risky_region = regions[0]
    region_risk_level = 0
    for region in regions
        if region.uninfected.length() > region_risk_level
            risky_region = region
            region_risk_level = region.uninfected.length()
        end
    end
    return risky_region
end

def region_add_walls(region, matrix)
    for item in region.infected
        if item[0] - 1 >= 0 and matrix[item[0] - 1][item[1]] == 0
            region.walls = region.walls + 1
        end
        if item[0] + 1 < matrix.length() and matrix[item[0] + 1][item[1]] == 0
            region.walls = region.walls + 1 
        end
        if item[1] - 1 >= 0 and matrix[item[0]][item[1] - 1] == 0
            region.walls = region.walls + 1 
        end
        if item[1] + 1 < matrix[0].length() and matrix[item[0]][item[1] + 1] == 0
            region.walls = region.walls + 1 
        end
    end
    return region.walls
end

def fix_regions(regions)
    old_count = regions.length()
    new_count = 0
    loop do 
        old_count = new_count
        for i in 0..(regions.length()-1)
            for j in (i+1)..(regions.length()-1)
                for item in regions[i].infected
                    if regions[j].infected.include?([item[0]-1, item[1]])
                        regions[i].infected = regions[i].infected + regions[j].infected
                        regions[j].infected = Set.new
                    end
                    if regions[j].infected.include?([item[0]+1, item[1]])
                        regions[i].infected = regions[i].infected + regions[j].infected
                        regions[j].infected = Set.new
                    end
                    if regions[j].infected.include?([item[0], item[1]-1])
                        regions[i].infected = regions[i].infected + regions[j].infected
                        regions[j].infected = Set.new
                    end
                    if regions[j].infected.include?([item[0], item[1]+1])
                        regions[i].infected = regions[i].infected + regions[j].infected
                        regions[j].infected = Set.new
                    end
                end
            end
        end
        temp_count = regions.length() - 1
        while temp_count >= 0
            regions.delete(regions[temp_count]) if regions[temp_count].infected.empty?
            temp_count = temp_count - 1
        end
        new_count = regions.length()
    break if old_count == new_count
    end
end
def contain_virus_bonus(is_infected)
    walls = 0
    while true
        regions = []
        (0..(is_infected.length()-1)).each do |i|
            (0..(is_infected[0].length()-1)).each do |j|
                if is_infected[i][j] == 1
                    if regions.empty?
                        regions.append(Region.new)
                    end
                    create_regions(regions, is_infected, i, j)
                end
            end
        end
        fix_regions(regions)        
        if regions.empty?
            return walls
        end
        (0..(is_infected.length()-1)).each do |i|
            (0..(is_infected[0].length()-1)).each do |j|
                add_soon_to_be_infected(regions, is_infected, i, j)
            end
        end
        region = dangerous_region(regions)
        walls = walls + region_add_walls(region, is_infected)
        for item in region.infected
            is_infected[item[0]][item[1]] = -1
        end
        regions.delete(region)
        for region in regions
            region.infected = region.infected + region.uninfected
            for item in region.uninfected
                is_infected[item[0]][item[1]] = 1
            end
            region.uninfected = Set.new
        end
        if regions.empty?
            break
        end
    end
    return walls
end

# Example input, where 1 represents infected cells and 0 represents uninfected cells:
# isInfected = [
#   [0, 1, 0, 0, 1],
#   [0, 1, 0, 0, 1],
#   [0, 0, 0, 0, 1]
# ]

isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]

# Call the function and store the result in a variable
result = contain_virus_bonus(isInfected)

# Print the result
puts "Number of walls needed: #{result}"