#!/usr/bin/env ruby
# A regular expression that matches ten digit numbers
# like a phone number.

puts ARGV[0].scan(/^[0-9]{10}$/).join
