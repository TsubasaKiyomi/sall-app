# import calculation
# print(calculation.add(1, 2))
# print(calculation.sub(1, 2))

class_member_score_list = [100, 21, 73, 85, 99, 12, 55, 65, 43]

# best score
print("class's best score is :", 100)

# worst score
print("class's worst score is :", 12)

# average score
print("class's average score is :", 61.4)

# max関数で最大値をlistから算出
print(max(class_member_score_list))

# min関数で最小値をlistから算出
print(min(class_member_score_list))


# 平均値はまずsum関数で合計値を出し要素数（長さ）を取得するlen関数で求める
ave = sum(class_member_score_list) / len(class_member_score_list)
print(ave)
