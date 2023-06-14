#!/usr/bin/env ruby
# A regular expression that matches the specified cases

puts ARGV[0].scan(/hbt{1,4}n/).join
