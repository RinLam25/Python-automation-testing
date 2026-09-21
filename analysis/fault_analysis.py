import pandas as pd
from scipy.stats import chi2_contingency

# API: 4 Critical, 8 Major, 9 Minor
# UI:  1 Critical, 1 Major, 7 Minor
contingency_table = pd.DataFrame(
    [[4, 8, 9], [1, 1, 7]],
    index=["API", "UI"],
    columns=["Critical", "Major", "Minor"],
)

print("Bảng quan sát thực tế:")
print(contingency_table)
print()

chi2, p_value, dof, expected = chi2_contingency(contingency_table)

print("Bảng kỳ vọng (để kiểm tra điều kiện áp dụng):")
print(pd.DataFrame(expected, index=["API", "UI"], columns=["Critical", "Major", "Minor"]))
print()

print(f"Chi-square statistic: {chi2:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Degrees of freedom: {dof}")

so_o_duoi_5 = (expected < 5).sum()
tong_so_o = expected.size
print(f"\nSố ô có giá trị kỳ vọng < 5: {so_o_duoi_5}/{tong_so_o}")

import matplotlib.pyplot as plt

contingency_table.plot(kind="bar", figsize=(8, 5))
plt.title("Phân bố mức độ nghiêm trọng lỗi theo tầng kiểm thử (API vs UI)")
plt.xlabel("Tầng kiểm thử")
plt.ylabel("Số lượng test case")
plt.xticks(rotation=0)
plt.legend(title="Mức độ nghiêm trọng")
plt.tight_layout()
plt.savefig("analysis/severity_by_layer.png")
plt.show()