class AddAyaOrderToTafseer < ActiveRecord::Migration[6.1]
  def change
    add_column :tafseers, :aya_order, :string
  end
end
