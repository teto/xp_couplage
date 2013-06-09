
set xlabel "File size (Kbytes)"
set ylabel "Transfer time (s)"

set autoscale

unset mxtics

set terminal png enhanced size 800,600 


set style line 1 lt 1 lw 3 pt 3 lc rgb "red"
set style line 2 lt 3 lw 3 pt 3 lc rgb "red"
set style line 3 lt 1 lw 3 pt 3 lc rgb "blue"
set style line 4 lt 3 lw 3 pt 3 lc rgb "blue"
