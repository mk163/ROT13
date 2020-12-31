
def rand
num = Random.rand(13) + 1
puts "num = " + num.to_s
return num.to_i
end

def rotN(cha,num)
puts "character : "
#cha = gets
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
  char = "kokoasdfrugb"
  rotN(char,rand)
end

main
