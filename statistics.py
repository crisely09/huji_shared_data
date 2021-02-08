#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:34:59 2020

@author: nico
"""
import numpy as np
import pandas as pd
import json as js

with open("bla_bins_tot.json", "r") as f:
    bla_bins_tot = [np.array(i) for i in js.load(f)["list"]]
with open("bla_bins_maj.json", "r") as f:
    bla_bins_maj = [np.array(i) for i in js.load(f)["list of arrays"]]
with open("bla_bins_min.json", "r") as f:
    bla_bins_min = [np.array(i) for i in js.load(f)["list of arrays"]]
with open("basins.json", "r") as f:
    d = js.load(f)
    major = np.array(d["major"])
    minor = np.array(d["minor"])
    
isos = pd.read_csv("iso1.csv",index_col=0)
avgisos = pd.read_csv("averaged_iso1.csv",index_col=0)
embs = pd.read_csv("emb1.csv",index_col=0)
min_ = isos["SCF"].min()
isos["dE_GS(eV)"] = 27.2114*(isos["SCF"] - min_)
isos["dE_GS(kcal/mol)"] = 627.5*(isos["SCF"] - min_)
ex_en = isos["ex_en"].values
avgisos["dE_GS(eV)"] = 27.2114*(avgisos["SCF"] - min_)
avgisos["dE_GS(kcal/mol)"] = 627.5*(avgisos["SCF"] - min_)

avgisos["mean_ref"]=[ex_en[i].mean() for i in \
        [major,minor]+[j for j in bla_bins_maj]+[j for j in bla_bins_min]]
avgisos["err"]=avgisos["ex_en"]-avgisos["mean_ref"]


