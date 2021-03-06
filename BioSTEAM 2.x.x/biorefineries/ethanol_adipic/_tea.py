#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# BioSTEAM: The Biorefinery Simulation and Techno-Economic Analysis Modules
# Copyright (C) 2020, Yoel Cortes-Pena <yoelcortes@gmail.com>
# Bioindustrial-Park: BioSTEAM's Premier Biorefinery Models and Results
# Copyright (C) 2020, Yalin Li <yalinli2@illinois.edu> (this biorefinery)
# 
# This module is under the UIUC open-source license. See 
# github.com/BioSTEAMDevelopmentGroup/biosteam/blob/master/LICENSE.txt
# for license details.


# %%

from biorefineries.cornstover import CellulosicEthanolTEA

__all__ = ('EthanolAdipicTEA',)

class EthanolAdipicTEA(CellulosicEthanolTEA):
    
    __slots = (*CellulosicEthanolTEA.__slots__, '_TCI_ratio_cached')
    
    # For uncertainty analysis
    _TCI_ratio_cached = 1
    

