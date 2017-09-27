#!/bin/bash
#PBS -l procs=14
#PBS -l walltime=120:00:00
#PBS -q joe
#PBS -N testat
#PBS -o /nv/hp13/yzhang3027/dev/stdout
#PBS -e /nv/hp13/yzhang3027/dev/stderr

cd /nv/hp13/yzhang3027/dev
source  /gpfs/pace1/project/chbe-medford/medford-share/envs/espresso-5.1.r11289-pybeef_ase3.13_cust_esp


python test.py
