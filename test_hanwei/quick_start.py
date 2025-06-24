# import sys
# sys.path.append()

import os,sys

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.append(project_root)


# sys.path.append("/home/unstructured")
sys.path.appen(os.path.join(project_root,'unstructured'))


from unstructured.partition.auto import partition
elements = partition("/home/unstructured/materials/现行_GB51222-2017_《城镇内涝防治技术规范》.pdf")


