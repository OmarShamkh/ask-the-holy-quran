class AddTextToAya < ActiveRecord::Migration[6.1]
  def change
    add_column :ayas, :text, :text
  end
end
