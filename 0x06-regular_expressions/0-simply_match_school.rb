#!/usr/bin/env ruby

# Check if the argument matches the regular expression for "School"
if ARGV.length == 1
  input_string = ARGV[0]
  regex = /School/

  # Use the match method to check if the input string contains the pattern
  match_result = input_string.match(regex)

  # Output the result
  if match_result
    puts "#{match_result[0]}$"
  else
    puts "$"
  end
else
  puts "Usage: #{$PROGRAM_NAME} <input_string>"
end

