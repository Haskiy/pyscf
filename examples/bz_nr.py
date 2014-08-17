from pyscf import gto
from pyscf import scf

mol = gto.Mole()
mol.verbose = 5
mol.output = "out_bz"

mol.atom = [
    ["C", (-0.65830719,  0.61123287, -0.00800148)],
    ["C", ( 0.73685281,  0.61123287, -0.00800148)],
    ["C", ( 1.43439081,  1.81898387, -0.00800148)],
    ["C", ( 0.73673681,  3.02749287, -0.00920048)],
    ["C", (-0.65808819,  3.02741487, -0.00967948)],
    ["C", (-1.35568919,  1.81920887, -0.00868348)],
    ["H", (-1.20806619, -0.34108413, -0.00755148)],
    ["H", ( 1.28636081, -0.34128013, -0.00668648)],
    ["H", ( 2.53407081,  1.81906387, -0.00736748)],
    ["H", ( 1.28693681,  3.97963587, -0.00925948)],
    ["H", (-1.20821019,  3.97969587, -0.01063248)],
    ["H", (-2.45529319,  1.81939187, -0.00886348)],]


mol.basis = {"H": 'cc-pvtz',
             "C": 'cc-pvtz',} # -230.776765415
#mol.basis = {"H": '6-31g',
#             "C": '6-31g',}  # E=-230.621312769

mol.build()

rhf = scf.RHF(mol)
rhf.conv_threshold = 1e-8
print "E=", rhf.scf()
