class Array
    alias original_index []
    alias original_map map
    def [](index)
        if (index < self.length() and index >= (0 - self.length()))
            return self.original_index(index)
        else
            return '\0'
        end
    end

    def map(range = nil, &block)#DOUBLE CHECK WHAT INVALID RANGE IS
        if range == nil
            return self.original_map(&block)
        else
            result = []
            for i in range do
                if self[i] != '\0'
                    result.push(yield self[i])
                end
            end
            return result
        end
    end
end
  
a = [1,2,34,5]
b = ["cat","bat","mat","sat"]
# puts(b[-10], b[-9], b[-8], b[-7], b[-6], b[-5], b[-4], b[-3], b[-2], b[-1], b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[9], b[10])
print b.map(-10..10) { |x| x[0].upcase + x[1,x.length] }, "\n"
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