# we will call this on the command line using system perl

use warnings;
use strict;

my $version = $ARGV[0];

die "Cannot determine version" if !$version;

my ($major, $minor, $micro) = split (/\./, $version);

#define LIBZIP_VERSION "1.6.1"
#define LIBZIP_VERSION_MAJOR 1
#define LIBZIP_VERSION_MINOR 6
#define LIBZIP_VERSION_MICRO 1

if (open my $in, '<', 'zipconf.h_template') {
    if (open my $out, '>', 'zipconf.h') {
        while (<$in>) {
            chomp;
            if (m/^#define LIBZIP_VERSION /) {
                print $out qq{#define LIBZIP_VERSION "$version"
};
                next;
            }

            if (m/^#define LIBZIP_VERSION_MAJOR/) {
                print $out qq{#define LIBZIP_VERSION_MAJOR $major
};
                next;
            }

            if (m/^#define LIBZIP_VERSION_MINOR/) {
                print $out qq{#define LIBZIP_VERSION_MINOR $minor
};
                next;
            }

            if (m/^#define LIBZIP_VERSION_MICRO/) {
                print $out qq{#define LIBZIP_VERSION_MICRO $micro
};
                next;
            }

            print $out $_ . "\n";
        }
        close $in;
        close $out;

# for debug
if (open my $inx, '<', 'zipconf.h') {
    while (<$inx>) {
        print $_;
    }
    close $inx;
}
    }
    else {
        die "Cannot open zipconf.h";
    }
}
else {
    die "Cannot open zipconf.h_template";
}

