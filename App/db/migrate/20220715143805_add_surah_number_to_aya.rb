class AddSurahNumberToAya < ActiveRecord::Migration[6.1]
  def change
    add_column :ayas, :surah_number, :integer
  end
end
