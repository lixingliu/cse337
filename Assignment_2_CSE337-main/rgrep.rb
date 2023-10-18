#!/usr/bin/env ruby
# args = ARGF.argv
args = ARGV
if args.length() <= 1
    print("Missing required arguments")
else
    args.shift
    while !args.empty?
        case args[0]
            when '-w' #the next arg should be a pattern
                args.shift #pop -w
                count_option = false
                match_option = false
                if args[0] == '-c'
                    count_option = true
                    args.shift  #pop the count option
                end
                if args[0] == '-m'
                    match_option = true
                    args.shift  #pop the match option
                end
                if count_option && match_option
                    print("cannot have both -c and -m")
                    return
                end
                pattern = args[0]
                args.shift #pop the pattern
                if !match_option and !count_option
                    result = []
                    IO.foreach("test.txt") {|line| result.push(line[..-2]) if line.split().include? pattern }
                    print result
                    return result
                elsif count_option
                    count = 0
                    IO.foreach("test.txt") {|line| count = count + 1 if line.split().include? pattern }
                    print count
                    return count
                elsif match_option
                    result = []
                    IO.foreach("test.txt") {|line| result.push(pattern) if line.split().include? pattern }
                    puts result
                    return result

                end
            when '-p'
                args.shift #pop -w
                count_option = false
                match_option = false
                if args[0] == '-c'
                    count_option = true
                    args.shift  #pop the count option
                end
                if args[0] == '-m'
                    match_option = true
                    args.shift  #pop the match option
                end
                if count_option && match_option
                    print("cannot have both -c and -m")
                    return
                end
                pattern = args[0]
                args.shift #pop the pattern
                if !match_option and !count_option
                    print(pattern)
                end
        end
    end
end

