# Model Contingency Table Evaluator
# Shawn Young - styoung@my.ccsu.edu
"""
This function returns metrics for evalutating cross-tabluations generated
by C&R Trees and C4/5.0
"""
print("----------------------------------------------------")
def mevaluate(Model_Name, Tn, Fn, Fp, Tp):
    N = Tn + Fn + Fp + Tp
    
    print(Model_Name)
    print("Accuracy:"), (Tn + Tp) / N
    print("Overall Error Rate:"), 1 - ((Tn + Tp) / N)
    print("Sensitivity:"), Tp / (Tp + Fn)
    print("Specificity:"), Tn / (Fp + Tn)
    print("False Positive Rate:"), 1 - (Tn / (Fp + Tn))
    print("False Negative Rate:"), 1 - (Tp / (Tp + Fn))
    print("Proportion of True Positives:"), Tp / (Fp + Tp)
    print("Proportion of True Negatives:"), Tn / (Fn + Tn)
    print("Proportion of False Positives:"), 1 - (Tp / (Fp + Tp))
    print("Proportion of False Negatives:"), 1 - (Tn / (Fn + Tn))
    print("----------------------------------------------------")
"""
Call function mevaluate by replacing the existing input in the format:
mevaluate("Model Name", Tn.0, Fn.0, Fp.0, Tp.0)
"""


mevaluate("No Interest", 13730.0, 743.0, 11204.0, 24021.0)
mevaluate("RS1", 10462.0, 5.0, 14472.0, 24759.0)
mevaluate("RS2", 18263.0, 7116.0, 6671.0, 17648.0)
mevaluate("RS3", 12315.0, 201.0, 12619.0, 24563.0)
mevaluate("RS4", 19692.0, 4603.0, 5242.0, 20161.0)




