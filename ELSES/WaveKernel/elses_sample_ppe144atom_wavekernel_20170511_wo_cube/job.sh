#!/bin/bash
#------ qsub option -------- 
#QSUB -q gr10080b
#QSUB -ug gr10080
#QSUB -M irhn1058@gmail.com
#QSUB -m be
#QSUB -W 10:00
#QSUB -o ppe144atom_jobinfo.txt
#QSUB -e ppe144atom_err.txt
#QSUB -A p=4:t=8:c=8
~/ms/ELSES/bin/elses -verbose config.xml > log.txt
