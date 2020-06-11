# Read from the file words.txt and output the word frequency list to stdout.
for i in `seq \`head -n1 file.txt | wc -w\``; do awk -v c=$i '{print $c}' file.txt | tr '\n' ' ' | awk '{$1=$1};1';   done
