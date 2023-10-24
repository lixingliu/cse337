#!/usr/bin/env ruby
# args = ARGF.argv

$P_OPTION = false
$W_OPTION = false
$C_OPTION = false
$M_OPTION = false
$V_OPTION = false
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
    if args.length() == 1 and !args[0].start_with?('-')
        $P_OPTION = true
        $PATTERN = args[0]
        args.shift()
    end
    while !args.empty? and option_counter <= 2
        case args[0]
            when '-w'
                if $P_OPTION or $W_OPTION or $V_OPTION
                    return "Invalid combination of options"
                end
                option_counter = option_counter + 1
                $W_OPTION = true
                input_options.append(args[0])
                args.shift()
            when '-p'
                if $P_OPTION or $W_OPTION or $V_OPTION
                    return "Invalid combination of options"
                end
                option_counter = option_counter + 1
                $P_OPTION = true
                input_options.append(args[0])
                args.shift()
            when '-v'
                if $P_OPTION or $W_OPTION or $V_OPTION
                    return "Invalid combination of options"
                end
                option_counter = option_counter + 1
                $V_OPTION = true
                input_options.append(args[0])
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
                if input_options.include?('-w') or input_options.include?('-p') or input_options.include?('-v')
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

    #confused about the default thing
    # if args.none? { |arg| arg.start_with?('-')}
    #     P_OPTION = true
    # end

    if $V_OPTION
        file = []
        result = []
        IO.foreach(filename) {|line| file.push(line)}
        IO.foreach(filename) {|line| result.push(line) if line.match(/#{$PATTERN}/)}
        if $C_OPTION
            return (file - result).length()
        end
        if $M_OPTION
            return "Invalid combination of options" 
        end
        # puts file - result
        return file - result
    end

    if $P_OPTION
        result = []
        IO.foreach(filename) {|line| result.push(line) if line.match(/#{$PATTERN}/)}
        # puts result
        if $C_OPTION
            return result.length()
        end
        if $M_OPTION
            result = []
            IO.foreach(filename) {|line| result.push(line.match(/#{$PATTERN}/)) }
            return result
        end
        return result
    end
    if $W_OPTION
        result = []
        IO.foreach(filename) {|line| result.push(line[..-2]) if line.split().include? $PATTERN }
        if $C_OPTION
            return result.length()
        end
        if $M_OPTION
            return result.map{$PATTERN}
        end
        return result 
    end  



    # need to check for missing pattern 
    # need to check for invalid combination of options

    # if provided just the file with no options rgrep.rb test.txt

end

puts(rgrep())