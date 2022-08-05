class AddAyaNumberToTafseer < ActiveRecord::Migration[6.1]
  def change
    add_column :tafseers, :aya_number, :integer
  end
end
