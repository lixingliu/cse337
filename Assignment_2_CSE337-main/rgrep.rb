#!/usr/bin/env ruby
# args = ARGF.argv
$COUNT_OPTION = false
$MATCH_OPTION = false

def option_helper_function(args)
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

end


args = ARGV
if args.length() <= 1
    print("Missing required arguments")
else
    filename = args[0]
    args.shift
    valid_start_options = ['-w', '-p', '-v']
    if valid_start_options.include? args[0]
        puts('valid')
    else
        puts("wtf am i looking at")
        return
    end
    while !args.empty?
        case args[0]
            when '-w' #the next arg should be a pattern
                args.shift #pop -w
                option_helper_function(args) #check if the next arg is a -c or -m and set the global variables
                pattern = args[0]   #next word should be the pattern
                args.shift #pop the pattern
                if !$MATCH_OPTION and !$COUNT_OPTION
                    result = []
                    IO.foreach(filename) {|line| result.push(line[..-2]) if line.split().include? pattern }
                    print result
                elsif $COUNT_OPTION
                    count = 0
                    IO.foreach(filename) {|line| count = count + 1 if line.split().include? pattern }
                    print count
                elsif $MATCH_OPTION
                    result = []
                    IO.foreach(filename) {|line| result.push(pattern) if line.split().include? pattern }
                    puts result

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

