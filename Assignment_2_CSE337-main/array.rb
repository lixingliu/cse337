class Array
    alias original_index []
    alias original_map map
    def [](index)
        if (index < self.length() and index >= (0 - self.length()))
            original_index(index)
        else
            return '\0'
        end
    end

    def map(range = nil)
        print(self)
        puts()
        if range == nil
            self.original_map(){yield(self)}
        end
    end
end
  
b = ["cat","bat","mat","sat"]
# puts(b[0]) #cat
# puts(b[1]) #bat
# puts(b[2]) #mat
# puts(b[3]) #sat
# puts(b[-1]) #sat
# puts(b[-2]) #mat
# puts(b[-3]) #bat
# puts(b[-4]) #cat
# puts()
# puts(b[-10], b[-9], b[-8], b[-7], b[-6], b[-5], b[-4], b[-3], b[-2], b[-1], b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[9], b[10])
a = [1,2,34,5]
# puts(a[2])
# puts(a[-2])
# puts(a[5])
# puts(a[-6])

print a.map{|x| x.to_f}
# print b.map(-10..10) { |x| x[0].upcase + x[1,x.length] }, "\n"
  
  