#!/bin/bash
#QSUB -q gr10080b
#QSUB -ug gr10080
#QSUB -M irhn1058@gmail.com
#QSUB -m be
#QSUB -W 1:00
#QSUB -o benzene_jobinfo.txt
#QSUB -e benzene_err.txt
#QSUB -A p=1:t=4:c=4
# write path and module
module load gaussian09
# execute application
g09 benzene.gjf
formchk benzene.chk
