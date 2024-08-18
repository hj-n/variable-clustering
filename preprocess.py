import numpy as np
import json
import os
from tqdm import tqdm
from copy import deepcopy



scatterplot_key_list = []


with open("./data/task_and_ambiguity/784745915_result.json") as f:
	data = json.load(f)
	for splot_key in data["ambiguity"]:
		scatterplot_key_list.append(splot_key)


task_and_ambiguity_files = os.listdir('./data/task_and_ambiguity')


clustering_results = {}
for splot_key in scatterplot_key_list:
  clustering_results[splot_key] = []

for file in task_and_ambiguity_files: 
  with open(f"./data/task_and_ambiguity/{file}") as f:
    data = json.load(f)
    lassoResult = data["lassoResult"]
    
    for key in lassoResult:
      with open(f"./data/splots/{key}.json") as ff:
        splot_size = len(json.load(ff))
      clustering = []
      for i in range(splot_size):
        clustering.append("-1")
      
      for clust_idx in lassoResult[key]:
        for i, point_brushed in enumerate(lassoResult[key][clust_idx]):
          if (point_brushed):
            if (clustering[i] == "-1"):
              clustering[i] = str(clust_idx)
            else:
              clustering[i] = str(clust_idx) + "_" + str(clustering[i])
      clustering_results[key].append(deepcopy(clustering))


print(clustering_results)

for splot_key in scatterplot_key_list:
	clustering_results_of_splot = clustering_results[splot_key]
   
	with open(f"./data/preprocessed/{splot_key}.json", "w") as f:
		json.dump(clustering_results_of_splot, f)
  



                              