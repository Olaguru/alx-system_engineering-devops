#!/usr/bin/env ruby
# done by crypto tech coder 

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
