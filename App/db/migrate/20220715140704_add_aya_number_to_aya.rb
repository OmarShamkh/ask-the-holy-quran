class AddAyaNumberToAya < ActiveRecord::Migration[6.1]
  def change
    add_column :ayas, :aya_number, :integer
  end
end
