# -*- coding: utf-8 -*-
"""
Created on Wed May 24 20:05:20 2017

@author: xiaoc
"""

KO_list = [41.440500, 41.350526, 42.241304, 42.934210, 43.892380, 44.974091, 45.184001, 43.682609, 42.677619, 41.979524, 41.523809, 41.345714]
month = range(1, 13)
closeMeansKO  = pd.DataFrame(KO_list, index = month, columns = ['close'])
closeMeansKO.index.name = 'month'
