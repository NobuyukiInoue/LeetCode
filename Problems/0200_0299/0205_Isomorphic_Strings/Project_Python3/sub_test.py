# -*- coding: utf-8 -*-
 
import re
 
# 対象の文字列
text = "abc123def456efg"
 
# 連続した小文字のアルファベットを置換
result = re.sub(r'[a-z]+', "0", text)
 
print(result) # 01230456340
