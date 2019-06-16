import sys
import SimpleITK as sitk
from pyntcloud import PyntCloud as pc
import numpy as np
from ml_metrics import rmse

if len(sys.argv) < 3 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print("Usage: compute-metrics.py <input1.ply> <input2.ply>")
    sys.exit(1)

def verify_rmse(a, b):
    n = len(a)
    return np.linalg.norm(np.array(b) - np.array(a)) / np.sqrt(n)

def compare(a, b):
    m = pc.from_file(a).points
    n = pc.from_file(b).points
    m = [ tuple(m.x), tuple(m.y), tuple(m.z) ]; m = m[0]
    n = [ tuple(n.x), tuple(n.y), tuple(n.z) ]; n = n[0]
    v1, v2 = verify_rmse(m, n), rmse(m,n)
    print(v1, v2)

compare(sys.argv[1], sys.argv[2])
