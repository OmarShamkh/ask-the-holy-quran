class AddSurahNameToAya < ActiveRecord::Migration[6.1]
  def change
    add_column :ayas, :surah_name, :string
  end
end
