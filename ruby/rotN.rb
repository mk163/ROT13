
def rand
num = Random.rand(13) + 1
puts "今回はROT" + num.to_s + "です"
return num.to_i
end

def rotN(num)
puts "文字列を入力してください"
cha = gets
result = ""
cha.split(//).each_with_index do |s,i|
end

for i in 0..cha.length - 1 do
  if cha[i].ord > 'z'.ord - num then
    ans = ((cha[i].ord) - 26 + num).chr
  else
    ans = ((cha[i].ord) + num).chr
  end
  result += ans
end
puts result
return result
end

def main
  rotN(rand)
end

main
