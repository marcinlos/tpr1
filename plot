
set terminal png size 900,900 

set xlabel "Msg size (B)"

set title "Average"
set output 'time.png'
set ylabel "Delay (ms)"

plot 'std.dat' using 1:3 with lines title "Standard", \
     'sync.dat' using 1:3 with lines title "Synchronized"

set title "Throughput"
set output 'throughput.png'
set ylabel "Throughput (KB/s)"
plot 'std.dat' using 1:4 with lines title "Standard", \
     'sync.dat' using 1:4 with lines title "Synchronized" 
