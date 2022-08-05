class CreateTafseers < ActiveRecord::Migration[6.1]
  def change
    create_table :tafseers do |t|
      t.string :tafser
      t.string :ayanumber
      t.integer :chapter_number

      t.timestamps
    end
  end
end
