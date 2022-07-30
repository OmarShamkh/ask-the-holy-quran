require "json"
path = File.join(File.dirname(__FILE__),'1.json')
hash = JSON.parse(File.read(path))


#get الاية رقم واحد التكست بتاعها فقط   puts hash["verses"][1]["text"] 
# hash1.keys.each do |key| 
#     if key == "verses"
#         hash1["verses"][1]
#     end
# end

# hash.each do |record|
#     #puts record["verses"]["text"]
#     verses = record["verses"]
#     verses.each do |aya|
#       # Aya.create(content: aya["text"])
#       puts aya["text"]
#     end
# end
        hash.each do |record|
          Aya.create(content: record["simple"] , text: record["text"])
          
        end

