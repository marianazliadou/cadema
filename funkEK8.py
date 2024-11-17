import math


# ΑΡΙΣΤΕΡΑ
# ΘΕΤΙΚΗ ΣΕΙΣΜΙΚΗ ΦΟΡΑ
def SMRc_ar_t(MRc_1a, MRc_2t) -> float:
    return abs(MRc_1a) + MRc_2t


def SMRb_ar_t(MRb1l_a, MRb_1t) -> float:
    return abs(MRb1l_a) + MRb_1t


# ΑΡΝΗΤΙΚΗ ΣΕΙΣΜΙΚΗ ΦΟΡΑ
def SMRc_ar_a(MRc_1t, MRc_2a) -> float:
    return MRc_1t + abs(MRc_2a)


def SMRb_ar_a(MRb1l_t, MRb_1a) -> float:
    return MRb1l_t + abs(MRb_1a)


# ΔΕΞΙΑ
# ΘΕΤΙΚΗ ΣΕΙΣΜΙΚΗ ΦΟΡΑ
def SMRc_de_t(MRc_3a, MRc_4t) -> float:
    return abs(MRc_3a) + MRc_4t


def SMRb_de_t(MRb2r_t, MRb_2a) -> float:
    return MRb2r_t + abs(MRb_2a)


# ΑΡΝΗΤΙΚΗ ΣΕΙΣΜΙΚΗ ΦΟΡΑ
def SMRc_de_a(MRc_3t, MRc_4a) -> float:
    return MRc_3t + abs(MRc_4a)


def SMRb_de_a(MRb2r_a, MRb_2t) -> float:
    return abs(MRb2r_a) + MRb_2t


#ΡΟΠΕΣ
def Mid_b(grd, MR, SMRc, SMRb) -> float:
    return grd * MR * (SMRc / SMRb)


def Mid_bu(grd, MR, SMRb, SMRc) -> float:
    if SMRc == 0:
      return 0
    else:
      return grd * MR * (SMRb / SMRc)


def Mid_s(grd, MR) -> float:
    return grd * MR


def DV(M1, M2, lcl) -> float:
    return (abs(M1) + abs(M2)) / lcl



def VEd_t_ar(V0_i, DV) -> float:
    return  V0_i + DV


def VEd_t_de(V0_i, DV) -> float:
    return  - V0_i + DV


def VEd_a_ar(V0_i, DV) -> float:
    return  V0_i - DV


def VEd_a_de(V0_i, DV) -> float:
    return  - V0_i - DV




# ΤΕΜΝΟΥΣΕΣ ΔΟΚΩΝ
def Vd_B(grd, MRb1, SMRc1, SMRb1, lcl, MRb2, V0_i, SMRc2, SMRb2) -> float:
    return ((grd * (MRb1 * (SMRc1 / SMRb1)) + (MRb2 * (SMRc2 / SMRb2))) / lcl) + V0_i


def Vd_b(grd, MRb1, MRb2, lcl, V0_i) -> float:
    return ((grd * (MRb1 + MRb2)) / lcl) + V0_i


def Vd_b1(grd, MRb1, MRb2, SMRc, SMRb, lcl, V0_i) -> float:
    return ((grd * (MRb1 * (SMRc / SMRb)) + MRb2) / lcl) + V0_i


def Vd_b2(grd, MRb1, MRb2, SMRc, SMRb, lcl, V0_i) -> float:
    return ((grd * (MRb1 + (MRb2 * (SMRc / SMRb)))) / lcl) + V0_i



# ΤΕΜΝΟΥΣΕΣ ΥΠΟΣΤΥΛΩΜΑΤΩΝ
def Vd_C(grd, MRc1, SMRc1, SMRb1, MRc2, lcl, SMRc2, SMRb2) -> float:
    if SMRc1 == 0:
      return (grd * + (MRc2 * (SMRb2 / SMRc2))) / lcl
    elif SMRc2 == 0:
        return (grd * (MRc1 * (SMRb1 / SMRc1))) / lcl
    else:
        return (grd * ((MRc1 * (SMRb1 / SMRc1)) + (MRc2 * (SMRb2 / SMRc2)))) / lcl


def Vd_c(grd, MRc1, MRc2, lcl) -> float:
    return (grd * (MRc1 + MRc2)) / lcl


def Vd_c1(grd, MRc1, MRc2, SMRc, SMRb, lcl) -> float:
    return (grd * ((MRc1 * (SMRb / SMRc)) + MRc2)) / lcl


def Vd_c2(grd, MRc1, MRc2, SMRb, SMRc, lcl) -> float:
    return (grd * (MRc1 + (MRc2 * (SMRb / SMRc)))) / lcl


# ΑΝΩ
# ΘΕΤΙΚΗ ΣΕΙΣΜΙΚΗ ΦΟΡΑ
def SMRc_a_t(MRc_1t, MRc1o_a) -> float:
    return MRc_1t + abs(MRc1o_a)


def SMRb_a_t(MRb_2a, MRb_1t) -> float:
    return abs(MRb_2a) + MRb_1t


# ΑΡΝΗΤΙΚΗ ΣΕΙΣΜΙΚΗ ΦΟΡΑ
def SMRc_a_a(MRc_1a, MRc1o_t) -> float:
    return abs(MRc_1a) + MRc1o_t


def SMRb_a_a(MRb_2t, MRb_1a) -> float:
    return MRb_2t + abs(MRb_1a)


# ΚΑΤΩ
# ΘΕΤΙΚΗ ΣΕΙΣΜΙΚΗ ΦΟΡΑ
def SMRc_k_t(MRc_2a, MRc2u_t) -> float:
    return abs(MRc_2a) + MRc2u_t


def SMRb_k_t(MRb_3t, MRb_4a) -> float:
    return MRb_3t + abs(MRb_4a)


# ΑΡΝΗΤΙΚΗ ΣΕΙΣΜΙΚΗ ΦΟΡΑ
def SMRc_k_a(MRc_2t, MRc2u_a) -> float:
    return MRc_2t + abs(MRc2u_a)


def SMRb_k_a(MRb_3a, MRb_4t) -> float:
    return MRb_4t + abs(MRb_3a)





# ΥΠΟΛΟΓΙΣΜΟΙ ΓΙΑ ΙΚΑΝΟΤΙΚΟ ΣΕ ΚΟΜΒΟΥΣ
#ΕΣΩΤΕΡΙΚΟΣ
def SMRc_th(MRc1_p, MRc2_n) -> float:
    return MRc1_p + abs(MRc2_n) 


def SMRc_ar(MRc1_n, MRc2_p) ->float:
    return abs(MRc1_n) + MRc2_p


def SMRb_th(MRb1_p, MRb2_n) -> float:
    return MRb1_p + abs(MRb2_n)


def SMRb_ar(MRb1_n, MRb2_p) -> float:
    return abs(MRb1_n) + MRb2_p

#ΕΞΩΤΕΡΙΚΟΣ
def SMRc_eks_th(MRc1_p, MRc2_n) -> float:
    return MRc1_p + abs(MRc2_n)


def SMRc_eks_arn(MRc2_p, MRc1_n) -> float:
    return MRc2_p + abs(MRc1_n)


#ΓΩΝΙΑΚΟ
def SMRc_g_an(MRc1_p, MRc1_n) -> float:
    return abs(MRc1_p + MRc1_n)


def SMRc_g_kat(MRc2_p, MRc2_n) -> float:
    return abs(MRc2_p + MRc2_n)


def SMRb_g_ar(MRb1_p, MRb1_n) -> float:
    return abs(MRb1_p + MRb1_n)


def SMRb_g_de(MRb2_p, MRb2_n) -> float:
    return abs(MRb2_p + MRb2_n)

