## 学んだこと

「クラス」はオブジェクトを生成するモノ、オブジェクトを定義。
オブジェクトが何を持っているのか表せる。

「オブジェクト」はモノ・部品、データとメソッド、関数を持っている。
「オブジェクト」はモノでモノは処理のまとまり

上位互換、下位互換は継承の関係性にある。
継承されたモノより良いモノ、上のもの、上位互換。

リストは１〜１００までのデータがあれは１から順番に呼び出し返すのに対し、辞書型はキーワードを呼び出し値を返すので、辞書型は早い。「パフォーマンスがいい」

- 新しくファイルを作る時は、意味のある名前にする。

mutable など im をつけるだけで反対の意味になる単語もある。

## 問題

class_member_score_list = [100, 21, 73, 85, 99, 12, 55, 65, 43]

```
### best score
print("class's best score is :", 100)

### worst score
print("class's worst score is :", 12)

### average score
print("class's average score is :", 61.4)

### max関数で最大値をlistから算出
print(max(class_member_score_list))

### min関数で最小値をlistから算出
print(min(class_member_score_list))


### 平均値はまずsum関数で合計値を出し要素数（長さ）(要素数の数（９）で割る)を取得するlen関数で求める


ave = sum(class_member_score_list) / len(class_member_score_list)
print(ave)
```
