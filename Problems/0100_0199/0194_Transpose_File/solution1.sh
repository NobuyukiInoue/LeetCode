for ((i=1; i<=$(head -n 1 file.txt | wc -w);i++)){
 echo $(cut -d ' ' -f $i file.txt)
}
