import math 

#komvos
def acd(grd, SMR, SME) -> float:
  return grd * (SMR /abs(SME))


def MR(acd, ME) -> float:
  return acd * ME



#dokos
def ΔV_CD(MRb1, MRb2, lb) -> float:
  return 1.20 * ((MRb1 + MRb2) / lb)


def Vb(V0b, ΔV_CD) -> float:
  return V0b + ΔV_CD


#ipostiloma
def Vc(MRc1, MRc2, lc) -> float:
  return 1.40 * ((MRc1 + MRc2) / lc)