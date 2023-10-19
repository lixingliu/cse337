class Array
    alias original_index [] #use alias to represent the original []
    alias original_map map  #use alias to represent the original map

    def [](index)   #override the original []
        if (index < self.length() and index >= (0 - self.length())) #if the index is greater than the negative range and less than the max index
            return self.original_index(index)   #perform the original []
        else
            return '\0' # if the index is invalid, then rethrn \0
        end
    end

    def map(range = nil, &block)    #override the map function, range represents the optional range that the user provides, default is nil, &block represents the 
        if range == nil #if the range doesnt exit, then perform the orignal map method with the block provided originally
            return self.original_map(&block)
        else
            result = [] #create an array called result to return the array after applying the custom map function
            for i in range do   #for every element in the range
                if self[i] != '\0'  #if the element does not equal '\0' that means that the element exit
                    result.push(yield self[i])  #save the element after applying the stuff
                end
            end
            return result
        end
    end
end
  
a = [1,2,34,5]
b = ["cat","bat","mat","sat"]
# puts(b[-10], b[-9], b[-8], b[-7], b[-6], b[-5], b[-4], b[-3], b[-2], b[-1], b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[9], b[10])
# print b.map(-10..10) { |x| x[0].upcase + x[1,x.length] }, "\n"
# print b.map(2..4) { |x| x[0].upcase + x[1,x.length] }, "\n"
print b.map { |x| x[0].upcase + x[1,x.length] }, "\n"
print b.map(2..10) { |x| x[0].upcase + x[1,x.length] }, "\n"
# puts a[1]
# puts a[10]
# print a.map(4..2) { |i| i.to_f}, "\n"
# print a.map(2..4) { |i| i.to_f}, "\n"
# print a.map(1..-3) {|i| i.to_f}, "\n"
# print a.map { |i| i.to_f}, "\n"
# puts b[-1]
# puts b[5]
# print b.map(2..10) { |x| x[0].upcase + x[1,x.length] }, "\n"
# print b.map(2..4) { |x| x[0].upcase + x[1,x.length] }, "\n"
# print b.map(-3..-1) { |x| x[0].upcase + x[1,x.length] }, "\n"
# print b.map { |x| x[0].upcase + x[1,x.length] }, "\n"