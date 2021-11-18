#!/usr/bin/env perl
use strict;
use warnings;
use POSIX qw/strftime/;

my @words = qw/alpha bravo charlie delta echo foxtrot golf hotel india juliet kilo lima mike november oscar papa quebec romeo sierra tango unifrom viktor whiskey x-ray yankee zulu/;

sub random_word {
    $words[int(rand(scalar @words))];
}

for my $file (1..10) {
    open my $fh, ">", "logs/$file.log" or die "open: $!";
    my $time = time;
    for my $line (1..100) {
        print $fh strftime("%Y%m%d%H%M%S ", localtime($time));
        print $fh join(" ", map { random_word() } 1..10);
        print $fh "\n";
        $time += int(rand(10000));
    }
}
