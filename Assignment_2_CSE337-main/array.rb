class Array
    alias original_index [] #use alias to represent the original []
    alias original_map map  #use alias to represent the original map

    def [](index = nil, index2 = nil)   #override the original []
        if index == nil and index2 == nil   #if there are no indexes
            return "wrong number of arguments (given 0, expected 1..2)"
        end
        if index != nil and index2 != nil   #if there are 2 indexes
            return self.original_index(index, index2)   #perform the original [] with 2 index
        end
        if index.is_a?(Range)   #if the input is a range
            result = []
            for i in index
                if self.original_index(i).nil?
                    result.append('\0')
                end
                puts(result)
            end
            return self.original_index(index)
        end
        if (index < self.length() and index >= (0 - self.length())) #if the index is greater than the negative range and less than the max index
            return self.original_index(index)   #perform the original [] with 1 index
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
  
# a = [1,2,34,5]
# b = ["cat","bat","mat","sat"]
# c = [1, 2]
# puts c[2..10]
# puts b[]
# puts b[1]
# puts b[0,4]
# puts b[0..4]
# puts(b[-10], b[-9], b[-8], b[-7], b[-6], b[-5], b[-4], b[-3], b[-2], b[-1], b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[9], b[10])
# print b.map(-10..10) { |x| x[0].upcase + x[1,x.length] }, "\n"
# print b.map(2..4) { |x| x[0].upcase + x[1,x.length] }, "\n"
# print b.map { |x| x[0].upcase + x[1,x.length] }, "\n"
# print b.map(2..10) { |x| x[0].upcase + x[1,x.length] }, "\n"
# puts a[1]
# puts a[10]

# print a.map(4..-2) { |i| i.to_f}, "\n"
# print a.map(2..4) { |i| i.to_f}, "\n"
# print a.map(1..-3) {|i| i.to_f}, "\n"
# print a.map { |i| i.to_f}, "\n"
# puts b[-1]
# puts b[5]
# print b.map(2..10) { |x| x[0].upcase + x[1,x.length] }, "\n"
# print b.map(2..4) { |x| x[0].upcase + x[1,x.length] }, "\n"
# print b.map(-3..-1) { |x| x[0].upcase + x[1,x.length] }, "\n"
# print b.map { |x| x[0].upcase + x[1,x.length] }, "\n"

# a = [1,2,34,5]
# b = ["cat","bat","mat","sat"]
# puts(b[-10], b[-9], b[-8], b[-7], b[-6], b[-5], b[-4], b[-3], b[-2], b[-1], b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[9], b[10])
# print b.map(-10..10) { |x| x[0].upcase + x[1,x.length] }, "\n"
# print b.map(2..4) { |x| x[0].upcase + x[1,x.length] }, "\n"
# print b.map { |x| x[0].upcase + x[1,x.length] }, "\n"
# print b.map(2..10) { |x| x[0].upcase + x[1,x.length] }, "\n"
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

# a = [nil, nil, 1, nil, 2]
# print a[1], "\n"
# result5 = a.map(0..4) { |x| x.to_s }
# print result5, "\n"


# a = [1, 2]
# p a[2..10], "\n"


# b = ["cat","bat","mat","sat"]
# p b[2..10]
# p b[2]
# p b[5]
# p b[5..10]

# a = [1,2,34,5]
# b = ["cat","bat","mat","sat"]
# puts(b[-10], b[-9], b[-8], b[-7], b[-6], b[-5], b[-4], b[-3], b[-2], b[-1], b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[9], b[10])
# print b.map(-10..10) { |x| x[0].upcase + x[1,x.length] }, "\n"
# print b.map(2..4) { |x| x[0].upcase + x[1,x.length] }, "\n"
# print b.map { |x| x[0].upcase + x[1,x.length] }, "\n"
# print b.map(2..10) { |x| x[0].upcase + x[1,x.length] }, "\n"
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

# a = [nil, nil, 1, nil, 2]
# print a[1], "\n"
# result5 = a.map(0..4) { |x| x.to_s }
# print result5, "\n"


# a = [1, 2]
# p a[2..10], "\n"


# b = ["cat","bat","mat","sat"]
# p b[2..10]
# p b[2]
# p b[5]
# p b[5..10]


# def assert_equal(expected, actual, message = nil)
#   if expected != actual
#     fail_message = message || "Expected #{expected.inspect}, but got #{actual.inspect}."
#     raise fail_message
#   else
#     puts "Passed: #{message}"
#   end
# end

# a = [1, 2, 34, 5]
# assert_equal(1, a[0], "in-bounds positive index: a[0]")
# assert_equal(2, a[1], "in-bounds positive index: a[1]")
# assert_equal(5, a[-1], "in-bounds negative index: a[-1]")
# assert_equal(34, a[-2], "in-bounds negative index: a[-2]")
# assert_equal('\0', a[5], "out-of-bounds positive index: a[5]")
# assert_equal('\0', a[-6], "out-of-bounds negative index: a[-6]")

# b = ["cat", "bat", "mat", "sat"]
# result = b.map { |x| x[0].upcase + x[1,x.length] }
# assert_equal(["Cat", "Bat", "Mat", "Sat"], result, "default map behavior")

# result = b.map(2..3) { |x| x[0].upcase + x[1,x.length] }
# assert_equal(["Mat", "Sat"], result, "in-bounds sequence: (2..3)")

# result = b.map(2..10) { |x| x[0].upcase + x[1,x.length] }
# assert_equal(["Mat", "Sat"], result, "sequence with out-of-bounds indices: (2..10)")

# result = b.map(5..10) { |x| x[0].upcase + x[1,x.length] }
# assert_equal([], result, "completely out-of-bounds sequence: (5..10)")

# result = b.map(-3..-1) { |x| x[0].upcase + x[1,x.length] }
# assert_equal(["Bat", "Mat", "Sat"], result, "negative in-bounds sequence: (-3..-1)")

# result = b.map(-10..-1) { |x| x[0].upcase + x[1,x.length] }
# assert_equal(["Cat", "Bat", "Mat", "Sat"], result, "sequence with both types of negative indices: (-10..-1)")

# c = []
# assert_equal('\0', c[0], "Out-of-bounds index on empty array: c[0]")
# assert_equal('\0', c[-1], "Out-of-bounds negative index on empty array: c[-1]")

# assert_equal(1, a[-0], "Accessing element at -0: a[-0]")
# d = []
# result = d.map { |x| x * 2 }
# assert_equal([], result, "Mapping over empty array without sequence")

# result = d.map(0..2) { |x| x * 2 }
# assert_equal([], result, "Mapping over empty array with sequence")

# result = b.map(-10..-5) { |x| x.upcase }
# assert_equal([], result, "Completely out-of-bounds negative sequence: (-10..-5)")
# seq = [1, 3, 5, -1, -5]
# result = b.map(seq) { |x| x[0].upcase + x[1,x.length] }
# assert_equal(["Bat", "Sat", "Sat"], result, "Mixed sequence of indices: [1, 3, 5, -1, -5]")
# result = b.map([2]) { |x| x.upcase }
# assert_equal(["MAT"], result, "Single-element sequence: [2]")
# result = b.map("not a valid sequence") { |x| x.upcase }
# assert_equal(b.map(&:upcase), result, "Non-Integer and non-Range sequence should default to original behavior")