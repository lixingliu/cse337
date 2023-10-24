#!/usr/bin/env ruby
# args = ARGF.argv

$P_OPTION = false
$W_OPTION = false
$C_OPTION = false
$M_OPTION = false
$PATTERN = ''
def initial_check(args)
    valid_options = ['-w', '-p', '-v', '-c', '-m']

    if args.empty?
        return "Missing required arguments"
    end

    if !args[0].include?(".txt")
        return "Missing required arguments"
    end

    if args.any? { |arg| arg.start_with?('-') and !valid_options.include?(arg) }
        return "Invalid option"
    end

    return nil
end

def rgrep()
    args = ARGV
    option_counter = 0
    initial_result = initial_check(args) 
    if initial_result != nil
        return initial_result
    end
    filename = args[0]
    args.shift()
    input_options = []
    while !args.empty? and option_counter <= 2
        case args[0]
            when '-w'
                if $W_OPTION
                    return "Invalid combination of options"
                end
                option_counter = option_counter + 1
                $W_OPTION = true
                input_options.append(args[0])
                args.shift()
            when '-p'
                if $P_OPTION
                    return "Invalid combination of options"
                end
                option_counter = option_counter + 1
                $P_OPTION = true
                input_options.append(args[0])
                args.shift()
            when '-v'
                option_counter = option_counter + 1
                print('v')
                args.shift()
            when '-c'
                option_counter = option_counter + 1
                $C_OPTION = true
                input_options.append(args[0])
                args.shift()
            when '-m'
                option_counter = option_counter + 1
                $M_OPTION = true
                input_options.append(args[0])
                args.shift()
            else
#need to deal with -w -p                    
                if input_options.include?('-w') or input_options.include?('-p')
                    $PATTERN = args[0]
                    args.shift()
                    break
                else
                    return "Invalid combination of options"
                end
                args.shift()

        end
    end

    if !args.empty?
        return "Invalid combination of options"
    end
    print(input_options)
    puts
    #confused about the default thing
    # if args.none? { |arg| arg.start_with?('-')}
    #     P_OPTION = true
    # end

    #lets start with reading -w
    # if we read -w, next one can be a -c or -m or a pattern
    # if we read a -c next one has to be a -c or a -p or a -v
    # -w pattern
    # -w -c pattern
    # -c -w pattern
    if $P_OPTION and $M_OPTION
        result = []
        IO.foreach(filename) {|line| result.push(line.match(/#{$PATTERN}/)) }
        # puts result
        return result
    end
    if $P_OPTION and $C_OPTION
        count = 0
        IO.foreach(filename) {|line| count = count + 1 if line.match(/#{$PATTERN}/) }
        # print count
        return count
    end
    if $P_OPTION
        result = []
        IO.foreach(filename) {|line| result.push(line) if line.match(/#{$PATTERN}/)}
        return result
    end
    if $W_OPTION and $M_OPTION
        result = []
        IO.foreach(filename) {|line| result.push($PATTERN) if line.split().include? $PATTERN }
        # puts result
        return result
    end
    if $W_OPTION and $C_OPTION
        count = 0
        IO.foreach(filename) {|line| count = count + 1 if line.split().include? $PATTERN }
        # print count
        return count
    end
    if $W_OPTION
        result = []
        IO.foreach(filename) {|line| result.push(line[..-2]) if line.split().include? $PATTERN }
        # print result
        return result 
    end  



    # need to check for missing pattern 
    # need to check for invalid combination of options


end

puts(rgrep())